import mysql.connector
import xlrd


book=xlrd.open_workbook("/home/saisri/Desktop/clientdetails.xlsx","rb")

sheets=book.sheet_by_index(0)


db=mysql.connector.connect(host="localhost",user="root",password="password",database="user_info")

curs=db.cursor()


curs.execute("CREATE TABLE xl_data(ids INT ,first_name VARCHAR(30),last_name VARCHAR(30),email VARCHAR(40),gender varchar(30),ipaddress varchar(30))")


for row in range(1,sheets.nrows):
	ids=sheets.cell(row,0).value

	first_name=sheets.cell(row,1).value
	last_name=sheets.cell(row,2).value
	email=sheets.cell(row,3).value
	gender=sheets.cell(row,4).value
	ipaddress=sheets.cell(row,5).value
	
	data=(ids,first_name,last_name,email,gender,ipaddress)
	
	print data


	curs.execute("INSERT  INTO xl_data(ids,first_name,last_name,email,gender,ipaddress) VALUES (%s,%s,%s,%s,%s,%s)",data)
	db.commit()			


curs.close()
db.close()
			
	