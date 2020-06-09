import mysql.connector
#db=  MySQLdb.connect("localhost","grocery_app_db","grocery_app_db","grocery_app_db")

cnx = mysql.connector.connect(user='grocery_app_db', 
        password='grocery_app_db', host='localhost',
                              port='3306', database='grocery_app_db')
