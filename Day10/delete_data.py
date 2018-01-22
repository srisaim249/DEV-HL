import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="password",database="user_info")

curs=db.cursor()

curs.execute("USE user_info")
curs.execute("DELETE FROM user_profile WHERE ID=5")
db.commit()

curs.close()
db.close()


