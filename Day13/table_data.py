import mysql.connector


database=mysql.connector.connect(host='localhost',user='root',password='password',database='COMPANY')

cusor=database.cursor()



sql_query="INSERT INTO CATEGORY_DETAILS VALUES (%s,%s,%s)"

cusor.execute("SELECT * FROM COMPANY_CATEGORIES")
row = cusor.fetchall()

for line in row:
	try:
		print line[0],line[1],line[2]
		cusor.execute(sql_query,(line[0],line[1],line[2]))
		database.commit()
	except:
		pass	


cusor.close()
database.close()

