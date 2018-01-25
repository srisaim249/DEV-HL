import mysql.connector


database=mysql.connector.connect(host='localhost',user='root',password='password',database='COMPANY')

cusor=database.cursor()

file_path="/home/saisri/Desktop/company_details.csv"

file_data=open(file_path,"r")

sql_query="INSERT INTO COMPANY_DETAILS VALUES (%s,%s,%s,%s)"

file_data.next()

for row in file_data:
	line=row.split(",")
	companyCIN=line[0]
	company_name=line[1]
	location=line[2]
	pin=line[3]
	data=(companyCIN,company_name,location,pin)
	try:
		cusor.execute(sql_query,data)

		database.commit()
	except:
		pass	
		

cusor.close()
database.close()

