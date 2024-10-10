import tabulate
from tkinter import messagebox  # For showing messages
from matplotlib.gridspec import GridSpec  # For arranging graph grids
import matplotlib.pyplot as plt  # For plotting graphs
import matplotlib  # For backend operations
import numpy as np  # For numerical operations
import report  # Custom module for report generation
import datetime  # For date operations
from datetime import datetime, timedelta, date  # Specific date classes
from matplotlib.widgets import Cursor as LineCursor  # For cursor widget
import mysql.connector as mysql  # For MySQL connections

# =============================================================================================================== Plot Colors
plot_colors = [
    "#440154", "#3b528b", "#21918c", "#5ec962", "#fde725",
    "#f89540", "#e16462", "#b12a90", "#6a00a8", "#0d0887",
    "#3474eb", "#5ec962", "yellow", "#f89540", "tomato", "tan"
]

# ================================================================================================== Connecting to MySQL
try:
    db_connection = mysql.connect(
        host='localhost',
        user='root',
        passwd='tejas123',
        database='finance'
    )
    db_cursor = db_connection.cursor()
except mysql.Error as err:
    messagebox.showerror("Database Connection Error", f"Error connecting to MySQL: {err}")
    raise SystemExit(err)

login_attempts = 0  # To track failed login attempts

# ========================================================================================= View Data
def view_data(user_id):
    try:
        query = f"SELECT * FROM money WHERE u_id={user_id}"
        db_cursor.execute(query)
        records = db_cursor.fetchall()
        if len(records) == 0:
            result = "Your dataSet is empty."
        else:
            columns = [column[0] for column in db_cursor.description]
            table = tabulate.tabulate(records, headers=columns, tablefmt="pretty")
            result = table
        return result
    except mysql.Error as err:
        messagebox.showerror("Database Error", f"Error fetching data: {err}")
        return "An error occurred while fetching data."

