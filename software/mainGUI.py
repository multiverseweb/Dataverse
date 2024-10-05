import tkinter as tk                                                #for GUI
from tkinter import *                                               #for GUI
from tkinter import messagebox                                      #for GUI messages
from PIL import Image, ImageTk                                      #for GUI images
from functools import partial                                       #for calling button functions
import customtkinter                                                #for scrollable GUI frame
import mysql.connector as my                                        #for connecting database
import datetime                                                     #for getting current date
import time                                                         #for getting current time
import webbrowser                                                   #for opening external link
import ctypes as ct                                                 #for styling windows
import financeTracker as financeTracker                             #user defined module - finance
import matplotlib.pyplot as plt                                     #for plotting graphs
import matplotlib                                                   #for plotting graphs
from matplotlib.widgets import Cursor                               #for lines on hover in plot
import numpy as np                                                  #for x-axis time arange
#===================================================================================================================plot colors
colors=["#440154", "#3b528b","#21918c", "#5ec962", "#fde725","#f89540", "#e16462","#b12a90", "#6a00a8", "#0d0887", "#3474eb", "#5ec962", "yellow", "#f89540", "tomato","tan"]
#===================================================================================================================connecting mySQL
mycon=financeTracker.mycon
cursor=financeTracker.cursor
cursor.execute("CREATE TABLE IF NOT EXISTS user (u_id INT PRIMARY KEY, u_name VARCHAR(255), pwd VARCHAR(255), country varchar(50) default 'India')")
cursor.execute("CREATE TABLE IF NOT EXISTS money (u_id INT, fiat FLOAT DEFAULT 0, gold FLOAT DEFAULT 0, stocks FLOAT DEFAULT 0, commodity FLOAT DEFAULT 0, sales FLOAT DEFAULT 0, expenditure FLOAT DEFAULT 0, total DOUBLE AS (fiat + gold + stocks + commodity + sales - expenditure), entryDate date);")
#===================================================================================================================================
#============================================================================================Dataverse Operations
#=============================================================================Login- b1
def login(b1,b2,b3,b4,preview_image):
    switch(b1,b2,b3,b4)
    preview_image.place_forget()
    def show_message():
        message=financeTracker.check_credentials(f"{user.get()}",f"{pwd.get()}")
        word=message.split(' ')[0]
        if word=='Login':
            messagebox.showinfo(title="", message=message,icon="info")
            global menu
            menu.pack_forget()
            form.pack_forget()
            user_menu(message.split(' ')[-1],f"{user.get()}")
        elif word=='No':
            messagebox.showinfo(title="", message=message,icon="info")
        elif word=='Incorrect':
            messagebox.showinfo(title="", message=message,icon="error")
        else:
            messagebox.showinfo(title="", message="Some unknown error occured.",icon="warning")
    global relation
    relation.pack_forget()
    global text
    text.pack_forget()
    global form
    form.pack_forget()
    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=TOP,fill=Y,pady=140,padx=(0,200))
    global title
    title.pack_forget()
    title=Label(form,font="poppins 10",fg='#ffffff',bg='#171717',text="PERSONAL FINANCE TRACKER")
    title.pack(fill=Y,pady=35,padx=0)
    user=StringVar()
    pwd=StringVar()
    user_entry=Entry(form,textvariable=user,width=30)
    pwd_entry=Entry(form,textvariable=pwd,width=30,show="●")
    user_entry.insert(0,'Username')
    pwd_entry.insert(0,'Password')
    user_entry.pack(pady=20,padx=50)
    pwd_entry.pack(pady=20,padx=50)
    Button(form,text="Login",width=15,command=show_message,cursor="hand2").pack(pady=20)
    form.mainloop()

#======================================================================password encryption
def encrypt(pwd):
    n=len(pwd)
    e=""
    t=pwd[int(n/2):]
    t+=pwd[:int(n/2)]
    for _ in range(len(t)):
        e+=chr(ord(t[_])*2)
    return e 
#====================================================================== Create account -b2
def create(b2,b1,b3,b4,preview_image):
    def show_message(u_name,pwd,country,names):
        u_name=f"{u_name.get()}"
        pwd=f"{pwd.get()}"
        pwd=encrypt(pwd)
        country=f"{country.get()}"
        if u_name in names:
            messagebox.showinfo(title="Username Not Available", message="That username is already taken. Try another one.",icon="info")
        else:
            u_id = datetime.datetime.now().strftime("%H%M%S")
            q="insert into user values({},'{}','{}','{}')".format(u_id,u_name,pwd,country)
            cursor.execute(q)
            mycon.commit()
            msg="Account Created Successfully! ✓\nYour User ID is: {}\n".format(u_id)
            global text
            text=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text=msg)
            text.pack(fill=X,pady=35,padx=(0,200))
            messagebox.showinfo(title="Important", message="This User ID is required while deleting the account.",icon="warning")

    switch(b2,b1,b3,b4)
    preview_image.place_forget()
    names=[]
    q="select u_name from user"
    cursor.execute(q)
    data=cursor.fetchall()
    for i in data:
        names.append(i[0])
    global relation
    relation.pack_forget()
    global text
    text.pack_forget()
    global form
    form.pack_forget()
    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=TOP,fill=Y,pady=140,padx=(0,200))
    global title
    title.pack_forget()
    title=Label(form,font="poppins 10",fg='#ffffff',bg='#171717',text="Create Dataverse Account")
    title.pack(fill=Y,pady=35,padx=0)
    u_name=StringVar()
    pwd=StringVar()
    country=StringVar()
    user_entry=Entry(form,textvariable=u_name,width=30)
    pwd_entry=Entry(form,textvariable=pwd,width=30)
    country_entry=Entry(form,textvariable=country,width=30)
    user_entry.insert(0,'Username')
    pwd_entry.insert(0,'Password')
    country_entry.insert(0,'India')
    user_entry.pack(pady=20,padx=50)
    pwd_entry.pack(pady=20,padx=50)
    country_entry.pack(pady=20,padx=50)
    Button(form,text="Create Account",width=15,command=partial(show_message,u_name,pwd,country,names),cursor="hand2").pack(pady=20)

    form.mainloop()
