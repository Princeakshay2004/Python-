import mysql.connector as conn

# Step 1 :To create Connection
Database=conn.connect(
    host="localhost",
    user="root",
    password="akshay"
)
print(Database)


# step 2 : To Create Database   ( This Used for only create Database or Schema )
Cursorobj=Database.cursor()
Cursorobj.execute("CREATE DATABASE Demo")
print("Database Created !!")


