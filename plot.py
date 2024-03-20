import matplotlib
from matplotlib.gridspec import GridSpec
import mysql.connector as my                                    #required modules
import matplotlib.pyplot as plt 
import numpy as np
import time
import datetime
from datetime import datetime, timedelta,date
import math
import functions                          #user-defined
import report

colors=["#fde725","#5ec962","#21918c","#3b528b","#440154","#f89540","#cc4778","cyan","#7e03a8","tomato","tan","#0d0887","green","blue","indigo","violet"]
#========================================================================================================================================connecting mySQL
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()
#=============================================================================================================================================fetch data
def fetch_data(u_id):
    q="select * from money where u_id={}".format(u_id)
    cursor.execute(q)
    data=cursor.fetchall()
    if len(data)==0:
        print("Your dataSet is empty.")
        return None
    else:
        cursor.execute("DESCRIBE money")
        schema = cursor.fetchall()
        columns=[]
        for i in schema:
            columns.append(i[0])

#=========================================make dataframe of values
        # initialize data of lists.
        pool = {}
        for i in columns:
            column_values=[]
            q="select {} from money where u_id={}".format(i,u_id)
            cursor.execute(q)
            values=cursor.fetchall()
            for j in values:
                column_values.append(j[0])
            pool[i]=column_values
        requireds=[columns,pool]
        return requireds

#=======================================================================================visualize/plot data

def plot_data(requireds,u_name):
        #style.use("ggplot")
    plt.style.use('dark_background')
    fig, ax = plt.subplots(2,2)

    gs = GridSpec(2, 2, width_ratios=[2,2], height_ratios=[1.5,1])
    
# Create the subplots
    ax[0,0] = plt.subplot(gs[0, :])
    ax[1,0] = plt.subplot(gs[1, 0])
    ax[1,1] = plt.subplot(gs[1, 1])

    for i in fig.get_axes():
        i.tick_params(bottom=False, labelbottom=False, left=False, right=False, labelleft=False)
    

    columns=requireds[0]
    pool=requireds[1]
    t = np.arange(min(pool["entryDate"]), max(pool["entryDate"]) + timedelta(days=2), timedelta(days=1)).astype(datetime)
    only_dates = [x.date().isoformat() for x in t]
    t_new = np.array(only_dates)
    pool_new=[x.strftime('%Y-%m-%d') for x in pool["entryDate"]]

#====================================================================================================================================Line chart
#=====================================================================================================================================DATA WRANGLING
    l=list(pool.values())
    if len(t)>1:
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
            ax[0,0].plot(t,wrangled_data, label=columns[i],color=colors[i],linewidth=0.7)
    else:
        #===================================================================================some error here
        for i in range(1,len(l)-1):
            c=0
            wrangled_data=[]
            for j in range(len(t)):
                if t_new[j] not in pool_new:
                    wrangled_data.append((wrangled_data[j-1]))
                else:
                    wrangled_data.append(pool[columns[i]][c])
                    c+=1
            ax[0,0].scatter(t,wrangled_data, label=columns[i],color=colors[i],marker="*",markersize=50)
#==================================================================================================================================================
#==================================================================================================================================================
    ax[0,0].tick_params(bottom=True, labelbottom=True, left=True, right=True, labelleft=True)
    ax[0,0].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
    ax[0,0].set_title("{}_{}\nLine Chart".format(u_name.title(),date.today()))
    ax[0,0].set_xlabel("Time")
    ax[0,0].set_ylabel("Amount (₹1 * y)")
    #ax[0,0].xticks(rotation=30)
    #ax[0,0].xlim(min(pool["entryDate"]), max(pool["entryDate"]))

    #ax[0,0].xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=1)) 
    #plt.ylim(0,101)

    ax[0,0].locator_params(axis='y', nbins=21) 
    ax[0,0].axvline(x = date.today(), color = 'lime',linewidth = 0.6,linestyle = "dashed",label="Today")
    #plt.scatter(t,targets, label="Target",color='yellow',marker='*')
    ax[0,0].spines['bottom'].set_color('teal')
    ax[0,0].spines['top'].set_color('#ffffff40') 
    ax[0,0].spines['right'].set_color('#ffffff30')
    ax[0,0].spines['left'].set_color('darkturquoise')
    ax[0,0].grid(linestyle = "dashed",linewidth = 1, alpha = 0.25)
    #plt.rcParams['figure.figsize'] = [15,10]

#===================================================================================piechart
    total=l[-2][-1]
    print("TOTAL= INR",total)
    maximum=max(l[-2])
    print("Max till now= ",maximum)
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
    ax[1,0].pie(sectors, explode = explode, colors=colors[:len(columns)])
    ax[1,0].set_title("Pie Chart- {}".format(date.today()))
    ax[1,0].legend(labels=columns[1:len(columns)-2], bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)
    ax[1,0].spines['bottom'].set_color('black')
    ax[1,0].spines['top'].set_color('black') 
    ax[1,0].spines['right'].set_color('black')
    ax[1,0].spines['left'].set_color('black')

    plt.tight_layout()
    from tkinter import messagebox
    a=input("Do you want to download today's report?")
    if a=="y":
        plt.savefig("plot.png", dpi=100)
        report.save(u_name,total)
        print("Report downloaded. ✓")
    plt.show()


