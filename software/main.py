import manage_data as manage_data                 #user defined module - finance
import db_config                                  # database configuration
import db_config                                  # database configuration
#user defined module - finance
import matplotlib.pyplot as plt                   #for plotting graphs
from mpl_toolkits.mplot3d import Axes3D           #for 3d plotting
import matplotlib                                 #for plotting graphs
from matplotlib.widgets import Cursor             #for lines on hover in plot
import datetime
import time
from tkinter import messagebox


mycon=manage_data.mycon
cursor=manage_data.cursor
# Use configured DB name, but keep legacy creation for safety
cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_config.DB_NAME}`;")
cursor.execute(f"USE `{db_config.DB_NAME}`;")
cursor.execute("CREATE TABLE IF NOT EXISTS user (u_id BIGINT PRIMARY KEY, u_name VARCHAR(255), pwd VARCHAR(255), country varchar(50) default 'India')")
cursor.execute("CREATE TABLE IF NOT EXISTS finance (u_id BIGINT, salary FLOAT DEFAULT 0, gold FLOAT DEFAULT 0, stocks FLOAT DEFAULT 0, commodity FLOAT DEFAULT 0, sales FLOAT DEFAULT 0, expenditure FLOAT DEFAULT 0, total FLOAT AS (salary + gold + stocks + commodity + sales - expenditure), entryDate date);")


def login():
    u_name = username_entry.get()
    pwd = password_entry.get()
    country = country_entry.get()

    q = "SELECT u_id, pwd FROM user WHERE u_name=%s"
    cursor.execute(q, (u_name,))
    data=cursor.fetchall()
    if len(data)==0:
        messagebox.showinfo(title="", message="User not found. ✖",icon="warning")
    else:
        if u_name==data[0][0] and pwd==data[0][1]:
            messagebox.showinfo(title="", message="Login successful. ✓",icon="info")
            # Assuming you have a main window or dashboard after successful login
            # For now, we'll just close the login window
            login_window.destroy()
        else:
            messagebox.showinfo(title="", message="Incorrect password. ✖",icon="warning")


def register():
    u_name = username_entry.get()
    pwd = password_entry.get()
    country = country_entry.get()

    q = "SELECT u_id FROM user WHERE u_name=%s"
    cursor.execute(q, (u_name,))
    data=cursor.fetchall()
    if len(data)==0:
        u_id = int(datetime.datetime.now().strftime("%y%m%d%H%M%S"))
        q = "INSERT INTO user (u_id, u_name, pwd, country) VALUES (%s, %s, %s, %s)"
        cursor.execute(q, (u_id, u_name, pwd, country))
        mycon.commit()
        messagebox.showinfo(title="", message="Registration successful. ✓",icon="info")
    else:
        messagebox.showinfo(title="", message="Username already exists. ✖",icon="warning")


def delete_user():
    u_name = username_entry.get()
    pwd = password_entry.get()

    q = "SELECT u_id, pwd FROM user WHERE u_name=%s"
    cursor.execute(q, (u_name,))
    data=cursor.fetchall()
    if len(data)==0:
        messagebox.showinfo(title="", message="User not found. ✖",icon="warning")
    else:
        if u_name==data[0][0] and pwd==data[0][1]:
            cursor.execute("DELETE FROM user WHERE u_id=%s", (data[0][0],))
            mycon.commit()
            messagebox.showinfo(title="", message="User deleted. ✓",icon="info")
            # Also delete associated finance data
            cursor.execute("DELETE FROM finance WHERE u_id=%s", (data[0][0],))
            mycon.commit()
        else:
            messagebox.showinfo(title="", message="Incorrect password. ✖",icon="warning")


def profile():
    u_name = username_entry.get()
    q = "SELECT u_name, country FROM user WHERE u_name=%s"
    cursor.execute(q, (u_name,))
    data=cursor.fetchall()
    if len(data)==0:
        messagebox.showinfo(title="", message="User not found. ✖",icon="warning")
    else:
        messagebox.showinfo(title="Profile", message=f"Username: {data[0][0]}\nCountry: {data[0][1]}",icon="info")


def visualize():
    u_name = username_entry.get()
    q = "SELECT u_name FROM user WHERE u_name=%s"
    cursor.execute(q, (u_name,))
    data=cursor.fetchall()
    if len(data)==0:
        messagebox.showinfo(title="", message="User not found. ✖",icon="warning")
    else:
        q = "SELECT entryDate FROM finance WHERE u_id=%s"
        cursor.execute(q, (data[0][0],))
        dates = [row[0] for row in cursor.fetchall()]

        q = "SELECT salary, gold, stocks, commodity, sales, expenditure FROM finance WHERE u_id=%s"
        cursor.execute(q, (data[0][0],))
        values = [row for row in cursor.fetchall()]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, values[0], label='Salary')
        plt.plot(dates, values[1], label='Gold')
        plt.plot(dates, values[2], label='Stocks')
        plt.plot(dates, values[3], label='Commodity')
        plt.plot(dates, values[4], label='Sales')
        plt.plot(dates, values[5], label='Expenditure')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title(f'Financial Data for {u_name}')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def insert_data():
    u_name = username_entry.get()
    variables = [salary_entry.get(), gold_entry.get(), stocks_entry.get(), commodity_entry.get(), sales_entry.get(), expenditure_entry.get()]
    if not all(v.isdigit() or v.replace('.', '', 1).isdigit() for v in variables):
        messagebox.showinfo(title="", message="Please enter valid numbers for all fields.",icon="warning")
        return

    q = "SELECT u_id FROM user WHERE u_name=%s"
    cursor.execute(q, (u_name,))
    data=cursor.fetchall()
    if len(data)==0:
        messagebox.showinfo(title="", message="User not found. ✖",icon="warning")
    else:
        u_id=data[0][0]
        ti=str(time.strftime('%y-%m-%d'))
        q = ("INSERT INTO finance (u_id, salary, gold, stocks, commodity, sales, expenditure, entryDate) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(q, (
            u_id,
            variables[0].get(),
            variables[1].get(),
            variables[2].get(),
            variables[3].get(),
            variables[4].get(),
            variables[5].get(),
            ti
        ))
        mycon.commit()
        messagebox.showinfo(title="", message="Data inserted. ✓",icon="info")


def delete_data():
    u_name = username_entry.get()
    e_date = date_entry.get()

    q = "SELECT u_id FROM user WHERE u_name=%s"
    cursor.execute(q, (u_name,))
    data=cursor.fetchall()
    if len(data)==0:
        messagebox.showinfo(title="", message="User not found. ✖",icon="warning")
    else:
        u_id=data[0][0]
        q = "SELECT * FROM finance WHERE u_id=%s AND entryDate=%s"
        cursor.execute(q, (u_id, e_date.get()))
        data=cursor.fetchall()
        if len(data)==0:
            messagebox.showinfo(title="", message="Data not found. ✖",icon="warning")
        else:
            q = "DELETE FROM finance WHERE u_id=%s AND entryDate=%s"
            cursor.execute(q, (u_id, e_date.get()))
            mycon.commit()
            messagebox.showinfo(title="", message="Data deleted. ✓",icon="info")


# Create the main window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x300")

# Username and Password fields
tk.Label(login_window, text="Username:").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)
tk.Label(login_window, text="Password:").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)
tk.Label(login_window, text="Country:").pack(pady=5)
country_entry = tk.Entry(login_window)
country_entry.pack(pady=5)

# Login and Register buttons
tk.Button(login_window, text="Login", command=login).pack(pady=10)
tk.Button(login_window, text="Register", command=register).pack(pady=10)
tk.Button(login_window, text="Delete User", command=delete_user).pack(pady=10)
tk.Button(login_window, text="Profile", command=profile).pack(pady=10)
tk.Button(login_window, text="Visualize", command=visualize).pack(pady=10)
tk.Button(login_window, text="Insert Data", command=insert_data).pack(pady=10)
tk.Button(login_window, text="Delete Data", command=delete_data).pack(pady=10)

login_window.mainloop()