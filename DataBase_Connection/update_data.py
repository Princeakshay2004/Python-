import mysql.connector as conn
import create_connection

cursor_obj=create_connection.Database.cursor()

# To update Data
cursor_obj.execute("update Emp set Roll=%s where Ename=%s",(405,"Akshay"))
create_connection.Database.commit()


cursor_obj.execute("select * from Emp where roll=405")
results=cursor_obj.fetchall()
for i in results:
    print(i)