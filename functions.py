import mysql.connector as my                                    #required modules
import matplotlib.pyplot as plt 
import numpy as np
import time
import datetime
from datetime import datetime
import getpass
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
        print("Your dataSet is empty.")
    else:
        cursor.execute("DESCRIBE money")
# Get the schema of the table
        schema = cursor.fetchall()
        print(19*9*"-",end="")
        print("+")
        print("\r| ",end="")
        for column in schema:
            print((15-len(str(column[0])))*" ",column[0],end=" | ")
        print("\r")
        print(19*9*"-",end="")
        print("+")
        for i in data:
            print("| ",end="")
            for j in i:
                print((15-len(str(j)))*" ",j,end=" | ")
            print("\r")
        print(19*9*"-",end="")
        print("+")
