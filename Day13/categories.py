import mysql.connector


database=mysql.connector.connect(host='localhost',user='root',password='password',database='COMPANY')

cusor=database.cursor()

file_path="/home/saisri/Desktop/categories.csv"

file_data=open(file_path,"r")

sql_query="INSERT INTO COMPANY_CATEGORIES VALUES (%s,%s,%s)"

file_data.next()

for row in file_data:
	line=row.split(",")
	companyCIN=line[0]
	categories=line[1]
	city_tire=line[2]
	
	data=(companyCIN,categories,city_tire)
	try:
		cusor.execute(sql_query,data)

		database.commit()
	except:
		pass	
		

cusor.close()
database.close()

