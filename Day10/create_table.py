import mysql.connector


db =mysql.connector.connect(host="localhost",user="root",password="password")

curs = db.cursor()

curs.execute("DROP DATABASE IF EXISTS user_info")
curs.execute("CREATE DATABASE  user_info")
curs.execute("USE  user_info")

curs.execute("CREATE TABLE  user_profile(id INT PRIMARY KEY,first_name VARCHAR(30),last_name VARCHAR(30),gender VARCHAR(30))")

curs.close()

db.close()