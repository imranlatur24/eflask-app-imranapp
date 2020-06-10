import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  db="chat_db"
)
mycursor = mydb.cursor()

sql =("INSERT INTO customers(email) VALUES (%s)")
val = ("John@gmail.com",)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
print("connected db:")
