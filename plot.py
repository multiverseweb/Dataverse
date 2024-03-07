import matplotlib
import mysql.connector as my                                    #required modules
import matplotlib.pyplot as plt 
import numpy as np
import time
import datetime
from datetime import datetime, timedelta,date
import math
import functions                          #user-defined

colors=["#fde725","#5ec962","#21918c","#3b528b","#440154","#f89540","#cc4778","#0d0887","#7e03a8","tomato","tan","cyan","green","blue","indigo","violet"]

#==================================================================================================connecting mySQL
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()
#====================================================================fetch data
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
    fig, ax=plt.subplots()


    columns=requireds[0]
    pool=requireds[1]
    t = np.arange(min(pool["entryDate"]), max(pool["entryDate"]), timedelta(days=1)).astype(datetime)
    only_dates = [x.date().isoformat() for x in t]
    t_new = np.array(only_dates)
    pool_new=[x.strftime('%Y-%m-%d') for x in pool["entryDate"]]

#=====================================================================================================================================
#=====================================================================================================================================DATA WRANGLING
    l=list(pool.values())
    for i in range(1,len(l)-1):
        c=0
        wrangled_data=[]
        for j in range(len(t)):
            if t_new[j] not in pool_new:
                wrangled_data.append((pool[columns[i]][c])/j)
            else:
                wrangled_data.append(pool[columns[i]][c])
                c+=1
        plt.plot(t,wrangled_data, label=columns[i],color=colors[i],linewidth=0.7)
#=====================================================================================================================================
#=====================================================================================================================================

    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
    plt.title("{}_{}".format(u_name.title(),date.today()))
    plt.xlabel("Time")
    plt.ylabel("Amount (₹1 * y)")
    plt.xticks(rotation=30)
    plt.xlim(min(pool["entryDate"]), max(pool["entryDate"]))
    #ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=1)) 
    #plt.ylim(0,101)
    plt.locator_params(axis='y', nbins=21) 
    plt.axvline(x = date.today(), color = 'lime',linewidth = 1,linestyle = "dashed",label="Today")
    #plt.scatter(t,targets, label="Target",color='yellow',marker='*')
    ax.spines['bottom'].set_color('teal')
    ax.spines['top'].set_color('#ffffff40') 
    ax.spines['right'].set_color('#ffffff40')
    ax.spines['left'].set_color('darkturquoise')
    ax.grid(linestyle = "dashed",linewidth = 1, alpha = 0.25)
    plt.rcParams['figure.figsize'] = [15,10]
    #plt.savefig("example.png", dpi=3000)
    plt.show()

