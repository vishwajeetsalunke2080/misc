import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mia@4722",
    database="Sakila"
)
mycursor = mydb.cursor()
mycursor.execute("select * tables")
data = mycursor.fetchall()
print(data)