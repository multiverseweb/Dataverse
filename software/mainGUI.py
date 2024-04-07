from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from functools import partial
import functions
import customtkinter
import plot
import mysql.connector as my   
#========================================================================================================================================connecting mySQL
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()
#==========================================================================================================================================================

def login(text,menu,b1,preview_image):
    switch(b1)
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
    Button(form,text="Submit",width=15,command=show_message).pack(pady=20)
    form.mainloop()
    
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

    b1=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Add Data",width=22,font="poppins 10")
    b2=Button(menu,fg='#ffffff',bg='#1a1a1a',text="View Data",width=22,command=view,font="poppins 10")
    b3=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Visualise Data",width=22,font="poppins 10",command=partial(visualize,u_name))
    b4=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Save & Logout",width=22,command=lambda: [main(), clear(menu,text,profile)],font="poppins 10")
    
    b1.pack(pady=(30,5),padx=15)
    b2.pack(pady=5,padx=15)
    b3.pack(pady=5,padx=15)
    b4.pack(pady=5,padx=15)
    b4.config(command=partial(clear,menu,text,profile))

def visualize(u_name):
    q="select u_id from user where u_name='{}'".format(u_name)
    cursor.execute(q)
    u_id=cursor.fetchall()[0][0]
    requireds=plot.fetch_data(u_id)                             #in progress
    if requireds==None:
            messagebox.showinfo(title="", message="Not enough data to visualize.",icon="warning")
    else:
        values=plot.plot_data(requireds,u_name)
        report="Total Amount= {}\nMax Till Now= {}".format(values[0],values[1])
        text=Label(font="poppins 10 bold",fg='#ffffff',bg='#000000',text=report)
        text.pack(fill=X,pady=35,padx=(0,200))
def clear(menu,text,profile):
    menu.pack_forget()
    text.pack_forget()
    profile.pack_forget()
    main()

def switch(b):
    b["state"] = DISABLED
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

    b1=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Login",width=22,font="poppins 10")
    b2=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Create Account",width=22,font="poppins 10")
    b3=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Continue as Guest",width=22,font="poppins 10")
    b4=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Delete Account",width=22,font="poppins 10")
    b5=Button(menu,fg='#ffffff',bg='#1a1a1a',text="Login as Admin",width=22,font="poppins 10")
    b1.pack(pady=(30,5),padx=15)
    b2.pack(pady=5,padx=15)
    b3.pack(pady=5,padx=15)
    b4.pack(pady=5,padx=15)
    b5.pack(pady=5,padx=15)

    b1.config(command=partial(login,text,menu,b1,preview_image))
    root.mainloop()

main()