#=========================================================================GUEST
def guest(b1,b2,b3,b4,preview_image):
    switch(b1,b2,b3,b4)
    global relation
    relation.pack_forget()
    global text
    text.pack_forget()
    global form
    form.pack_forget()
    preview_image.place_forget()
    global menu
    menu.pack_forget()
    menu=Frame(root,bg="#171717",relief=SUNKEN)
    menu.pack(side=LEFT,fill=Y)
    global title
    title.pack_forget()
    title=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text="DATA VISUALISATION SOFTWARE")
    title.pack(fill=X,pady=35,padx=(0,200))

    b1=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Line Graph",width=22,font="poppins 10",cursor="hand2")
    b2=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Bar Graph",width=22,font="poppins 10",cursor="hand2")
    b3=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Scatter Plot",width=22,font="poppins 10",cursor="hand2")
    b4=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Area Chart",width=22,font="poppins 10",cursor="hand2")
    b5=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Histogram",width=22,font="poppins 10",cursor="hand2")
    b6=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Pie Chart",width=22,font="poppins 10",cursor="hand2")
    b7=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Heatmap",width=22,font="poppins 10",cursor="hand2")
    b8=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Radar Chart",width=22,font="poppins 10",cursor="hand2")
    b9=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Polar Scatter Plot",width=22,font="poppins 10",cursor="hand2")
    b10=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Plot Equations",width=22,font="poppins 10",cursor="hand2")
    b11=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Maps",width=22,font="poppins 10",cursor="hand2")
    b13=Button(menu,fg='#ffffff',bg='#1a1a1a',text="3d Scatter",width=22,font="poppins 10",cursor="hand2")
    b14=Button(menu,fg='#ffffff',bg='#1a1a1a',text="3D Surface",width=22,font="poppins 10",cursor="hand2")
    b12=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Live Graphs",width=22,font="poppins 10",cursor="hand2")
    b15=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Go to Home",width=22,font="poppins 10",command=main,cursor="hand2")

    b1.config(command=partial(line,c="line"))
    b2.config(command=partial(line,c="bar"))
    b3.config(command=partial(line,c="scatter"))
    b4.config(command=partial(line,c="area"))
    b5.config(command=partial(line,c="hist"))
    b8.config(command=partial(line,c="radar"))
    b9.config(command=partial(line,c="polar"))
    b6.config(command=partial(pie,c="pie"))
    
    b1.pack(pady=(30,5),padx=15)
    b2.pack(pady=5,padx=15)
    b3.pack(pady=5,padx=15)
    b4.pack(pady=5,padx=15)
    b5.pack(pady=5,padx=15)
    b6.pack(pady=5,padx=15)
    b7.pack(pady=5,padx=15)
    b8.pack(pady=5,padx=15)
    b9.pack(pady=5,padx=15)
    b10.pack(pady=5,padx=15)
    b11.pack(pady=5,padx=15)
    b13.pack(pady=5,padx=15)
    b14.pack(pady=5,padx=15)
    b12.pack(pady=5,padx=15)
    b15.pack(pady=30,padx=15)
#==================================================================================Delete Account- b4
def delete(b4,b1,b3,b2,preview_image):
    def show_message(u_name,u_id,pwd,names):
        u_name=f"{u_name.get()}"
        u_id=u_id.get()
        pwd=f"{pwd.get()}"
        if u_name in names:
            q="select u_id,pwd from user where u_name='{}'".format(u_name)
            cursor.execute(q)
            data=cursor.fetchall()
            if u_id==data[0][0] and pwd==data[0][1]:
                cursor.execute("delete from user where u_id={}".format(u_id))
                mycon.commit()
                cursor.execute("delete from money where u_id={}".format(u_id))
                mycon.commit()
                messagebox.showinfo(title="", message="Account deleted successfully. ✓",icon="info")
            else:
                messagebox.showinfo(title="Attempt failed.", message="Invalid credentials. ✖",icon="error")

        else:
            messagebox.showinfo(title="Error", message="Account not found. ✖",icon="error")

    switch(b4,b1,b3,b2)
    preview_image.place_forget()
    names=[]
    q="select u_name from user"
    cursor.execute(q)
    data=cursor.fetchall()
    for i in data:
        names.append(i[0])
    global relation
    relation.pack_forget()
    global text
    text.pack_forget()
    global form
    form.pack_forget()
    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=TOP,fill=Y,pady=140,padx=(0,200))
    global title
    title.pack_forget()
    title=Label(form,font="poppins 10",fg='#ffffff',bg='#171717',text="Delete Dataverse Account")
    title.pack(fill=Y,pady=35,padx=0)
    u_name=StringVar()
    u_id=IntVar()
    pwd=StringVar()
    user_entry=Entry(form,textvariable=u_name,width=30)
    user_id=Entry(form,textvariable=u_id,width=30)
    pwd_entry=Entry(form,textvariable=pwd,width=30)
    user_entry.insert(0,'Username')
    user_id.insert(0,'User I')
    pwd_entry.insert(0,'Password')
    user_entry.pack(pady=20,padx=50)
    user_id.pack(pady=20,padx=50)
    pwd_entry.pack(pady=20,padx=50)
    Button(form,text="Delete Account",width=15,command=partial(show_message,u_name,u_id,pwd,names),cursor="hand2").pack(pady=20)

    form.mainloop()
