import mysql.connector as conn
import create_connection

# To Delete Data

cursor_obj=create_connection.Database.cursor()
query=("DELETE FROM Emp WHERE Ename=%s")
values=("Akshay",)
cursor_obj.execute(query,values)
create_connection.Database.commit()

#To show data
cursor_obj.execute("select * from Emp")
results = cursor_obj.fetchall()
for i in results:
     print(i)
