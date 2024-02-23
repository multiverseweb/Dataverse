def add_data():                                                                    #add data
    n=int(input("No. of points: "))
    for i in range(n):
        print("\nx",i+1,":")
        x=int(input())
        print("y",i+1,":")
        y=int(input())
        q="insert into points values({},{})".format(x,y)
        cursor.execute(q)
        mycon.commit()
