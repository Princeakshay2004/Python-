import mysql.connector as conn
import create_connection 

cursor_obj=create_connection.Database.cursor()

#To select data
cursor_obj.execute("select * from Emp")
results=cursor_obj.fetchall()

for i in results:
    print(i)