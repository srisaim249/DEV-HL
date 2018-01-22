import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="password",database="user_info")

curs=db.cursor()

curs.execute("USE user_info")
curs.execute("UPDATE  user_profile SET first_name='ROBERT' WHERE id=3",)
curs.execute("UPDATE  user_profile SET id=5 WHERE id=6",)


db.commit()

curs.close()
db.close()