import mysql.connector as my                                    #required modules
import matplotlib.pyplot as plt 
import time
import datetime
import getpass
#========================================================================================================connecting mySQL
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user (u_id INT PRIMARY KEY, u_name VARCHAR(255), pwd VARCHAR(255))")
#===========================================================================================================add data
def add_data():
    n=int(input("No. of points: "))
    for i in range(n):
        print("\nx",i+1,":")
        x=int(input())
        print("y",i+1,":")
        y=int(input())
        q="insert into points values({},{})".format(x,y)
        cursor.execute(q)
        mycon.commit()
#===========================================================================================================view data
def view_data():
    x=[]
    y=[]
    q="select * from points"
    cursor.execute(q)
    data=cursor.fetchall()
    for i in data:
        x.append(i[0])
        y.append(i[1])
    print(9*"-","+",9*"-",sep="")
    print("| x \t |\ty |",sep="")
    print(9*"-","+",9*"-",sep="")
    for i in range(len(x)):
        print("|",x[i],7*"_","|",7*"_",y[i],"|",sep="")
    print(9*"-","+",9*"-",sep="")
#==============================================================================================================plot data
def plot_data():
    plt.style.use('dark_background')
    x=[]
    y=[]
    q="select * from points"
    cursor.execute(q)
    data=cursor.fetchall()
    for i in data:
        x.append(i[0])
        y.append(i[1])
    fig = plt.figure(figsize=(12, 9))
    plt.plot(x,y,color="teal")
    plt.scatter(x,y,color="yellow",marker="*")
    plt.title("XY - Plot", fontsize=15, fontname="Monospace")
    plt.xlabel("x points")
    plt.ylabel("y points")
    plt.tight_layout()
    plt.show()
#==================================================================================================================Account operations
def main_menu():
    ch=1
    while ch!=0:
        print(100*"=","\n",48*" ","MENU\n",100*"=","\n","1. Add Data\n2. View Data\n3. Visualise Data\n4. Save & Logout",sep="")
        ch=int(input("Enter your choice: "))
        if ch==1:
            add_data()
        elif ch==2:
            view_data()
        elif ch==3:
            plot_data()
        elif ch==4:
            print("Data saved successfully. ✓")
            break
        else:
            print("Invalid Choice. ✖")
#==========================================================================================================for guest
def guest_plot():
    plt.style.use('dark_background')
    print("\tMENU\n1. Bar Graph\n2. Histogram\n3. Scatter Plot\n4. Line Chart\n5. Pie Chart\n6. 3d Scatter\n7. 3d Surface\n8. All")
    c=int(input("Enter your choice: "))
    n=int(input("\nEnter the number of observations: "))
    x = []
    y = []
    for i in range(n):
        print("Enter x{}: ".format(i+1),end="")
        a=float(input())
        x.append(a)
        print("Enter y{}: ".format(i+1),end="")
        b=float(input())
        y.append(b)
    if c==1:
        plt.bar(x,y, color='yellow') 
    elif c==2:
        plt.hist(x,y, color='yellow') 
    elif c==3:
        plt.scatter(x,y, c='yellow') 
    elif c==4:
        plt.plot(x,y, c='yellow') 
    else:
        plt.bar(x,y, color='yellow',alpha=0.6) 
        plt.hist(x,y, color='blue',alpha=0.6) 
        plt.scatter(x,y, c='green',alpha=0.6) 
        plt.plot(x,y, c='red',alpha=0.6) 
    plt.show()
            
#=========================================================================================================Start
#==============================================================================================================
while True: 
    print(201*"=")
    greet="PERSONAL FINANCE TRACKER & DATA VISUALIZTAION SOFTWARE"
    print(70*" ",greet)
    print(201*"=","\n","1. Login\n2. Create Account\n3. Continue as Guest\n4. Exit",sep="")                #Login Menu
    user_type=int(input("Enter your choice: "))

#==========================================================================================================Login
    if user_type==1:
        print(83*" ","𝗣𝗲𝗿𝘀𝗼𝗻𝗮𝗹 𝗙𝗶𝗻𝗮𝗻𝗰𝗲 𝗧𝗿𝗮𝗰𝗸𝗲𝗿")
        u_name=input("Username: ")
        q="select u_name from user "
        cursor.execute(q)
        data=cursor.fetchall()
        names=[]
        for i in data:
            names.append(i[0])
        if u_name not in names:
            print("No account exists with that username.")
        else:
            try:
                pwd = getpass.getpass()
            except Exception as error:
                print('There was some error: ', error)
            else:
                q="select pwd from user where u_name='{}'".format(u_name)
                cursor.execute(q)
                data=cursor.fetchall()
                if data[0][0]==pwd:
                    print("Login Successful.")
                    main_menu()
                else:
                    print("Incorrect password! ✖")
#=========================================================================================================Create Account
    elif user_type==2:
        print(83*" ","𝗣𝗲𝗿𝘀𝗼𝗻𝗮𝗹 𝗙𝗶𝗻𝗮𝗻𝗰𝗲 𝗧𝗿𝗮𝗰𝗸𝗲𝗿")
        ok=False
        q="select u_name from user"
        cursor.execute(q)
        data=cursor.fetchall()
        while ok!=True:                                                  #set up in mySQL before running
            u_name=input("Username: ")
            for i in data:
                ok=True
                if i[0]==u_name:
                    ok=False
                    print("An account exists with the same username. Try another one.")
                    break
        pwd=input("Password: ")
        u_id = datetime.datetime.now().strftime("%H%M%S")
        q="insert into user values({},'{}','{}')".format(u_id,u_name,pwd)
        cursor.execute(q)
        mycon.commit()
        print("Account Created Successfully! ✓")
        print("Your User ID is: ",u_id)
#==========================================================================================================Guest
    elif user_type==3:
        print(81*" ","𝗗𝗮𝘁𝗮 𝗩𝗶𝘀𝘂𝗮𝗹𝗶𝘇𝗮𝘁𝗶𝗼𝗻 𝗦𝗼𝗳𝘁𝘄𝗮𝗿𝗲")
        guest_plot()
#==========================================================================================================Exit
    elif user_type==4:
        print(201*"=")
        print("Made with <3 Tejas :)")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".",end="\n")
        print(201*"=")
        break
    else:
        print("Invalid choice! ✖")