import tabulate
from tkinter import messagebox                                      # for showing messages
from matplotlib.gridspec import GridSpec                            # for showing graph grid
import matplotlib.pyplot as plt                                     # for plotting graphs
import matplotlib                                                   # for plotting graphs
import numpy as np                                                  # for x-axis time arange
import report                                                       # for report pdf
import datetime                                                     # for getting date
from datetime import datetime, timedelta, date                       # for x-axis time class-width
from matplotlib.widgets import Cursor as lines
from sklearn.linear_model import LinearRegression
import pandas as pd
#===============================================================================================================plot colors
colors=["#440154", "#3b528b","#21918c", "#5ec962", "#fde725","#f89540", "#e16462","#b12a90", "#6a00a8", "#0d0887", "#3474eb", "#5ec962", "yellow", "#f89540", "tomato","tan"]
#==================================================================================================connecting MySQL
import mysql.connector as my                                    #required modules
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()

#=========================================================================================view data
def view_data(u_id):
    if u_id is None:
        messagebox.showerror("Input Error", "User ID cannot be None.")
        return None

    try:
        q = "SELECT * FROM money WHERE u_id=%s"
        cursor.execute(q, (u_id,))
        data = cursor.fetchall()
        if len(data) == 0:
            result = "Your dataset is empty."
        else:
            columns = [col[0] for col in cursor.description]
            table = tabulate.tabulate(data, headers=columns, tablefmt="pretty")
            result = table
    except my.Error as e:
        messagebox.showerror("Database Error", f"Error retrieving data: {e}")
        result = None
    return result

