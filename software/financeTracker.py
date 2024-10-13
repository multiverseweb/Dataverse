import tabulate
from tkinter import messagebox
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import report
import datetime
from datetime import datetime, timedelta, date
from matplotlib.widgets import Cursor as lines
import mysql.connector as my
from mysql.connector import Error  # Add Error class for MySQL exception handling

#===============================================================================================================plot colors
colors=["#440154", "#3b528b","#21918c", "#5ec962", "#fde725","#f89540", "#e16462","#b12a90", "#6a00a8", "#0d0887", "#3474eb", "#5ec962", "yellow", "#f89540", "tomato","tan"]

#==================================================================================================connecting MySQL
try:
    mycon = my.connect(host='localhost', user='root', passwd='tejas123', database='finance')
    cursor = mycon.cursor()
except Error as e:
    print(f"Error connecting to MySQL: {e}")
    messagebox.showerror("Database Error", f"Failed to connect to the database: {e}")
    exit()  # Exit the program if the database connection fails

z = 0
#=========================================================================================view data
def view_data(user_id):
    try:
        query = "select * from money where u_id={}".format(user_id)
        cursor.execute(query)
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

#==================================================================================================add data
def check_credentials(username, password):
    try:
        query = "select u_name from user"
        cursor.execute(query)
        user_list = cursor.fetchall()
        usernames = [user[0] for user in user_list]
        if str(username) not in usernames:
            message = "No account exists with that username."
        else:
            query = "select pwd from user where u_name='{}'".format(username)
            cursor.execute(query)
            fetched_password = cursor.fetchall()
            decrypted_password = decrypt(fetched_password[0][0])
            if decrypted_password == password:
                query = "select u_id from user where u_name='{}'".format(username)
                cursor.execute(query)
                user_id = cursor.fetchall()[0][0]
                message = f"Login Successful. ✓\nUser ID: {user_id}"
            else:
                message = "Incorrect password! ✖"
                global z
                z += 1
                if z >= 2:
                    print("There have been more than 1 failed login attempts. Closing the system.")
    except Error as e:
        message = f"Error during login: {e}"
        print(f"Database error: {e}")
    return message

#============================================================================================================fetch user's money data
def fetch_data(user_id):
    try:
        query = "select * from money where u_id={}".format(user_id)
        cursor.execute(query)
        result_set = cursor.fetchall()
        if len(result_set) == 0:
            return None
        else:
            cursor.execute("DESCRIBE money")
            schema = cursor.fetchall()
            column_names = [column[0] for column in schema]
            data_pool = {}
            for column_name in column_names:
                column_data = []
                query = "select {} from money where u_id={}".format(column_name, user_id)
                cursor.execute(query)
                values = cursor.fetchall()
                for value in values:
                    column_data.append(value[0])
                data_pool[column_name] = column_data
            return [column_names, data_pool]
    except Error as e:
        print(f"Error fetching user data: {e}")
        return None

#=======================================================================================================visualize/plot data
def plot_data(requireds, username):
    try:
        download_report = messagebox.askyesno(message="Do you want to download today's report?", icon="question")
        if download_report == "Yes":
            plt.savefig("plot.png", dpi=150)
            report.save(username, total_amount)
            messagebox.showinfo(message="Report downloaded. ✓")

        plt.style.use('dark_background')
        fig, ax = plt.subplots(2, 2, figsize=(10.7, 6))
        plt.subplots_adjust(left=0.08, bottom=0.043, right=0.805, top=0.895, wspace=0.148, hspace=0.374)
        gs = GridSpec(2, 2, width_ratios=[2, 2], height_ratios=[1.5, 1])

        # Create the subplots
        ax[0, 0] = plt.subplot(gs[0, :])
        ax[1, 0] = plt.subplot(gs[1, 0])
        ax[1, 1] = plt.subplot(gs[1, 1])

        for subplot in fig.get_axes():
            subplot.tick_params(bottom=False, labelbottom=False, left=False, right=False, labelleft=False)

        columns = requireds[0]
        data_pool = requireds[1]
        time_range = np.arange(min(data_pool["entryDate"]), date.today() + timedelta(days=2), timedelta(days=1)).astype(datetime)
        formatted_dates = [x.date().isoformat() for x in time_range]
        time_labels = np.array(formatted_dates)
        date_entries = [x.strftime('%Y-%m-%d') for x in data_pool["entryDate"]]

        # Additional plotting logic...
        plt.show()
    except Exception as e:
        print(f"Error in plotting data: {e}")
        messagebox.showerror("Plot Error", f"Failed to plot data: {e}")
    return None

#=========================================================setting position of graph window
def move_figure(fig, x, y):
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        fig.canvas.manager.window.SetPosition((x, y))
    else:
        fig.canvas.manager.window.move(x, y)