#=============================================================================================USER OPERATIONS
#===========================================================================Menu after login
def user_menu(u_id,u_name):
    global relation
    relation.pack_forget()
    global form
    form.pack_forget()
    global menu
    menu.pack_forget()
    global text
    text.pack_forget()
    menu=Frame(root,bg="#171717",relief=SUNKEN)
    menu.pack(side=LEFT,fill=Y)
    global title
    title.pack_forget()
    #text=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text="PERSONAL FINANCE TRACKER")
    #text.pack(fill=X,pady=35,padx=(0,200))

    profile=Frame(root,bg="#171717",relief=SUNKEN,width=25,height=100)
    profile.pack(side=RIGHT,fill=Y,anchor=NE)
    q="select entryDate from money where u_id={}".format(u_id)
    cursor.execute(q)
    data=cursor.fetchall()
    since="NA"
    last="NA"
    if len(data)!=0:
        since=data[0][0].strftime("%d-%m-%y")
        last=data[-1][0].strftime("%d-%m-%y")
    name=Label(profile,font="poppins 10 bold",fg='#ffffff',bg='#171717',text="{}\n\n\nMember since: {}\n\nLast active on: {}".format(u_name.title(),since,last))
    name.pack(fill=X,padx=30,pady=10)

    b1=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Add Data",width=22,font="poppins 10",command=partial(insert,u_id,u_name),cursor="hand2")
    b2=Button(menu,fg='#ffffff',bg='#1a1a1a',text="View Data",width=22,command=partial(view,u_id,u_name),font="poppins 10",cursor="hand2")
    b3=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Visualise Data",width=22,font="poppins 10",command=partial(visualize,u_name),cursor="hand2")
    b5=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Delete Data",width=22,font="poppins 10",command=partial(delete_data,u_id),cursor="hand2")
    b4=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Save & Logout",width=22,command=main,font="poppins 10",cursor="hand2")
    
    b1.pack(pady=(30,5),padx=15)
    b2.pack(pady=5,padx=15)
    b3.pack(pady=5,padx=15)
    b5.pack(pady=5,padx=15)
    b4.pack(pady=5,padx=15)
    b4.config(command=partial(clear,menu,text,profile))

def view(u_id,u_name):
    result=financeTracker.view_data(u_id)
    global form
    form.pack_forget()
    global relation
    relation.pack_forget()
    relation=customtkinter.CTkScrollableFrame(root,
                                                width=900,
                                                height=700,
                                                label_text="{}'s Data".format(u_name.title()),
                                                border_width=1,
                                                fg_color="#000000",
                                                scrollbar_button_hover_color="#ffffff"
                                                )
    relation.pack(side=TOP,fill=Y,pady=40)
    title=Label(relation,font="Courier 10",fg='#ffffff',bg='#000000',text=result)
    title.grid(row=3,column=2)
#=========================================================================Visualize data
def visualize(u_name):
    global relation
    relation.pack_forget()
    global form
    form.pack_forget()
    global text
    text.pack_forget()
    q="select u_id from user where u_name='{}'".format(u_name)
    cursor.execute(q)
    u_id=cursor.fetchall()[0][0]
    requireds=financeTracker.fetch_data(u_id)                             #in progress
    if requireds==None:
            messagebox.showinfo(title="", message="Not enough data to visualize. ✖",icon="warning")
    else:
        values=financeTracker.plot_data(requireds,u_name)
        report="Total Amount= {}\nMax Till Now= {}".format(values[0],values[1])
        text=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text=report)
        text.pack(fill=X,pady=35,padx=(0,200))
#==========================================================================================insert data
def insert(u_id,u_name):
    def show_message():
        ti=str(time.strftime('%y-%m-%d'))
        q="insert into money (u_id,salary,gold,stocks,commodity,sales,expenditure,entryDate) values({},{},{},{},{},{},{},'{}')".format(u_id,variables[0].get(),variables[1].get(),variables[2].get(),variables[3].get(),variables[4].get(),variables[5].get(),ti)
        cursor.execute(q)
        mycon.commit()
        messagebox.showinfo(title="", message="Data added successfully. ✓",icon="info")
    global relation
    relation.pack_forget()
    global form
    form.pack_forget()
    global text
    text.pack_forget()
    form=customtkinter.CTkScrollableFrame(root,
                                                  width=900,
                                                  height=500,
                                                  label_text="{}'s Data".format(u_name.title()),
                                                  border_width=1,
                                                  fg_color="#171717",
                                                  scrollbar_button_hover_color="#ffffff"
                                                  )
    form.pack(side=TOP,fill=Y,pady=40,padx=(0,125))
    title=Label(form,font="poppins 10",fg='#ffffff',bg='#171717',text="Enter Today's Data")
    title.pack(fill=Y,pady=35,padx=0)

    cursor.execute("DESCRIBE money")
    schema = cursor.fetchall()
    money=IntVar()
    gold=IntVar()
    stocks=IntVar()
    commodity=IntVar()
    sales=IntVar()
    expenditure=IntVar()
    variables=[money,gold,stocks,commodity,sales,expenditure]
    new=[]
    for i in range(1,7):
        text=Label(form,text=schema[i][0].title()+":\n",bg='#171717',fg='#ffffff')
        text.pack(fill=X,pady=(5,0),padx=(0,0))
        value=Entry(form,textvariable=variables[i-1],width=50)
        value.insert(0,'')
        value.pack(pady=(0,0),padx=50)
    Button(form,text="Add Data",width=15, command=show_message,cursor="hand2").pack(pady=20)
    form.mainloop()

#==========================================================================================delete data
def delete_data(u_id):
    def show(u_id,e_date):
        q="select * from money where u_id={} and entryDate='{}'".format(u_id,e_date.get())
        cursor.execute(q)
        data=cursor.fetchall()
        if len(data)==0:
            messagebox.showinfo(title="", message="Data not found. ✖",icon="warning")
        else:
            q="delete from money where u_id={} and entryDate='{}'".format(u_id,e_date.get())
            cursor.execute(q)
            mycon.commit()
            messagebox.showinfo(title="", message="Data deleted successfully. ✓",icon="info")
    global relation
    relation.pack_forget()
    global form
    form.pack_forget()
    global text
    text.pack_forget()
    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=TOP,fill=Y,pady=140,padx=(0,200))
    title=Label(form,font="poppins 10",fg='#ffffff',bg='#171717',text="Delete Data")
    title.pack(fill=Y,pady=35,padx=0)
    e_date=StringVar()
    date_entry=Entry(form,textvariable=e_date,width=30)
    date_entry.insert(0,'YYYY-MM-DD')
    date_entry.pack(pady=20,padx=50)
    Button(form,text="Delete Data",width=15,command=partial(show,u_id,e_date),cursor="hand2").pack(pady=20)

    form.mainloop()

