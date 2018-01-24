import mysql.connector
import readline


database=mysql.connector.connect(host='localhost',user='root',password='password',database='user_data')

cusor=database.cursor()

applicationid=raw_input("enter your applicationid ")

userid=raw_input("enter your userid ")

first_name=raw_input("enter your first_name ")

last_name=raw_input("enter your last_name ")

email=raw_input("enter your email ")

age=raw_input("enter your age ")

address1=raw_input("enter your address1 ")

address2=raw_input("enter your address2 ")

salary=raw_input("enter your salary ")

company_name=raw_input("enter your company_name ")


data=(applicationid,userid,age,address1,address2,salary,company_name)
	
data1=(userid,first_name,last_name,email)

query1="INSERT INTO USER VALUES (%s,%s,%s,%s)"

query=("INSERT INTO APPLICATION(applicationid,userid,age,address1,address2,salary,company_name) VALUES (%s,%s,%s,%s,%s,%s,%s)")


question=raw_input("do you want to save the data (yes/no): ")


if(question=="yes"):
	cusor.execute(query1,data1)
	cusor.execute(query,data)
	database.commit()
	print "your data is saved"

else:
	print "your data is not saved"
				
cusor.close()
database.close()