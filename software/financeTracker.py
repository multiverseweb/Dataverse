import tabulate
#==================================================================================================connecting mySQL
import mysql.connector as my                                    #required modules
mycon=my.connect(host='localhost',user='root',passwd='tejas123',database='finance')
cursor=mycon.cursor()
#=========================================================================================view data
def view_data(u_id):
    q="select * from money where u_id={}".format(u_id)
    cursor.execute(q)
    data=cursor.fetchall()
    if len(data)==0:
        result="Your dataSet is empty."
    else:
        columns = [col[0] for col in cursor.description]
        table = tabulate.tabulate(data, headers=columns, tablefmt="pretty")
        result=table
    return result

#==================================================================================================add data
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
