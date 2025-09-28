import mysql.connector as conn


# To create Connection
Database=conn.connect(
    host="localhost",
    user="root",
    password="akshay",
    database="Demo"
)
print(Database)
print("Connection Created !!")