# ====================================================================================== Password Decryption
def decrypt_password(encrypted_password):
    try:
        password_length = len(encrypted_password)
        decrypted_password = ""
        if password_length % 2 == 0:
            rearranged_password = encrypted_password[int(password_length / 2):] + encrypted_password[:int(password_length / 2)]
        else:
            rearranged_password = encrypted_password[int(password_length / 2) + 1:] + encrypted_password[:int(password_length / 2) + 1]
        for char in rearranged_password:
            decrypted_char = chr(ord(char) // 2)
            decrypted_password += decrypted_char
        return decrypted_password
    except Exception as e:
        messagebox.showerror("Decryption Error", f"Error decrypting password: {e}")
        return ""

#================================================================================================== Check Credentials
def check_credentials(username, password):
    global login_attempts
    try:
        query = "SELECT u_name FROM user"
        db_cursor.execute(query)
        fetched_data = db_cursor.fetchall()
        username_list = [entry[0] for entry in fetched_data]
        if str(username) not in username_list:
            message = "No account exists with that username."
        else:
            query = f"SELECT pwd FROM user WHERE u_name='{username}'"
            db_cursor.execute(query)
            fetched_password = db_cursor.fetchall()
            if not fetched_password:
                message = "No password found for the given username."
            else:
                decrypted_password = decrypt_password(fetched_password[0][0])
                if decrypted_password == password:
                    query = f"SELECT u_id FROM user WHERE u_name='{username}'"
                    db_cursor.execute(query)
                    user_id_fetch = db_cursor.fetchall()
                    if not user_id_fetch:
                        message = "User ID not found."
                    else:
                        user_id = user_id_fetch[0][0]
                        message = f"Login Successful. ✓\nUser ID: {user_id}"
                else:
                    message = "Incorrect password! ✖"
                    login_attempts += 1
                    if login_attempts >= 2:
                        messagebox.showwarning(
                            "Login Attempts Exceeded",
                            "There have been more than 1 failed login attempts. Closing the system."
                        )
                        # Implement system closure logic here if needed
        return message
    except mysql.Error as err:
        messagebox.showerror("Database Error", f"Error checking credentials: {err}")
        return "An error occurred during login."
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        return "An unexpected error occurred during login."

#============================================================================================================ Fetch User's Money Data
def fetch_data(user_id):
    try:
        query = f"SELECT * FROM money WHERE u_id={user_id}"
        db_cursor.execute(query)
        records = db_cursor.fetchall()
        if len(records) == 0:
            return None
        else:
            db_cursor.execute("DESCRIBE money")
            schema = db_cursor.fetchall()
            columns = [column[0] for column in schema]
            # Initialize data dictionary
            data_pool = {}
            for column in columns:
                column_values = []
                query = f"SELECT {column} FROM money WHERE u_id={user_id}"
                db_cursor.execute(query)
                values = db_cursor.fetchall()
                for value in values:
                    column_values.append(value[0])
                data_pool[column] = column_values
            required_data = [columns, data_pool]
            return required_data
    except mysql.Error as err:
        messagebox.showerror("Database Error", f"Error fetching user's money data: {err}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        return None

#======================================================================================================= Visualize/Plot Data
def plot_data(required_data, username):
    try:
        user_choice = messagebox.askyesno(message="Do you want to download today's report?", icon="question")
        if user_choice:
            plt.savefig("plot.png", dpi=150)
            report.save(username, total)
            messagebox.showinfo(message="Report downloaded. ✓")
        plt.style.use('dark_background')
        fig, axes = plt.subplots(2, 2, figsize=(10.7, 6))
        plt.subplots_adjust(left=0.08, bottom=0.043, right=0.805, top=0.895, wspace=0.148, hspace=0.374)
        grid_spec = GridSpec(2, 2, width_ratios=[2, 2], height_ratios=[1.5, 1])

        # Assign subplots
        axes[0, 0] = plt.subplot(grid_spec[0, :])
        axes[1, 0] = plt.subplot(grid_spec[1, 0])
        axes[1, 1] = plt.subplot(grid_spec[1, 1])

        for axis in fig.get_axes():
            axis.tick_params(bottom=False, labelbottom=False, left=False, right=False, labelleft=False)

        columns = required_data[0]
        data_pool = required_data[1]
        try:
            time_range = np.arange(
                min(data_pool["entryDate"]),
                date.today() + timedelta(days=2),
                timedelta(days=1)
            ).astype(datetime)
        except Exception as e:
            messagebox.showerror("Date Error", f"Error processing dates: {e}")
            return []

        only_dates = [x.date().isoformat() for x in time_range]
        formatted_dates = np.array(only_dates)
        pool_dates = [x.strftime('%Y-%m-%d') for x in data_pool["entryDate"]]

        # ============================================= Line Chart Data Wrangling and Plotting
        values_list = list(data_pool.values())
        main_plot = axes[0, 0]
        for i in range(1, len(values_list) - 2):
            counter = 0
            wrangled_data = []
            for j in range(len(time_range)):
                if formatted_dates[j] not in pool_dates:
                    if wrangled_data:
                        wrangled_data.append(wrangled_data[j - 1])
                    else:
                        wrangled_data.append(0)  # Default value if no previous data
                else:
                    wrangled_data.append(values_list[i][counter])
                    counter += 1
            main_plot.plot(
                time_range,
                wrangled_data,
                label=columns[i].title(),
                color=plot_colors[i],
                linewidth=0.7,
                marker=".",
                markersize=0.0
            )

        # ========================================== Customize Main Plot (Line Chart)
        main_plot.tick_params(bottom=True, labelbottom=True, left=True, labelleft=True)
        main_plot.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
        main_plot.set_title(f"{username.title()}_{date.today()}\nLine Chart")
        main_plot.set_xlabel("Time")
        main_plot.set_ylabel("Amount (₹1 * y)")
        main_plot.locator_params(axis='y', nbins=21)
        main_plot.axvline(x=date.today(), color='lime', linewidth=0.6, linestyle="dashed", label="Today")

        # Fetching maximum total
        try:
            total = values_list[-2][-1]
            maximum = max(values_list[-2])
            query = f"SELECT entryDate FROM money WHERE total={maximum}"
            db_cursor.execute(query)
            max_date_record = db_cursor.fetchall()
            if max_date_record:
                max_date = max_date_record[0][0]
                main_plot.axvline(x=max_date, color='yellow', linewidth=0.6, linestyle="dashed", label="Max_till_now")
        except mysql.Error as err:
            messagebox.showerror("Database Error", f"Error fetching maximum total date: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred while fetching maximum total date: {e}")

        # Customize spines
        try:
            main_plot.spines['bottom'].set_color('teal')
            main_plot.spines['top'].set_color('#ffffff40')
            main_plot.spines['right'].set_color('#ffffff30')
            main_plot.spines['left'].set_color('darkturquoise')
        except Exception as e:
            messagebox.showerror("Spine Customization Error", f"Error customizing spines: {e}")

        main_plot.grid(linestyle="dashed", linewidth=1, alpha=0.25)

        #=================================================================================== Pie Chart
        try:
            sectors = []
            explode = []
            for value in values_list[1:len(values_list) - 2]:
                sectors.append(value[-1])
                explode.append(0)
            if explode:
                explode[-1] = 0.1  # Highlight the last sector

            pie_chart = axes[1, 0]
            pie_chart.pie(sectors, explode=explode, colors=plot_colors[1:len(columns)+1])
            pie_chart.set_title(f"Money Distribution - {date.today()}")
            pie_chart.legend(
                labels=columns[1:len(columns)-2],
                bbox_to_anchor=(1.1, 1),
                loc='upper left',
                borderaxespad=0
            )
            pie_chart.spines['bottom'].set_color('black')
            pie_chart.spines['top'].set_color('black')
            pie_chart.spines['right'].set_color('black')
            pie_chart.spines['left'].set_color('black')
        except Exception as e:
            messagebox.showerror("Pie Chart Error", f"Error creating pie chart: {e}")

        #============================================================================ Bar Graph - Expenditure
        try:
            expenditure = values_list[-3]
            max_expenditure = max(expenditure)
            expenditure_index = expenditure.index(max_expenditure)

            bar_chart = axes[1, 1]
            bar_chart.bar(values_list[-1], expenditure, color=plot_colors[2], label=columns[-3].title())
            bar_chart.tick_params(bottom=True, labelbottom=True, left=True, labelleft=True)
            if expenditure_index != -1:
                bar_chart.bar(values_list[-1][expenditure_index], expenditure[expenditure_index], color="red", label="Max Expenditure")
            bar_chart.set_title("Expenditure Till Now")
            bar_chart.legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)
            bar_chart.spines['bottom'].set_color('black')
            bar_chart.spines['top'].set_color('black')
            bar_chart.spines['right'].set_color('black')
            bar_chart.spines['left'].set_color('black')
            bar_chart.set_xlabel("Time")
            bar_chart.set_ylabel("Expenditure")
            bar_chart.grid(linestyle="dashed", linewidth=1, alpha=0.25)
        except Exception as e:
            messagebox.showerror("Bar Chart Error", f"Error creating bar chart: {e}")

        # ================================================= Set Position of Graph Window
        try:
            move_figure(fig, 220, 170)
        except Exception as e:
            messagebox.showwarning("Window Positioning Warning", f"Could not move figure window: {e}")

        plt.show()
        plt.tight_layout()
        return [total, maximum]
    
# ========================================================== Set Position of Graph Window
def move_figure(fig, x, y):
    try:
        backend = matplotlib.get_backend()
        if backend == 'TkAgg':
            fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")
        elif backend == 'WXAgg':
            fig.canvas.manager.window.SetPosition((x, y))
        else:
            fig.canvas.manager.window.move(x, y)
    except Exception as e:
        messagebox.showwarning("Window Positioning Warning", f"Could not move figure window: {e}")
