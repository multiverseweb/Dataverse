import mysql.connector as my                                    #required modules
import time
from tabulate import tabulate

z=0                 #failed login attempts
#==================================================================================================connecting mySQL
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()
#==================================================================================================add data
def add_data(u_id):
    print("CURRENT DATA")
    view_data(u_id)

    print("Enter the data: ")
    new_data=[]
    cursor.execute("DESCRIBE money")
# Get the schema of the table
    schema = cursor.fetchall()
    for i in range(1,7):
        print(schema[i][0],end=": ")
        new_data.append(input(""))
    print("\n")
    ti=str(time.strftime('%y-%m-%d'))
    q="insert into money (u_id,salary,gold,stocks,commodity,sales,expenditure,entryDate) values({},{},{},{},{},{},{},'{}')".format(u_id,new_data[0],new_data[1],new_data[2],new_data[3],new_data[4],new_data[5],ti)
    cursor.execute(q)
    mycon.commit()

    print("Data added successfully. ✓")
    print("UPDATED DATA")
    view_data(u_id)

#=========================================================================================view data
def view_data(u_id):
    q="select * from money where u_id={}".format(u_id)
    cursor.execute(q)
    data=cursor.fetchall()
    if len(data)==0:
        result="Your dataSet is empty."
    else:
        columns = [col[0] for col in cursor.description]
        table = tabulate(data, headers=columns, tablefmt="pretty")
        result=table
    return result

def check_credentials(u_name,pwd):
    q="select u_name from user"
    cursor.execute(q)
    data=cursor.fetchall()
    names=[]
    for i in data:
        names.append(i[0])
    if str(u_name) not in names:
        message="No account exists with that username."
    else:
        q="select pwd from user where u_name='{}'".format(u_name)
        cursor.execute(q)
        data=cursor.fetchall()
        if data[0][0]==pwd:
            q="select u_id from user where u_name='{}'".format(u_name)
            cursor.execute(q)
            u_id=cursor.fetchall()[0][0]
            message="Login Successful. ✓\nUser ID: {}".format(u_id)
        else:
            message="Incorrect password! ✖"
            global z
            z+=1
            if z>=2:
                print("There have been more than 1 failed login attempts. Closing the system.")
    return message