#=========================================================================Clearing screen
def clear(menu,text,profile):
    menu.pack_forget()
    text.pack_forget()
    profile.pack_forget()
    main()

#=====================================================================disabling buttons
def switch(b1,b2,b3,b4):
    b1["state"] = DISABLED
    b2["state"] = NORMAL
    b3["state"] = NORMAL
    b4["state"] = NORMAL
#==================================================================================open link
def callback(url):
    webbrowser.open_new(url)



#=====================================================================================================================================DATA VISUALIZATION
x = []
y = []
d_attr=[]
count=0
def line(c):
    global form
    form.pack_forget()
    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=LEFT,pady=20,padx=20,anchor=NW)
    global title
    title.pack_forget()
    title_var=StringVar()
    x_var=StringVar()
    y_var=IntVar()
    title_label = Label(form, text = 'Title: ', font=('calibre',10),fg='#ffffff',bg='#171717')
    title_entry = Entry(form,textvariable = title_var, font=('calibre',10))
    x_label = Label(form, text = 'Name of Independent Variable: ', font = ('calibre',10),fg='#ffffff',bg='#171717')
    x_entry=Entry(form, textvariable = x_var, font = ('calibre',10))
    y_label = Label(form, text = 'No. of Dependent Variable(s): ', font = ('calibre',10),fg='#ffffff',bg='#171717')
    y_entry=Entry(form, textvariable = y_var, font = ('calibre',10))
    
    title_entry.insert(0,'Untitled')
    x_entry.insert(0,'x')

    title_label.grid(row=0,column=0,padx=(5,5),pady=(15,5))
    title_entry.grid(row=0,column=1,padx=(0,10),pady=(15,5))
    x_label.grid(row=1,column=0,padx=(5,5),pady=5)
    x_entry.grid(row=1,column=1,padx=(0,10),pady=5)
    y_label.grid(row=2,column=0,padx=(5,5),pady=5)
    y_entry.grid(row=2,column=1,padx=(0,10),pady=5)
    sub_btn=Button(form,text="Create",width=10,cursor="hand2")
    sub_btn.grid(row=3,column=1,padx=(10,15),pady=(15,15))
    if(c=="radar"):
        sub_btn.configure(command=partial(radar_values,c,title_var,x_var,y_var))
    else:
        sub_btn.configure(command=partial(line_values,c,title_var,x_var,y_var))

    form.mainloop()


def line_values(c,title_var,x_var,y_var):
    def y_values(c,y,start,end,width,names_form,x_label):
        if width.get()==0:
            width=width.get()+1
        else:
            width=width.get()
        Label(names_form, text = "For y-axis", font=('calibre',10,"bold"),fg='#ffffff',bg='#171717').grid(row=5,column=0,padx=(15,10),pady=(15,5))
        for i in range(start.get(),end.get()+1,width):
            x.append(i)
            #count+=1
        for i in range(y_var):
            Label(names_form, text = "Dependent Attribute {}: ".format(i+1), font=('calibre',10),fg='#ffffff',bg='#171717').grid(row=6+i,column=0,padx=(15,10),pady=(10,5))
            Entry(names_form,textvariable = d_attr[i], font=('calibre',10)).grid(row=6+i,column=1,padx=(15,10),pady=(10,5))
        enter_btn=Button(names_form,text="Enter Values",width=10,cursor="hand2")
        enter_btn.grid(row=7+y_var,column=1,padx=(10,15),pady=10)
        enter_btn.configure(command=partial(enter_values,c,y,start,end,width,x_label))

    def enter_values(c,y,start,end,width,x_label):
        for i in range(y_var):
            default=[]
            for j in range(start.get(),end.get()+1,width):
                default.append(0)
            y.append(default)
        for i in y:
            for j in i:
                i=IntVar()
        global values_form
        values_form.place_forget()
        values_form=customtkinter.CTkScrollableFrame(root,
                                                  width=230,
                                                  height=665,
                                                  label_text="Dependent Variable(s) Values",
                                                  border_width=1,
                                                  fg_color="#171717",
                                                  scrollbar_button_hover_color="#ffffff",
                                                  border_color="#000000"
                                                  )
        values_form.place(relx=1.0, rely=1.0, x=-930, y=-740,anchor=NW)
        row=0
        entry_widgets = []
        for i in range(len(y)):
            entries=[]
            Label(values_form, text = "For {}".format(d_attr[i].get().title()), font=('calibre',10,"bold"),fg='#ffffff',bg='#171717').grid(row=row,column=0,padx=(15,10),pady=(15,5))
            for j in range(len(y[0])):
                Label(values_form, text = "{}({}={}): ".format(d_attr[i].get(),x_label,x[j]), font=('calibre',10),fg='#ffffff',bg='#171717').grid(row=row+j+1,column=0,padx=(15,10),pady=(10,5))
                #entry=Entry(values_form,textvariable = y[i][j], font=('calibre',10),width=15).grid(row=row+j+1,column=1,padx=(15,10),pady=(10,5))
                entry = Entry(values_form, font=('calibre',10),width=15)
                entry.grid(row=row+j+1,column=1,padx=(15,10),pady=(10,5))
                entry.insert(0,0)
                entries.append(entry)
                row = row+1
            entry_widgets.append(entries)
            row+=len(y[0])
        plot_btn=Button(values_form,text="Plot",width=10,cursor="hand2")
        plot_btn.grid(row=row,column=0,padx=(10,15),pady=10)
        plot_btn.configure(command=partial(plot_line,c,x,y,d_attr,heading,x_label,start,end,width,entry_widgets))

    heading=title_var.get()
    x_label=x_var.get()
    y_var=y_var.get()

    if y_var>16:
        messagebox.showwarning(message="Too many dependent variables!\nThe maximum limit is 16.")
    elif y_var<=0:
        messagebox.showwarning(message="No. of dependent variables should be greater than 0.")
    else:
        global values_form
        values_form.place_forget()
        global names_form
        names_form.place_forget()
        names_form=customtkinter.CTkScrollableFrame(root,
                                                    width=330,
                                                    height=480,
                                                    label_text="{} Values".format(heading),
                                                    border_width=1,
                                                    fg_color="#171717",
                                                    scrollbar_button_hover_color="#ffffff",
                                                    border_color="#000000"
                                                    )
        names_form.place(relx=1.0, rely=1.0, x=-1300, y=-555,anchor=NW)

        start=IntVar()
        end=IntVar()
        width=IntVar()
        Label(names_form, text = "For {}".format(x_label), font=('calibre',10,"bold"),fg='#ffffff',bg='#171717').grid(row=0,column=0,padx=(15,10),pady=(15,5))
        start_label = Label(names_form, text = "{} Start Value: ".format(x_label), font=('calibre',10),fg='#ffffff',bg='#171717')
        start_entry = Entry(names_form,textvariable = start, font=('calibre',10))
        end_label = Label(names_form, text = "{} End Value: ".format(x_label), font = ('calibre',10),fg='#ffffff',bg='#171717')
        end_entry=Entry(names_form, textvariable = end, font = ('calibre',10))
        width_label = Label(names_form, text = "{} Class Width: ".format(x_label), font = ('calibre',10),fg='#ffffff',bg='#171717')
        width_entry=Entry(names_form, textvariable = width, font = ('calibre',10))

        start_label.grid(row=1,column=0,padx=(15,10),pady=(10,5))
        start_entry.grid(row=1,column=1,padx=(10,15),pady=5)
        end_label.grid(row=2,column=0,padx=(15,10),pady=5)
        end_entry.grid(row=2,column=1,padx=(10,15),pady=5)
        width_label.grid(row=3,column=0,padx=(15,10),pady=5)
        width_entry.grid(row=3,column=1,padx=(10,15),pady=5)

        next_btn=Button(names_form,text="Next",width=10,cursor="hand2")
        next_btn.grid(row=4,column=1,padx=(10,15),pady=10)
        next_btn.configure(command=partial(y_values,c,y,start,end,width,names_form,x_label))

        for i in range(y_var):
            d_attr.append("NA")
            d_attr[i]=StringVar()