#==============================================================================================password decryption
def decrypt(pwd):
    n = len(pwd)
    d = ""
    if n % 2 == 0:
        t = pwd[int(n/2):]
        t += pwd[:int(n/2)]
    else:
        t = pwd[int(n/2)+1:]
        t += pwd[:int(n/2)+1]
    for _ in range(len(t)):
        d += chr(ord(t[_]) // 2)
    return d

#==================================================================================================add data
def check_credentials(u_name, passwd):
    if not u_name or not passwd:
        messagebox.showerror("Input Error", "Username and password cannot be empty.")
        return "Username and password cannot be empty."

    try:
        q = "SELECT u_name FROM user"
        cursor.execute(q)
        data = cursor.fetchall()
        names = [i[0] for i in data]

        if str(u_name) not in names:
            message = "No account exists with that username."
        else:
            q = "SELECT pwd FROM user WHERE u_name=%s"
            cursor.execute(q, (u_name,))
            data = cursor.fetchall()
            if data:
                decrypted = decrypt(data[0][0])
                if decrypted == passwd:
                    q = "SELECT u_id FROM user WHERE u_name=%s"
                    cursor.execute(q, (u_name,))
                    u_id = cursor.fetchall()[0][0]
                    message = "Login Successful. ✓\nUser ID: {}".format(u_id)
                else:
                    message = "Incorrect password! ✖"
                    global z
                    z += 1
                    if z >= 2:
                        print("There have been more than 1 failed login attempts. Closing the system.")
            else:
                message = "User not found."
    except my.Error as e:
        message = f"Database error: {e}"
    return message

#============================================================================================================fetch user's money data
def fetch_data(u_id):
    if u_id is None:
        messagebox.showerror("Input Error", "User ID cannot be None.")
        return None

    try:
        q = "SELECT * FROM money WHERE u_id=%s"
        cursor.execute(q, (u_id,))
        data = cursor.fetchall()

        if len(data) == 0:
            return None

        cursor.execute("DESCRIBE money")
        schema = cursor.fetchall()
        columns = [i[0] for i in schema]

        # Make dataframe of values
        pool = {}
        for i in columns:
            column_values = []
            q = "SELECT {} FROM money WHERE u_id=%s".format(i)
            cursor.execute(q, (u_id,))
            values = cursor.fetchall()
            for j in values:
                column_values.append(j[0])
            pool[i] = column_values

        requireds = [columns, pool]
        return requireds
    except my.Error as e:
        messagebox.showerror("Database Error", f"Error fetching data: {e}")
        return None
    
#=======================================================================================================Predictive Analytics (Linear Regression)

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
    monthly_data.plot(kind='bar', color='skyblue')
    plt.title("Monthly Expenditure Comparison")
    plt.xlabel("Month")
    plt.ylabel("Total Expenditure")
    plt.xticks(rotation=45)  
    plt.tight_layout()  
    plt.show()

#=======================================================================================================visualize/plot data
def plot_data(requireds, u_name):
    if requireds is None or not u_name:
        messagebox.showerror("Input Error", "Required data cannot be None or empty.")
        return None

    try:
        a = messagebox.askyesno(message="Do you want to download today's report?", icon="question")
        if a:
            plt.savefig("plot.png", dpi=150)
            report.save(u_name, total)
            messagebox.showinfo(message="Report downloaded. ✓")

        plt.style.use('dark_background')
        fig, ax = plt.subplots(2, 2, figsize=(10.7, 6))
        plt.subplots_adjust(left=0.08, bottom=0.043, right=0.805, top=0.895, wspace=0.148, hspace=0.374)
        gs = GridSpec(2, 2, width_ratios=[2, 2], height_ratios=[1.5, 1])

        # Create the subplots
        ax[0, 0] = plt.subplot(gs[0, :])
        ax[1, 0] = plt.subplot(gs[1, 0])
        ax[1, 1] = plt.subplot(gs[1, 1])

        for i in fig.get_axes():
            i.tick_params(bottom=False, labelbottom=False, left=False, right=False, labelleft=False)

        columns = requireds[0]
        pool = requireds[1]
        t = np.arange(min(pool["entryDate"]), date.today() + timedelta(days=2), timedelta(days=1)).astype(datetime)
        only_dates = [x.date().isoformat() for x in t]
        t_new = np.array(only_dates)
        pool_new = [x.strftime('%Y-%m-%d') for x in pool["entryDate"]]

        #=======================================================================================================================Line chart
        l = list(pool.values())
        f1 = plt.figure(1)
        for i in range(1, len(l) - 1):
            c = 0
            wrangled_data = []
            for j in range(len(t)):
                if t_new[j] not in pool_new:
                    wrangled_data.append(wrangled_data[j - 1])
                else:
                    wrangled_data.append(pool[columns[i]][c])
                    c += 1
            ax[0, 0].plot(t, wrangled_data, label=columns[i].title(), color=colors[i], linewidth=0.7, marker=".", markersize=0.0)

        #==================================================================================================================================
        ax[0, 0].tick_params(bottom=True, labelbottom=True, left=True, right=True, labelleft=True)
        ax[0, 0].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
        ax[0, 0].set_title("{}_{}\nLine Chart".format(u_name.title(), date.today()))
        ax[0, 0].set_xlabel("Time")
        ax[0, 0].set_ylabel("Amount (₹1 * y)")
        ax[0, 0].locator_params(axis='y', nbins=21)
        ax[0, 0].axvline(x=date.today(), color='lime', linewidth=0.6, linestyle="dashed", label="Today")
        ax[0, 0].spines['bottom'].set_color('teal')
        ax[0, 0].spines['top'].set_color('#ffffff40')
        ax[0, 0].spines['right'].set_color('#ffffff30')
        ax[0, 0].spines['left'].set_color('darkturquoise')
        ax[0, 0].grid(linestyle="dashed", linewidth=1, alpha=0.25)

        #===================================================================================piechart
        total = l[-2][-1]
        maximum = max(l[-2])
        q = "SELECT entryDate FROM money WHERE total=%s"
        cursor.execute(q, (maximum,))
        max_date = cursor.fetchall()
        ax[0, 0].axvline(x=max_date, color='yellow', linewidth=0.6, linestyle="dashed", label="Max_till_now")
        sectors = []
        explode = []
        for i in l[1:len(l) - 2]:
            sectors.append(i[-1])
            explode.append(0.1)

        ax[1, 0].pie(sectors, labels=columns[1:len(columns) - 2], explode=explode, autopct='%1.1f%%', startangle=90)
        ax[1, 0].set_title("{}_{}\nPie Chart".format(u_name.title(), date.today()))

        #=================================================================================scatter chart
        ax[1, 1].scatter(pool["entryDate"], pool[columns[-2]], color=colors[-2], label="Scatter")
        ax[1, 1].set_title("{}_{}\nScatter Chart".format(u_name.title(), date.today()))
        ax[1, 1].set_xlabel("Date")
        ax[1, 1].set_ylabel(columns[-2].title())

        #==================================================================saving final plot as .png file
        plt.savefig("plot.png", dpi=150)
        plt.show()
    except Exception as e:
        messagebox.showerror("Plotting Error", f"An error occurred while plotting data: {e}")

#=================================================================================================exit gracefully
def exit():
    try:
        cursor.close()
        mycon.close()
        messagebox.showinfo("Exit", "Exiting the application.")
    except my.Error as e:
        messagebox.showerror("Database Error", f"Error closing the database connection: {e}")
        report.save(u_name,total)
        messagebox.showinfo(message="Report downloaded. ✓")
    plt.style.use('dark_background')
    fig, ax = plt.subplots(2,2,figsize=(10.7, 6))
    plt.subplots_adjust(left=0.08,bottom=0.043,right=0.805,top=0.895,wspace=0.148,hspace=0.374)
    gs = GridSpec(2, 2, width_ratios=[2,2], height_ratios=[1.5,1])

    # Create the subplots
    ax[0,0] = plt.subplot(gs[0, :])
    ax[1,0] = plt.subplot(gs[1, 0])
    ax[1,1] = plt.subplot(gs[1, 1])

    for i in fig.get_axes():
        i.tick_params(bottom=False, labelbottom=False, left=False, right=False, labelleft=False)
    
    columns=requireds[0]
    pool=requireds[1]
    t = np.arange(min(pool["entryDate"]), date.today() + timedelta(days=2), timedelta(days=1)).astype(datetime)
    only_dates = [x.date().isoformat() for x in t]
    t_new = np.array(only_dates)
    pool_new=[x.strftime('%Y-%m-%d') for x in pool["entryDate"]]

#=======================================================================================================================Line chart
#=====================================================================================================================DATA WRANGLING
    l=list(pool.values())
    f1= plt.figure(1)
    for i in range(1,len(l)-1):
        c=0
        wrangled_data=[]
        for j in range(len(t)):
            if t_new[j] not in pool_new:
                wrangled_data.append((wrangled_data[j-1]))
            else:
                wrangled_data.append(pool[columns[i]][c])
                c+=1
        ax[0,0].plot(t,wrangled_data, label=columns[i].title(),color=colors[i],linewidth=0.7,marker=".",markersize=0.0)

#==================================================================================================================================
    ax[0,0].tick_params(bottom=True, labelbottom=True, left=True, right=True, labelleft=True)
    ax[0,0].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
    ax[0,0].set_title("{}_{}\nLine Chart".format(u_name.title(),date.today()))
    ax[0,0].set_xlabel("Time")
    ax[0,0].set_ylabel("Amount (₹1 * y)")
    ax[0,0].locator_params(axis='y', nbins=21) 
    ax[0,0].axvline(x = date.today(), color = 'lime',linewidth = 0.6,linestyle = "dashed",label="Today")
    ax[0,0].spines['bottom'].set_color('teal')
    ax[0,0].spines['top'].set_color('#ffffff40') 
    ax[0,0].spines['right'].set_color('#ffffff30')
    ax[0,0].spines['left'].set_color('darkturquoise')
    ax[0,0].grid(linestyle = "dashed",linewidth = 1, alpha = 0.25)

#===================================================================================piechart
    total=l[-2][-1]
    maximum=max(l[-2])
    q="select entryDate from money where total={}".format(maximum)
    cursor.execute(q)
    max_date=cursor.fetchall()
    ax[0,0].axvline(x = max_date, color = 'yellow',linewidth = 0.6,linestyle = "dashed",label="Max_till_now")
    sectors=[]
    explode=[]
    for i in l[1:len(l)-2]:
        sectors.append(i[-1])
        explode.append(0)
    explode[-1]=0.1

    ax[1,0].pie(sectors, explode = explode, colors=colors[1:len(columns)+1])
    ax[1,0].set_title("Money Distribution- {}".format(date.today()))
    ax[1,0].legend(labels=columns[1:len(columns)-2], bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)
    ax[1,0].spines['bottom'].set_color('black')
    ax[1,0].spines['top'].set_color('black') 
    ax[1,0].spines['right'].set_color('black')
    ax[1,0].spines['left'].set_color('black')

#============================================================================bar graph-expenditure
    max_expend=max(l[-3])
    index=l[-3].index(max_expend)

    ax[1,1].bar(l[-1],l[-3], color=colors[2],label=columns[-3].title())
    ax[1,1].tick_params(bottom=True, labelbottom=True, left=True, right=True, labelleft=True)
    ax[1,1].bar(l[-1][index],l[-3][index], color="red",label="Max Expenditure")
    ax[1,1].set_title("Expenditure Till Now")
    ax[1,1].legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)
    ax[1,1].spines['bottom'].set_color('black')
    ax[1,1].spines['top'].set_color('black') 
    ax[1,1].spines['right'].set_color('black')
    ax[1,1].spines['left'].set_color('black')
    ax[1,1].set_xlabel("Time")
    ax[1,1].set_ylabel("Expenditure")
    ax[1,1].grid(linestyle = "dashed",linewidth = 1, alpha = 0.25)
    move_figure(fig, 220, 170)
    plt.show()
    plt.tight_layout()
    return [total,maximum]

#=========================================================setting position of graph window
def move_figure(fig, x, y):
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        fig.canvas.manager.window.SetPosition((x, y))
    else:
        fig.canvas.manager.window.move(x, y)
