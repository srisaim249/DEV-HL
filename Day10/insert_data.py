import mysql.connector

db =mysql.connector.connect(host="localhost",user="root",password="password")

curs = db.cursor()


data="USE user_info";

curs.execute(data)

curs.execute("INSERT INTO user_profile VALUES (1,'JOHN','BOB','MALE')")
curs.execute("INSERT INTO user_profile VALUES (2,'RAGHU','RATHAN','MALE')")
curs.execute("INSERT INTO user_profile VALUES (3,'RANI','RAGHAVI','MALE')")

db.commit()

curs.execute("INSERT INTO user_profile VALUES (4,'RICHI','RATHAN','MALE'),(5,'BOB','RAHUL','MALE'),(6,'NAVYA','BHAVYA','FEMALE')")

db.commit()


curs.close()

db.close()