def plot_line(c,x,y,d_attr,heading,x_label,start,end,width,entry_widgets):
    start=start.get()
    end=end.get()
    #for i in range(start,end+1,width):
        #x.append(i)
        #count+=1

    for i in range(len(entry_widgets)):
        #for j in range(len(y[0])):
        y[i]=[float(entry.get()) for entry in entry_widgets[i]]

    plt.style.use('dark_background')
    fig, ax=plt.subplots(figsize=(6.5, 5))
    plt.subplots_adjust(bottom=0.152,right=0.81)
    width=0.9
    if c=="polar":
        ax = fig.add_subplot(projection='polar')
    for i in range(len(y)):
        if c=="line":
            plt.plot(x,y[i], label=d_attr[i].get(),color=colors[i],linewidth=0.7)
        elif c=="bar":
            plt.bar(x,y[i], label=d_attr[i].get(),color=colors[i],linewidth=0.7,width=width, alpha = 0.7)
            width-=0.2
        elif c=="scatter":
            plt.scatter(x,y[i], label=d_attr[i].get(),color=colors[i],linewidth=0.7)
        elif c=="area":
            plt.fill_between(x, y[i],label=d_attr[i].get(),color=colors[i], alpha = 0.7)
        elif c=="hist":
            for j in range(len(x)):
                x[j]=round(x[j])
            print(x, y[i])
            plt.hist(x, y[i],label=d_attr[i].get(),color=colors[i], alpha = 0.7)                                                #PROBLEM HERE
        elif c=="polar":
            r = 2 * np.random.rand(len(x))
            area = 200 * r**2
            ax.scatter(x, y[i], color=colors[i], s=area, alpha=0.75)
        else:
            messagebox.showerror(message="Some error occured.")
            return
    if c in ["line","bar","scatter","hist","area"]:
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.title(heading)
        plt.xticks(rotation=30)
        plt.xlabel(x_label)
        ax.spines['bottom'].set_color('teal')
        ax.spines['top'].set_color('#ffffff40') 
        ax.spines['right'].set_color('#ffffff40')
        ax.spines['left'].set_color('darkturquoise')
        ax.grid(linestyle = "dashed",linewidth = 1, alpha = 0.25)
    elif c in ["polar"]:
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.title(heading)
        plt.xlabel(x_label)
    #plt.savefig("example.png", dpi=1000)
    financeTracker.move_figure(fig, 865, 125)
    cursor = Cursor(ax, color='red', linewidth=0.5)
    plt.show()

def pie(c):
    if c=="pie":
        global form
        form.pack_forget()
        form=Frame(root,bg="#171717",relief=SUNKEN)
        form.pack(side=LEFT,pady=20,padx=20,anchor=NW)
        global title
        title.pack_forget()
        title_var=StringVar()
        y_var=IntVar()
        title_label = Label(form, text = 'Title: ', font=('calibre',10),fg='#ffffff',bg='#171717')
        title_entry = Entry(form,textvariable = title_var, font=('calibre',10))
        y_label = Label(form, text = 'No. of Variable(s): ', font = ('calibre',10),fg='#ffffff',bg='#171717')
        y_entry=Entry(form, textvariable = y_var, font = ('calibre',10))
        
        title_entry.insert(0,'Untitled')

        title_label.grid(row=0,column=0,padx=(5,5),pady=(15,5))
        title_entry.grid(row=0,column=1,padx=(0,10),pady=(15,5))
        y_label.grid(row=2,column=0,padx=(5,5),pady=5)
        y_entry.grid(row=2,column=1,padx=(0,10),pady=5)
        sub_btn=Button(form,text="Create",width=10,cursor="hand2")
        sub_btn.grid(row=3,column=1,padx=(10,15),pady=(15,15))
        sub_btn.configure(command=partial(pie_values,c,title_var,y_var))

        form.mainloop()
