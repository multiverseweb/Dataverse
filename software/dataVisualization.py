from tkinter import messagebox                                      #for showing messages
from matplotlib.gridspec import GridSpec                            #for showing graph grid
import matplotlib.pyplot as plt                                     #for plotting graphs
import matplotlib                                                   #for plotting graphs
import numpy as np                                                  #for x-axis time arange
import report                                                       #for report pdf
import datetime                                                     #for getting date
from datetime import datetime, timedelta,date                       #for x-axis time class-width
#===============================================================================================================plot colors
colors=["#fde725","#5ec962","#21918c","#3b528b","#440154","#f89540","#cc4778","cyan","#7e03a8","tomato","tan","#0d0887","green","blue","indigo","violet"]
#===============================================================================================================connecting mySQL
import mysql.connector as my
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()
#============================================================================================================fetch user's money data
def fetch_data(u_id):
    q="select * from money where u_id={}".format(u_id)
    cursor.execute(q)
    data=cursor.fetchall()
    if len(data)==0:
        return None
    else:
        cursor.execute("DESCRIBE money")
        schema = cursor.fetchall()
        columns=[]
        for i in schema:
            columns.append(i[0])
        #=make dataframe of values
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

#=======================================================================================================visualize/plot data
def plot_data(requireds,u_name):
    a=messagebox.askyesno(message="Do you want to download today's report?",icon="question")
    if a=="Yes":
        plt.savefig("plot.png", dpi=150)
        report.save(u_name,total)
        messagebox.showinfo(message="Report downloaded. ✓")
    plt.style.use('dark_background')
    fig, ax = plt.subplots(2,2,figsize=(11.4, 6))
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
    ax[1,1].bar(l[-1][index],l[-3][index], color="red",label="Max Expenditure")
    ax[1,1].set_title("Expenditure Till Now")
    ax[1,1].legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)
    ax[1,1].spines['bottom'].set_color('black')
    ax[1,1].spines['top'].set_color('black') 
    ax[1,1].spines['right'].set_color('black')
    ax[1,1].spines['left'].set_color('black')
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
