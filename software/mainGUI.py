from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from functools import partial
import functions
import customtkinter
import plot
import mysql.connector as my   
import datetime
import time
#=============================================================================================================================connecting mySQL
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()
#=============================================================================================================================================
#=============================================================================Login- b1
def login(text,menu,b1,b2,b3,b4,preview_image):
    switch(b1,b2,b3,b4)
    text.pack_forget()
    preview_image.pack_forget()
    def show_message():
        message=functions.check_credentials(f"{user.get()}",f"{pwd.get()}")
        word=message.split(' ')[0]
        if word=='Login':
            messagebox.showinfo(title="", message=message,icon="info")
            menu.pack_forget()
            form.pack_forget()
            user_menu(message.split(' ')[-1],f"{user.get()}")
        elif word=='No':
            messagebox.showinfo(title="", message=message,icon="info")
        elif word=='Incorrect':
            messagebox.showinfo(title="", message=message,icon="error")
        else:
            messagebox.showinfo(title="", message="Some unknown error occured.",icon="warning")

    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=TOP,fill=Y,pady=140,padx=(0,200))
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
    Button(form,text="Login",width=15,command=show_message,cursor="dotbox").pack(pady=20)
    form.mainloop()
    
#====================================================================== Ceate account -b2
def create(text,b2,b1,b3,b4,preview_image):
    def show_message(u_name,pwd,names):
        u_name=f"{u_name.get()}"
        pwd=f"{pwd.get()}"
        if u_name in names:
            messagebox.showinfo(title="Username Not Available", message="That username is already taken. Try another one.",icon="info")
        else:
            u_id = datetime.datetime.now().strftime("%H%M%S")
            q="insert into user values({},'{}','{}')".format(u_id,u_name,pwd)
            cursor.execute(q)
            mycon.commit()
            msg="Account Created Successfully! ✓\nYour User ID is: {}\n".format(u_id)
            show=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text=msg)
            show.pack(fill=X,pady=35,padx=(0,200))
            messagebox.showinfo(title="Important", message="This User ID is required while deleting the account.",icon="warning")

    switch(b2,b1,b3,b4)
    text.pack_forget()
    preview_image.pack_forget()
    names=[]
    q="select u_name from user"
    cursor.execute(q)
    data=cursor.fetchall()
    for i in data:
        names.append(i[0])

    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=TOP,fill=Y,pady=140,padx=(0,200))
    title=Label(form,font="poppins 10",fg='#ffffff',bg='#171717',text="Create Dataverse Account")
    title.pack(fill=Y,pady=35,padx=0)
    u_name=StringVar()
    pwd=StringVar()
    user_entry=Entry(form,textvariable=u_name,width=30)
    pwd_entry=Entry(form,textvariable=pwd,width=30)
    user_entry.insert(0,'Username')
    pwd_entry.insert(0,'Password')
    user_entry.pack(pady=20,padx=50)
    pwd_entry.pack(pady=20,padx=50)
    Button(form,text="Create Account",width=15,command=partial(show_message,u_name,pwd,names),cursor="dotbox").pack(pady=20)

    form.mainloop()
#====================================================================GUEST
def guest(text,menu,b1,b2,b3,b4,preview_image):
    switch(b1,b2,b3,b4)
    text.pack_forget()
    preview_image.pack_forget()
    menu.pack_forget()
    menu=Frame(root,bg="#171717",relief=SUNKEN)
    menu.pack(side=LEFT,fill=Y)
    text=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text="DATA VISUALISATION SOFTWARE")
    text.pack(fill=X,pady=35,padx=(0,200))

    b1=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Line Graph",width=22,font="poppins 10",cursor="dotbox")
    b2=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Bar Graph",width=22,font="poppins 10",cursor="dotbox")
    b4=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Histogram",width=22,font="poppins 10",cursor="dotbox")
    b3=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Pie Chart",width=22,font="poppins 10",cursor="dotbox")
    b5=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Scatter Plot",width=22,font="poppins 10",cursor="dotbox")
    b6=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Heatmap",width=22,font="poppins 10",cursor="dotbox")
    b7=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Area Chart",width=22,font="poppins 10",cursor="dotbox")
    b8=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Radar Chart",width=22,font="poppins 10",cursor="dotbox")
    b9=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Polar Scatter Plot",width=22,font="poppins 10",cursor="dotbox")
    b10=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Candle Charts",width=22,font="poppins 10",cursor="dotbox")
    b11=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Maps",width=22,font="poppins 10",cursor="dotbox")
    b13=Button(menu,fg='#ffffff',bg='#1a1a1a',text="3d Scatter",width=22,font="poppins 10",cursor="dotbox")
    b14=Button(menu,fg='#ffffff',bg='#1a1a1a',text="3D Surface",width=22,font="poppins 10",cursor="dotbox")
    b12=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Live Graphs",width=22,font="poppins 10",cursor="dotbox")
    b15=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Go to Home",width=22,font="poppins 10",command=main,cursor="dotbox")
    
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
    b15.pack(pady=5,padx=15)