def pie_values(c,title_var,y_var):
    def enter_pie_values(c,y):
        '''for i in range(y_var):
            y.append(0)
            y[i]=IntVar()'''
        global values_form
        values_form.place_forget()
        values_form=customtkinter.CTkScrollableFrame(root,
                                                  width=230,
                                                  height=665,
                                                  label_text="Variable(s) Values",
                                                  border_width=1,
                                                  fg_color="#171717",
                                                  scrollbar_button_hover_color="#ffffff",
                                                  border_color="#000000"
                                                  )
        values_form.place(relx=1.0, rely=1.0, x=-930, y=-740,anchor=NW)
        row=0
        entries=[]
        for i in range(y_var):
            Label(values_form, text = "{}: ".format(d_attr[i].get()), font=('calibre',10),fg='#ffffff',bg='#171717').grid(row=row+1,column=0,padx=(15,10),pady=(10,5))
            #entry=Entry(values_form,textvariable = y[i][j], font=('calibre',10),width=15).grid(row=row+j+1,column=1,padx=(15,10),pady=(10,5))
            entry = Entry(values_form, font=('calibre',10),width=15)
            entry.grid(row=row+1,column=1,padx=(15,10),pady=(10,5))
            #entry.insert(0,0)
            entries.append(entry)
            row = row+1
        row+=1
        plot_btn=Button(values_form,text="Plot",width=10,cursor="hand2")
        plot_btn.grid(row=row,column=0,padx=(10,15),pady=10)
        plot_btn.configure(command=partial(plot_pie,c,y,d_attr,heading,entries))

    y_var=y_var.get()
    heading=title_var.get()
    if y_var>16:
        messagebox.showwarning(message="Too many variables!\nThe maximum limit is 16.")
    elif y_var<=0:
        messagebox.showwarning(message="No. of variables should be greater than 0.")
    else:
        for i in range(y_var):
            d_attr.append("NA")
            d_attr[i]=StringVar()
        global values_form
        values_form.place_forget()
        global names_form
        names_form.place_forget()
        names_form=customtkinter.CTkScrollableFrame(root,
                                                    width=330,
                                                    height=480,
                                                    label_text="{} Values".format(heading),
                                                    border_width=1,
                                                    fg_color="#171717",
                                                    scrollbar_button_hover_color="#ffffff",
                                                    border_color="#000000"
                                                    )
        names_form.place(relx=1.0, rely=1.0, x=-1300, y=-555,anchor=NW)

        Label(names_form, text = "Variable Names", font=('calibre',10,"bold"),fg='#ffffff',bg='#171717').grid(row=5,column=0,padx=(15,10),pady=(15,5))
        for i in range(y_var):
            Label(names_form, text = "Attribute {}: ".format(i+1), font=('calibre',10),fg='#ffffff',bg='#171717').grid(row=6+i,column=0,padx=(15,10),pady=(10,5))
            Entry(names_form,textvariable = d_attr[i], font=('calibre',10)).grid(row=6+i,column=1,padx=(15,10),pady=(10,5))

    enter_btn=Button(names_form,text="Enter Values",width=10,cursor="hand2")
    enter_btn.grid(row=7+y_var,column=1,padx=(10,15),pady=10)
    enter_btn.configure(command=partial(enter_pie_values,c,y))


def plot_pie(c,y,d_attr,heading,entries):
    for i in range(len(d_attr)):
        d_attr[i]=d_attr[i].get()
    plt.style.use('dark_background')
    fig, ax=plt.subplots(figsize=(6.5, 5))
    plt.subplots_adjust(bottom=0.152,right=0.81)
    for i in entries:
        y.append(i.get())
    if c=="pie":
        plt.pie(y, labels=d_attr,colors=colors)
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.title(heading)
    else:
        messagebox.showerror(message="Some error occured.")
        return
    #plt.savefig("example.png", dpi=1000)
    financeTracker.move_figure(fig, 865, 125)
    plt.show()


