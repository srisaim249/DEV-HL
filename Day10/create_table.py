import mysql.connector

db =mysql.connector.connect(host='localhost',user='root',password="password",db="user_details")

curs = db.cursor()

mysql="CREATE TABLE user_data1(id int primary key,first_name varchar(30),last_name varchar(30),gender varchar(30))";


curs.execute(mysql);

data="DESCRIBE user_data1";


print curs.execute(data)