#====================================================================Delete Account- b4
def delete(text,b4,b1,b3,b2,preview_image):
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
    text.pack_forget()
    preview_image.pack_forget()
    names=[]
    q="select u_name from user"
    cursor.execute(q)
    data=cursor.fetchall()
    for i in data:
        names.append(i[0])

    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=TOP,fill=Y,pady=140,padx=(0,200))
    title=Label(form,font="poppins 10",fg='#ffffff',bg='#171717',text="Delete Dataverse Account")
    title.pack(fill=Y,pady=35,padx=0)
    u_name=StringVar()
    u_id=IntVar()
    pwd=StringVar()
    user_entry=Entry(form,textvariable=u_name,width=30)
    user_id=Entry(form,textvariable=u_id,width=30)
    pwd_entry=Entry(form,textvariable=pwd,width=30)
    user_entry.insert(0,'Username')
    user_id.insert(0,'User ID')
    pwd_entry.insert(0,'Password')
    user_entry.pack(pady=20,padx=50)
    user_id.pack(pady=20,padx=50)
    pwd_entry.pack(pady=20,padx=50)
    Button(form,text="Delete Account",width=15,command=partial(show_message,u_name,u_id,pwd,names),cursor="dotbox").pack(pady=20)

    form.mainloop()

#===========================================================================Menu after login
def user_menu(u_id,u_name):
    def view():
        result=functions.view_data(u_id)
        relation=customtkinter.CTkScrollableFrame(root,
                                                  width=900,
                                                  height=500,
                                                  label_text="{}'s Data".format(u_name.title()),
                                                  border_width=1,
                                                  fg_color="#000000",
                                                  scrollbar_button_hover_color="#ffffff"
                                                  )
        relation.pack(side=TOP,fill=Y)
        title=Label(relation,font="Courier 10",fg='#ffffff',bg='#000000',text=result)
        title.grid(row=3,column=2)
        
    menu=Frame(root,bg="#171717",relief=SUNKEN)
    menu.pack(side=LEFT,fill=Y)
    text=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text="PERSONAL FINANCE TRACKER")
    text.pack(fill=X,pady=35,padx=(0,200))

    profile=Frame(root,bg="#171717",relief=SUNKEN,width=25,height=100)
    profile.pack(side=RIGHT,fill=Y,anchor=NE)
    name=Label(profile,font="poppins 15 bold",fg='#ffffff',bg='#171717',text=u_name.title())
    name.pack(fill=X,padx=20,pady=10)

    b1=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Add Data",width=22,font="poppins 10",command=partial(insert,u_id,u_name),cursor="dotbox")
    b2=Button(menu,fg='#ffffff',bg='#1a1a1a',text="View Data",width=22,command=view,font="poppins 10",cursor="dotbox")
    b3=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Visualise Data",width=22,font="poppins 10",command=partial(visualize,u_name),cursor="dotbox")
    b5=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Delete Data",width=22,font="poppins 10",command=partial(delete_data,u_id),cursor="dotbox")
    b4=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Save & Logout",width=22,command=main,font="poppins 10",cursor="dotbox")
    
    b1.pack(pady=(30,5),padx=15)
    b2.pack(pady=5,padx=15)
    b3.pack(pady=5,padx=15)
    b5.pack(pady=5,padx=15)
    b4.pack(pady=5,padx=15)
    b4.config(command=partial(clear,menu,text,profile))

#=========================================================================Visualize data
def visualize(u_name):
    q="select u_id from user where u_name='{}'".format(u_name)
    cursor.execute(q)
    u_id=cursor.fetchall()[0][0]
    requireds=plot.fetch_data(u_id)                             #in progress
    if requireds==None:
            messagebox.showinfo(title="", message="Not enough data to visualize. ✖",icon="warning")
    else:
        values=plot.plot_data(requireds,u_name)
        report="Total Amount= {}\nMax Till Now= {}".format(values[0],values[1])
        text=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text=report)
        text.pack(fill=X,pady=35,padx=(0,200))

