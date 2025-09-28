import mysql.connector as conn
import create_connection 


# Step 3 : To Create Table
Cursorobj=create_connection.Database.cursor()
Cursorobj.execute("create table Emp(Roll int,Ename varchar(20))")
print("Table Created ")

