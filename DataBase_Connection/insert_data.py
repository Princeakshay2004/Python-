import mysql.connector as conn
import create_connection



# To Insert data
Cursorobj=create_connection.Database.cursor()
Cursorobj.execute("insert into Emp(Roll,Ename) values(%s,%s)",(10,"Akshay"))
create_connection.Database.commit()
print("Record Inserted")


# To insert Multipal Records
sql="Insert into Emp(Roll,Ename) values(%s,%s)"
values=[(15,"Akshay"),
        (11,"BAchate"),
        (12,"Jivan"),
        (13,"Sudarshan")]
Cursorobj.executemany(sql,values)
create_connection.Database.commit()

print("Multipal Records Inserted")