def insert(u_id,u_name):
    def show_message():
        ti=str(time.strftime('%y-%m-%d'))
        q="insert into money (u_id,salary,gold,stocks,commodity,sales,expenditure,entryDate) values({},{},{},{},{},{},{},'{}')".format(u_id,variables[0].get(),variables[1].get(),variables[2].get(),variables[3].get(),variables[4].get(),variables[5].get(),ti)
        cursor.execute(q)
        mycon.commit()
        messagebox.showinfo(title="", message="Data added successfully. ✓",icon="info")
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
        value.insert(0,0)
        value.pack(pady=(0,0),padx=50)
    Button(form,text="Add Data",width=15, command=show_message,cursor="dotbox").pack(pady=20)
    form.mainloop()
    
def delete_data(u_id):
    def show(u_id,e_date):
        q="select * from money where u_id=%d and entryDate=%s" %(u_id,e_date)
        cursor.execute(q)
        data=cursor.fetchall()
        if len(data)==0:
            messagebox.showinfo(title="", message="Data not found. ✖",icon="warning")
        else:
            q="delete from money where u_id=%d and entryDate=`%s`" %(u_id,e_date)
            cursor.execute(q)
            mycon.commit()
            messagebox.showinfo(title="", message="Data deleted successfully. ✓",icon="info")
    form=Frame(root,bg="#171717",relief=SUNKEN)
    form.pack(side=TOP,fill=Y,pady=140,padx=(0,200))
    title=Label(form,font="poppins 10",fg='#ffffff',bg='#171717',text="Delete Data")
    title.pack(fill=Y,pady=35,padx=0)
    e_date=StringVar()
    date_entry=Entry(form,textvariable=e_date,width=30)
    date_entry.insert(0,'YYYY-MM-DD')
    date_entry.pack(pady=20,padx=50)
    Button(form,text="Delete Data",width=15,command=partial(show,u_id,e_date),cursor="dotbox").pack(pady=20)

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

#===============================================================GUI
root=Tk()
root.geometry("900x400")
root.title("Dataverse")
root.minsize(600,300)

photo = PhotoImage(file = "/Users/iamte/OneDrive/Desktop/Dataverse/software/images/2dlogo.png")
root.iconphoto(False, photo)
root.configure(bg="black")
top=Frame(root,bg="#1a1a1a",width=100)
title=Label(top,font="Courier 15 bold",fg='#ffffff',bg='#1a1a1a',text="Dataverse")
title.grid(row = 0, column = 1,padx=0,pady=(20,10))
top.pack(side=TOP,fill=X)
image = Image.open("/Users/iamte/OneDrive/Desktop/Dataverse/software/images/3dlogo.png")
resize_image = image.resize((50, 50))
logo = ImageTk.PhotoImage(resize_image)
label = Label(top,bg='#1a1a1a',image = logo)
label.grid(row = 0, column = 0,padx=(15,20),pady=(20,10))

def main():
    text=Label(text="")
    text.pack_forget()
    menu=Frame(root,bg="#171717",relief=SUNKEN)
    menu.pack(side=LEFT,fill=Y)
    text=Label(font="poppins 12",fg='#ffffff',bg='#000000',text='''What does this software do?\n
● This software can be used to visualise data in many forms.
● It allows the user to download the generated charts.
● It can be used as a finance tracker, providing various useful outputs.
● The data can also be stored for later use.''', justify="left", borderwidth=1, relief="sunken",padx=15,pady=15)
    text.pack(pady=40,padx=(40,200),side=TOP,anchor=W)

    image = Image.open("/Users/iamte/OneDrive/Desktop/Dataverse/software/images/preview.png")
    resize_image = image.resize((520, 320))
    preview = ImageTk.PhotoImage(resize_image)
    preview_image=Label(bg='#000000',image = preview, borderwidth=1, relief="solid",padx=15,pady=15)
    preview_image.pack(anchor=W,padx=40,pady=50)

    b1=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Finance Tracker",width=22,font="poppins 10",cursor="dotbox")
    b3=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Data Visualisation",width=22,font="poppins 10",cursor="dotbox")
    b2=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Create Account",width=22,font="poppins 10",cursor="dotbox")
    b4=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Delete Account",width=22,font="poppins 10",cursor="dotbox")
    b1.pack(pady=(30,5),padx=15)
    b3.pack(pady=5,padx=15)
    b2.pack(pady=5,padx=15)
    b4.pack(pady=5,padx=15)

    b1.config(command=partial(login,text,menu,b1,b2,b3,b4,preview_image))
    b3.config(command=partial(guest,text,menu,b3,b1,b4,b2,preview_image))
    b2.config(command=partial(create,text,b2,b1,b3,b4,preview_image))
    b4.config(command=partial(delete,text,b4,b1,b3,b2,preview_image))
    root.mainloop()

main()