def radar_values(c,title_var,x_var,y_var):
    def x_no_values(c,y,x_no_value,names_form,x_label):
        if x_no_value.get()<3:
            messagebox.showwarning(message="No. of values for independent variable should be greater than 2.")
        elif x_no_value.get()>16:
            messagebox.showwarning(message="Too many values for independent variable!\nThe maximum limit is 16.")
        else:
            x_no_value = x_no_value.get()
            Label(names_form, text = "For x-axis values", font=('calibre',10,"bold"),fg='#ffffff',bg='#171717').grid(row=5,column=0,padx=(15,10),pady=(15,5))
            global x
            x = [StringVar() for _ in range(x_no_value)]
            for i in range(x_no_value):
                Label(names_form, text = "{} Value {}: ".format(x_label,i+1), font=('calibre',10),fg='#ffffff',bg='#171717').grid(row=6+i,column=0,padx=(15,10),pady=(10,5))
                Entry(names_form,textvariable = x[i], font=('calibre',10)).grid(row=6+i,column=1,padx=(15,10),pady=(10,5))
            nxt_btn=Button(names_form,text="Next",width=10,cursor="hand2")
            nxt_btn.grid(row=7+i,column=1,padx=(10,15),pady=10)
            nxt_btn.configure(command=partial(y_values,c,x,y,x_no_value,x_label))

    def y_values(c,x,y,x_no_value,x_label):
        global values_1_form
        values_1_form.place_forget()
        values_1_form=customtkinter.CTkScrollableFrame(root,
                                                    width=330,
                                                    height=480,
                                                    label_text="{} Values".format(heading),
                                                    border_width=1,
                                                    fg_color="#171717",
                                                    scrollbar_button_hover_color="#ffffff",
                                                    border_color="#000000"
                                                    )
        values_1_form.place(relx=1.0, rely=1.0, x=-1300, y=-555,anchor=NW)
        Label(values_1_form, text = "For y-axis", font=('calibre',10,"bold"),fg='#ffffff',bg='#171717').grid(row=0,column=0,padx=(15,10),pady=(15,5))
        d_attr = [StringVar() for _ in range(y_var)]
        for i in range(y_var):
            Label(values_1_form, text = "Dependent Attribute {}: ".format(i+1), font=('calibre',10),fg='#ffffff',bg='#171717').grid(row=1+i,column=0,padx=(15,10),pady=(10,5))
            Entry(values_1_form,textvariable = d_attr[i], font=('calibre',10)).grid(row=1+i,column=1,padx=(15,10),pady=(10,5))

        enter_btn=Button(values_1_form,text="Enter Values",width=10,cursor="hand2")
        enter_btn.grid(row=2+i,column=1,padx=(10,15),pady=10)
        enter_btn.configure(command=partial(enter_values,c,x,y,x_no_value,x_label,d_attr))        

    def enter_values(c,x,y,x_no_value,x_label,d_attr):
        for i in range(y_var):
            default=[]
            for j in range(x_no_value):
                default.append(0)
            y.append(default)
        for i in y:
            for j in i:
                i=IntVar()
        global values_form
        values_form.place_forget()
        values_form=customtkinter.CTkScrollableFrame(root,
                                                  width=350,
                                                  height=665,
                                                  label_text="Dependent Variable(s) Values",
                                                  border_width=1,
                                                  fg_color="#171717",
                                                  scrollbar_button_hover_color="#ffffff",
                                                  border_color="#000000"
                                                  )
        values_form.place(relx=1.0, rely=1.0, x=-930, y=-740,anchor=NW)
        row=0
        entry_widgets = []
        for i in range(len(y)):
            entries=[]
            Label(values_form, text = "For {}".format(d_attr[i].get().title()), font=('calibre',10,"bold"),fg='#ffffff',bg='#171717').grid(row=row,column=0,padx=(15,10),pady=(15,5))
            for j in range(len(y[0])):
                Label(values_form, text = "{}({}={}): ".format(d_attr[i].get(),x_label,x[j].get()), font=('calibre',10),fg='#ffffff',bg='#171717').grid(row=row+j+1,column=0,padx=(15,10),pady=(10,5))
                entry = Entry(values_form, font=('calibre',10),width=15)
                entry.grid(row=row+j+1,column=1,padx=(15,10),pady=(10,5))
                entry.insert(0,0)
                entries.append(entry)
                row = row+1
            entry_widgets.append(entries)
            row+=len(y[0])
        plot_btn=Button(values_form,text="Plot",width=10,cursor="hand2")
        plot_btn.grid(row=row,column=0,padx=(10,15),pady=10)
        plot_btn.configure(command=partial(plot_radar,c,x,y,d_attr,heading,x_label,x_no_value,entry_widgets))   

    heading=title_var.get()
    x_label=x_var.get()
    y_var=y_var.get()
    
    if y_var>16:
        messagebox.showwarning(message="Too many dependent variables!\nThe maximum limit is 16.")
    elif y_var<=0:
        messagebox.showwarning(message="No. of dependent variables should be greater than 0.")
    else:
        global names_form
        names_form.place_forget()
        names_form=customtkinter.CTkScrollableFrame(root,
                                                    width=330,
                                                    height=480,
                                                    label_text="{} Values".format(heading),
                                                    border_width=1,
                                                    fg_color="#171717",
                                                    scrollbar_button_hover_color="#ffffff",
                                                    border_color="#000000"
                                                    )
        names_form.place(relx=1.0, rely=1.0, x=-1300, y=-555,anchor=NW)

        x_no_value=IntVar()
        Label(names_form, text = "For {}".format(x_label), font=('calibre',10,"bold"),fg='#ffffff',bg='#171717').grid(row=0,column=0,padx=(15,10),pady=(15,5))
        x_no_value_label = Label(names_form, text = "{} Number of values: ".format(x_label), font=('calibre',10),fg='#ffffff',bg='#171717')
        x_no_value_entry = Entry(names_form,textvariable = x_no_value, font=('calibre',10))
        
        x_no_value_label.grid(row=1,column=0,padx=(15,10),pady=(10,5))
        x_no_value_entry.grid(row=1,column=1,padx=(10,15),pady=5)

        next_btn=Button(names_form,text="Next",width=10,cursor="hand2")
        next_btn.grid(row=4,column=1,padx=(10,15),pady=10)
        next_btn.configure(command=partial(x_no_values,c,y,x_no_value,names_form,x_label))

def plot_radar(c,x,y,d_attr,heading,x_label,x_no_value,entry_widgets):
    for i in range(len(entry_widgets)):
        y[i]=[float(entry.get()) for entry in entry_widgets[i]]
    for i in range(len(x)):
        x[i] = x[i].get()
    for i in range(len(d_attr)):
        d_attr[i]=d_attr[i].get()
    plt.style.use('dark_background')
    fig, ax=plt.subplots(figsize=(6.5, 5))
    plt.subplots_adjust(bottom=0.152,right=0.81)                 
    # obtaining angles
    angles = np.linspace(0,2*np.pi,len(x),endpoint=False)
    # concatenate & append to complete circle
    angles = np.concatenate((angles,[angles[0]]))
    x_chart_labels = x[:]
    x.append(x[0])
    for i in range(len(y)):
        y[i].append(y[i][0])
    ax = fig.add_subplot(polar=True)
    for i in range(len(d_attr)):
        ax.plot(angles,y[i],'o-',color=colors[i],linewidth=2,label=d_attr[i])
        ax.fill(angles,y[i],alpha=0.25,color=colors[i])
    plt.xticks(angles[:-1],x_chart_labels)
    plt.tight_layout()
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.title(heading)
    financeTracker.move_figure(fig, 865, 125)    
    plt.show()    
