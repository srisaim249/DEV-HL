import mysql.connector

database=mysql.connector.connect(host='localhost',user='root',password='password',database='user_data')

cusor=database.cursor()

cusor.execute("CREATE TABLE USER(userid INT PRIMARY KEY ,first_name VARCHAR(40) UNIQUE,last_name VARCHAR(40),email VARCHAR(40) UNIQUE)")

cusor.execute("CREATE TABLE APPLICATION(applicationid INT PRIMARY KEY ,userid INT,age INT ,address1 VARCHAR(40),address2 VARCHAR(40),salary VARCHAR(30),company_name VARCHAR(30),FOREIGN KEY (userid) REFERENCES USER (userid))")





