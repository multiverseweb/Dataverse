import tabulate
import db_config
from tkinter import messagebox
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
#import report
import datetime
from datetime import datetime, timedelta, date
from matplotlib.widgets import Cursor as lines
import mysql.connector as my
from mysql.connector import Error
from security import security_manager
from validators import InputValidator
#===============================================================================================================plot colors
colors=["#440154", "#3b528b","#21918c", "#5ec962", "#fde725","#f89540", "#e16462","#b12a90", "#6a00a8", "#0d0887", "#3474eb", "#5ec962", "yellow", "#f89540", "tomato","tan"]
#==================================================================================================connecting MySQL
def get_db_connection():
    """
    Create a secure database connection with proper error handling
    
    Returns:
        mysql.connector.connection: Database connection or None if failed
    """
    try:
        connection = my.connect(
            host=db_config.DB_HOST,
            user=db_config.DB_USER,
            password=db_config.DB_PASSWORD,
            database=db_config.DB_NAME,
            autocommit=False,  # Enable transactions
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            sql_mode='STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO'
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        if db_config.APP_DEBUG:
            messagebox.showerror("Database Error", f"Failed to connect to the database: {e}\n\nPlease check your .env configuration.")
        return None

# Initialize database connection for backward compatibility
try:
    mycon = get_db_connection()
    if mycon:
        cursor = mycon.cursor()
        # Ensure database and tables exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config.DB_NAME}")
        cursor.execute(f"USE {db_config.DB_NAME}")
        mycon.commit()
    else:
        raise Error("Failed to establish database connection")
except Error as e:
    print(f"Error initializing database: {e}")
    if not db_config.APP_DEBUG:
        messagebox.showerror("Database Error", "Failed to connect to the database. Please check your configuration.")
    exit()

z = 0 # Global variable to track failed login attempts

#==================================================================================================secure user operations
def create_user_secure(username: str, password: str, country: str) -> tuple:
    """
    Securely create new user with proper validation and hashing
    
    Args:
        username (str): Username for new account
        password (str): Plain text password
        country (str): User's country
        
    Returns:
        tuple: (success: bool, message: str, user_id: str or None)
    """
    validator = InputValidator()
    
    # Validate inputs
    is_valid, error_msg = validator.validate_username(username)
    if not is_valid:
        return False, f"Invalid username: {error_msg}", None
    
    is_valid, error_msg = validator.validate_password(password)
    if not is_valid:
        return False, f"Invalid password: {error_msg}", None
    
    is_valid, error_msg = validator.validate_country(country)
    if not is_valid:
        return False, f"Invalid country: {error_msg}", None
    
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed", None
    
    try:
        cursor = connection.cursor()
        
        # Check if username already exists (parameterized query)
        check_query = "SELECT u_name FROM user WHERE u_name = %s"
        cursor.execute(check_query, (username,))
        
        if cursor.fetchone():
            return False, "Username already exists", None
        
        # Hash password securely
        try:
            hashed_password = security_manager.hash_password(password)
        except Exception as e:
            return False, f"Password hashing failed: {e}", None
        
        # Generate user ID
        u_id = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        
        # Insert user with parameterized query
        insert_query = """
            INSERT INTO user (u_id, u_name, pwd, country) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (u_id, username, hashed_password, country))
        
        connection.commit()
        return True, f"Account created successfully! User ID: {u_id}", u_id
        
    except Error as e:
        connection.rollback()
        print(f"Database error during user creation: {e}")
        return False, "Failed to create account due to database error", None
    except Exception as e:
        connection.rollback()
        print(f"Unexpected error during user creation: {e}")
        return False, "Failed to create account due to unexpected error", None
    finally:
        if connection:
            connection.close()

def authenticate_user_secure(username: str, password: str) -> tuple:
    """
    Securely authenticate user with proper validation and session management
    
    Args:
        username (str): Username to authenticate
        password (str): Plain text password
        
    Returns:
        tuple: (success: bool, message: str, session_token: str or None)
    """
    validator = InputValidator()
    
    # Basic input validation
    is_valid, error_msg = validator.validate_username(username)
    if not is_valid:
        return False, f"Invalid username format: {error_msg}", None
    
    if not password:
        return False, "Password cannot be empty", None
    
    # Check if account is locked due to failed attempts
    if security_manager.is_account_locked(username):
        return False, "Account temporarily locked due to multiple failed login attempts. Please try again later.", None
    
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed", None
    
    try:
        cursor = connection.cursor()
        
        # Get user data with parameterized query
        query = "SELECT u_id, pwd FROM user WHERE u_name = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        if not result:
            # Record failed attempt even for non-existent users to prevent enumeration
            security_manager.record_failed_attempt(username)
            return False, "Invalid username or password", None
        
        u_id, stored_hash = result
        
        # Verify password
        if security_manager.verify_password(password, stored_hash):
            # Clear any failed attempts on successful login
            security_manager.clear_failed_attempts(username)
            
            # Create session token
            session_token = security_manager.create_session(str(u_id), username)
            return True, "Login successful", session_token
        else:
            # Record failed attempt
            is_locked = security_manager.record_failed_attempt(username)
            if is_locked:
                return False, "Too many failed attempts. Account temporarily locked.", None
            else:
                return False, "Invalid username or password", None
            
    except Error as e:
        print(f"Database error during authentication: {e}")
        return False, "Authentication failed due to database error", None
    except Exception as e:
        print(f"Unexpected error during authentication: {e}")
        return False, "Authentication failed due to unexpected error", None
    finally:
        if connection:
            connection.close()

def validate_user_session(session_token: str) -> tuple:
    """
    Validate user session and return user information
    
    Args:
        session_token (str): Session token to validate
        
    Returns:
        tuple: (is_valid: bool, user_info: dict or None)
    """
    validator = InputValidator()
    
    if not validator.validate_session_token(session_token):
        return False, None
    
    session_info = security_manager.validate_session(session_token)
    if session_info:
        return True, {
            'user_id': session_info['user_id'],
            'username': session_info['username'],
            'last_activity': session_info['last_activity']
        }
    
    return False, None

def logout_user_secure(session_token: str) -> bool:
    """
    Securely logout user by destroying session
    
    Args:
        session_token (str): Session token to destroy
        
    Returns:
        bool: True if logout successful
    """
    return security_manager.destroy_session(session_token)

#=========================================================================================view data
def view_data(user_id):
    """
    Securely view user's financial data using parameterized queries
    
    Args:
        user_id: User ID to fetch data for
        
    Returns:
        str: Formatted data table or error message
    """
    connection = get_db_connection()
    if not connection:
        return "Database connection failed"
    
    try:
        cursor = connection.cursor()
        # Use parameterized query to prevent SQL injection
        query = "SELECT * FROM finance WHERE u_id = %s ORDER BY entryDate DESC"
        cursor.execute(query, (user_id,))
        result_set = cursor.fetchall()
        
        if len(result_set) == 0:
            result_message = "Your dataSet is empty."
        else:
            columns = [col[0] for col in cursor.description]
            result_table = tabulate.tabulate(result_set, headers=columns, tablefmt="pretty")
            result_message = result_table
            
    except Error as e:
        result_message = f"Error fetching data: {e}"
        print(f"Database error: {e}")
    finally:
        if connection:
            connection.close()
            
    return result_message

#==============================================================================================password decryption
def decrypt(encrypted_password):
    password_length = len(encrypted_password)
    decrypted_password = ""
    if password_length % 2 == 0:
        transformed_pwd = encrypted_password[int(password_length / 2):]
        transformed_pwd += encrypted_password[:int(password_length / 2)]
    else:
        transformed_pwd = encrypted_password[int(password_length / 2) + 1:]
        transformed_pwd += encrypted_password[:int(password_length / 2) + 1]
    for character in transformed_pwd:
        decrypted_password += chr(ord(character) // 2)
    return decrypted_password

#==================================================================================================add data (legacy function - kept for backward compatibility)
def check_credentials(username, password):
    """
    Legacy credential checking function - redirects to secure authentication
    
    Args:
        username: Username to check
        password: Password to verify
        
    Returns:
        str: Authentication result message
    """
    success, message, session_token = authenticate_user_secure(username, password)
    
    if success:
        # Extract user ID from session for backward compatibility
        session_info = security_manager.validate_session(session_token)
        if session_info:
            return f"Login Successful. ✓\nUser ID: {session_info['user_id']}"
        else:
            return "Login successful but session creation failed"
    else:
        return message

#============================================================================================================fetch user's finance data
def fetch_data(user_id):
    """
    Securely fetch user's financial data using parameterized queries
    
    Args:
        user_id: User ID to fetch data for
        
    Returns:
        list or None: [column_names, data_pool] or None if no data
    """
    connection = get_db_connection()
    if not connection:
        print("Database connection failed")
        return None
    
    try:
        cursor = connection.cursor()
        
        # Use parameterized query
        query = "SELECT * FROM finance WHERE u_id = %s ORDER BY entryDate"
        cursor.execute(query, (user_id,))
        result_set = cursor.fetchall()
        
        if len(result_set) == 0:
            return None
        else:
            cursor.execute("DESCRIBE finance")
            schema = cursor.fetchall()
            column_names = [column[0] for column in schema]
            data_pool = {}
            
            for column_name in column_names:
                column_data = []
                # Use parameterized query for each column
                query = f"SELECT {column_name} FROM finance WHERE u_id = %s ORDER BY entryDate"
                cursor.execute(query, (user_id,))
                values = cursor.fetchall()
                for value in values:
                    column_data.append(value[0])
                data_pool[column_name] = column_data
            return [column_names, data_pool]
            
    except Error as e:
        print(f"Error fetching user data: {e}")
        return None
    finally:
        if connection:
            connection.close()
#=======================================================================================================Predictive Analytics (Linear Regression)
'''
def predict_future_expenditure(pool):
    if 'entryDate' not in pool or 'total' not in pool:
        print("Missing required columns in pool.")
        return

    try:
        entry_dates = [datetime.strptime(date, '%Y-%m-%d') for date in pool['entryDate']]
    except ValueError as e:
        print(f"Error parsing entryDate: {e}")
        return

    total = pool['total']
    if not isinstance(total, list) or not all(isinstance(x, (int, float)) for x in total):
        print("Invalid total values. Ensure all values are numeric.")
        return
    
    if len(entry_dates) != len(total):
        print("Mismatch in lengths of entryDate and total.")
        return

    X = np.array([i for i in range(len(entry_dates))]).reshape(-1, 1)
    y = np.array(total)

    model = LinearRegression().fit(X, y)

    # Predict for the next 30 days
    future_dates = np.array([i for i in range(len(entry_dates), len(entry_dates) + 30)]).reshape(-1, 1)
    future_predictions = model.predict(future_dates)

    # Plotting
    plt.figure(figsize=(10, 5))
    future_dates_list = [entry_dates[-1] + timedelta(days=i) for i in range(1, 31)]
    plt.plot(entry_dates, y, label="Past Data")
    plt.plot(future_dates_list, future_predictions, label="Predicted", color='red')
    plt.legend()
    plt.title("Future Expenditure Prediction")
    plt.xlabel("Date")
    plt.ylabel("Expenditure")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#=======================================================================================================Monthly Comparison

def monthly_comparison(pool):
    if 'entryDate' not in pool or 'expenditure' not in pool:
        print("Missing required columns in pool.")
        return

    try:
        entry_dates = pd.to_datetime(pool['entryDate'])
    except ValueError as e:
        print(f"Error parsing entryDate: {e}")
        return

    expenditure = pool['expenditure']
    if not isinstance(expenditure, list) or not all(isinstance(x, (int, float)) for x in expenditure):
        print("Invalid expenditure values. Ensure all values are numeric.")
        return

    if len(entry_dates) != len(expenditure):
        print("Mismatch in lengths of entryDate and expenditure.")
        return

    df = pd.DataFrame({'entryDate': entry_dates, 'expenditure': expenditure})

    df['month'] = df['entryDate'].dt.to_period('M')  
    monthly_data = df.groupby('month')['expenditure'].sum()  

    # Plotting
    plt.figure(figsize=(10, 6))
    monthly_data.plot(kind='scatter', color='skyblue')
    plt.title("Monthly Expenditure Comparison")
    plt.xlabel("Month")
    plt.ylabel("Total Expenditure")
    plt.xticks(rotation=45)  
    plt.tight_layout()  
    plt.show()
'''
#=======================================================================================================visualize/plot data
def plot_data(requireds, username):
    try:
        download_report = messagebox.askyesno(message="Do you want to download today's report?", icon="question")
        if download_report == True:
            plt.savefig("plot.png", dpi=150)
            #report.save(username, total_amount)
            messagebox.showinfo(message="Report downloaded. ✓")

        plt.style.use('dark_background')
        fig, ax = plt.subplots(2, 2, figsize=(10.7, 6.6))
        plt.subplots_adjust(left=0.08, bottom=0.043, right=0.805, top=0.895, wspace=0.148, hspace=0.374)
        gs = GridSpec(2, 2, width_ratios=[2, 2], height_ratios=[1.5, 1])

        # Create the subplots
        ax[0, 0] = plt.subplot(gs[0, :])  # Line chart
        ax[1, 0] = plt.subplot(gs[1, 0])  # Pie chart
        ax[1, 1] = plt.subplot(gs[1, 1])  # scatter chart

        for subplot in fig.get_axes():
            subplot.tick_params(bottom=False, labelbottom=False, left=False, right=False, labelleft=False)

        columns = requireds[0]
        data_pool = requireds[1]

        # Generate time labels for x-axis
        time_range = np.arange(min(data_pool["entryDate"]), date.today() + timedelta(days=2), timedelta(days=1)).astype(datetime)
        formatted_dates = [x.date().isoformat() for x in time_range]
        time_labels = np.array(formatted_dates)
        date_entries = [x.strftime('%Y-%m-%d') for x in data_pool["entryDate"]]

        # ================================ Line Chart ====================================
        line_data = list(data_pool.values())
        for i in range(1, len(line_data) - 1):
            current_data = []
            index = 0
            for j in range(len(time_range)):
                if time_labels[j] not in date_entries:
                    current_data.append((current_data[j - 1] if j > 0 else 0))  # Use previous value or 0
                else:
                    current_data.append(data_pool[columns[i]][index])
                    index += 1
            ax[0, 0].plot(time_range, current_data, label=columns[i].title(), color=colors[i], linewidth=0.7, marker=".", markersize=0.0)

        ax[0, 0].tick_params(bottom=True, labelbottom=True, left=True, right=True, labelleft=True)
        ax[0, 0].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
        ax[0, 0].set_title(f"{username.title()}_{date.today()}\nLine Chart")
        ax[0, 0].set_xlabel("Time")
        ax[0, 0].set_ylabel("Amount (₹)")
        ax[0, 0].axvline(x=date.today(), color='lime', linewidth=0.6, linestyle="dashed", label="Today")
        ax[0, 0].grid(linestyle="dashed", linewidth=1, alpha=0.25)

        # Spines customization for the line chart
        ax[0, 0].spines['bottom'].set_color('teal')
        ax[0, 0].spines['top'].set_color('#ffffff40') 
        ax[0, 0].spines['right'].set_color('#ffffff30')
        ax[0, 0].spines['left'].set_color('darkturquoise')

        # ================================ Pie Chart ====================================
        total_amount = line_data[-2][-1]
        pie_data = [val[-1] for val in line_data[1:-2]]
        pie_explode = [0] * (len(pie_data) - 1) + [0.1]  # Explode the last slice

        ax[1, 0].pie(pie_data, explode=pie_explode, colors=colors[1:len(columns) + 1])
        ax[1, 0].set_title(f"Money Distribution - {date.today()}")
        ax[1, 0].legend(labels=columns[1:len(columns) - 2], bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)

        # Spines customization for the pie chart
        ax[1, 0].spines['bottom'].set_color('black')
        ax[1, 0].spines['top'].set_color('black') 
        ax[1, 0].spines['right'].set_color('black')
        ax[1, 0].spines['left'].set_color('black')

        # ================================ scatter Graph (Expenditure) ======================
        expenditure_data = line_data[-3]
        max_expenditure = max(expenditure_data)
        max_index = expenditure_data.index(max_expenditure)

        ax[1, 1].scatter(line_data[-1], expenditure_data, color=colors[2], label=columns[-3].title())
        ax[1, 1].scatter(line_data[-1][max_index], expenditure_data[max_index], color="red", label="Max Expenditure")
        ax[1, 1].set_title("Expenditure Till Now")
        ax[1, 1].legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)
        ax[1, 1].set_xlabel("Time")
        ax[1, 1].set_ylabel("Expenditure")
        ax[1, 1].grid(linestyle="dashed", linewidth=1, alpha=0.25)

        # Spines customization for the scatter chart
        ax[1, 1].spines['bottom'].set_color('black')
        ax[1, 1].spines['top'].set_color('black') 
        ax[1, 1].spines['right'].set_color('black')
        ax[1, 1].spines['left'].set_color('black')

        # Positioning the graph window
        move_figure(fig, 230, 120)
        plt.show()
        plt.tight_layout()

        return [total_amount, max_expenditure]
    except Exception as e:
        print(f"Error in plotting data: {e}")
        messagebox.showerror("Plot Error", f"Failed to plot data: {e}")
        return None


#=========================================================setting position of graph window
def move_figure(fig, x, y):
    backend = matplotlib.get_backend().lower()
    
    if 'tkagg' in backend:
        fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")
    elif 'wxagg' in backend:
        fig.canvas.manager.window.SetPosition((x, y))
    elif 'qt5agg' in backend or 'qtagg' in backend:
        fig.canvas.manager.window.move(x, y)
    else:
        raise NotImplementedError(f"Backend '{backend}' is not fully supported for moving the figure.")