#===========================================================================================================MAIN
def main():
    global relation
    relation.pack_forget()
    global form
    form.pack_forget()
    global title
    title.pack_forget()
    global menu
    menu.pack_forget()
    global text
    text.pack_forget()
    global names_form
    names_form.place_forget()
    global values_form
    values_form.place_forget()
    global values_1_form
    values_1_form.place_forget()
    menu=Frame(root,bg="#171717",relief=SUNKEN)
    menu.pack(side=LEFT,fill=Y)

    text = tk.Text(root, wrap="word",fg="#e8e8e8",bg="#000000",padx=15,pady=15,font="consolas 12",relief="flat")
# Insert some text into the Text widget
    text.insert("end", '''Welcome to Dataverse!\n
We’re excited to have you onboard! Dataverse is your go-to platform for seamless data visualization and efficient financial tracking, built to simplify your workflow and make data handling effortless.\n\nData Visualization
Easily transform raw data into visually appealing charts such as bar graphs, pie charts, and line graphs. It also supports advanced data visualisation techniques like heatmaps, Radar charts, 3D Surface Plots, etc.

You can also download the generated plots for later use.\n\n
Finance Tracking
Managing finances has never been easier! Dataverse’s finance tracking features allow you to monitor expenses, manage income and generate insightful reports. With detailed financial data at your fingertips, you can download and review reports whenever you need, keeping your finances organized and accessible.\n\n\n\n\n\n\n<--- You can visit our website to know more :)''')
    text.pack(pady=20,padx=40,side=TOP,anchor=W,fill=BOTH)

    #version = tk.Text(root, wrap="word",fg="#e8e8e8",bg="#000000",padx=15,pady=15,font="consolas 8",relief="flat")
    #version.insert("end","Current Version: 05.10.2024\nDesigned by Tejas 2023")
    #version.pack(pady=80,padx=40,side=TOP,anchor=W,fill=Y)

    image = Image.open("software/images/preview.png")
    resize_image = image.resize((650, 370))
    preview = ImageTk.PhotoImage(resize_image)
    preview_image=Label(bg='#000000',image = preview, borderwidth=1, relief="solid",padx=15,pady=15)
    preview_image.place(relx=1.0, rely=1.0, x=-40, y=-40,anchor="se")



    b1=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Finance Tracker",width=22,font="poppins 10",cursor="hand2")
    b3=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Data Visualisation",width=22,font="poppins 10",cursor="hand2")
    b2=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Create Account",width=22,font="poppins 10",cursor="hand2")
    b4=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Delete Account",width=22,font="poppins 10",cursor="hand2")
    b3.pack(pady=(30,5),padx=15)
    b1.pack(pady=5,padx=15)
    b2.pack(pady=5,padx=15)
    b4.pack(pady=5,padx=15)
    b1.config(command=partial(login,b1,b2,b3,b4,preview_image))
    b3.config(command=partial(guest,b3,b1,b4,b2,preview_image))
    b2.config(command=partial(create,b2,b1,b3,b4,preview_image))
    b4.config(command=partial(delete,b4,b1,b3,b2,preview_image))

    link1 = Label(menu,fg='#ffffff',bg='#1a1a1a',text="Visit Website",width=22,cursor="hand2",font="poppins 10", relief="sunken")
    link1.pack(pady=280,padx=15)
    link1.bind("<Button-1>", lambda e: callback("https://multiverse-dataverse.netlify.app/"))

    root.mainloop()

def dark(window):
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value),
                         4)

#===============================================================GUI
root=Tk()
#root.config(borderwidth=2, bordercolor='red')
root.geometry("1100x700")
root.title("Dataverse")
root.minsize(600,300)

bg=Image.open('software/images/background.png')

# Resize the image in the given (width, height)
img=bg.resize((1400,860))

# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)
# Show image using label 
label1 = Label( root, image = my_img) 
label1.place(x = 200, y = 0) 

dark(root)
photo = PhotoImage(file = "software/images/2dlogo.png")
root.iconphoto(False, photo)
root.configure(bg="black")
top=Frame(root,bg="#1a1a1a",width=100)
title=Label(top,font="Courier 15 bold",fg='#ffffff',bg='#1a1a1a',text="Dataverse")
title.grid(row = 0, column = 1,padx=0,pady=(20,10))
top.pack(side=TOP,fill=X)
image = Image.open("software/images/3dlogo.png")
resize_image = image.resize((50, 50))
logo = ImageTk.PhotoImage(resize_image)
label = Label(top,bg='#1a1a1a',image = logo)
label.grid(row = 0, column = 0,padx=(15,20),pady=(20,10))


text=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text="")
text.pack(fill=X,pady=35,padx=(0,200))
form=Frame(root,bg="#171717",relief=SUNKEN)
form.pack(side=TOP,fill=Y,pady=0,padx=(0,0))
names_form=Frame(root,bg="#171717",relief=SUNKEN)
names_form.place(relx=1.0, rely=1.0, x=-1300, y=-555,anchor=NW)
values_form=Frame(root,bg="#171717",relief=SUNKEN)
values_form.place(relx=1.0, rely=1.0, x=-1300, y=-555,anchor=NW)
values_1_form=Frame(root,bg="#171717",relief=SUNKEN)
values_1_form.place(relx=1.0, rely=1.0, x=-1300, y=-555,anchor=NW)
relation=customtkinter.CTkScrollableFrame(root,width=0,height=0,border_width=0,fg_color="#000000",scrollbar_button_hover_color="#000000",scrollbar_button_color="#000000")
relation.pack(side=RIGHT)
menu=Frame(root,bg="#171717",relief=SUNKEN)
menu.pack(side=LEFT,fill=Y)
main()
