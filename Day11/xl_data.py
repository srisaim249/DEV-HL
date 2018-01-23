import psycopg2 
import xlrd


book=xlrd.open_workbook("/home/saisri/Desktop/clientdetails.xlsx","rb")

sheets=book.sheet_by_index(0)


db=psycopg2.connect(host="localhost",user="postgres",password="test123",database="postgres")

curs=db.cursor()


curs.execute("create table xl_data(ids integer ,first_name varchar(30),last_name varchar(30),email varchar(40),gender varchar(30),ipaddress varchar(30))")


for row in range(1,sheets.nrows):
	ids=sheets.cell(row,0).value

	first_name=sheets.cell(row,1).value
	last_name=sheets.cell(row,2).value
	email=sheets.cell(row,3).value
	gender=sheets.cell(row,4).value
	ipaddress=sheets.cell(row,5).value
	
	data=(ids,first_name,last_name,email,gender,ipaddress)
	
	print data


	curs.execute("insert into xl_data(ids,first_name,last_name,email,gender,ipaddress) values (%s,%s,%s,%s,%s,%s)",data)
	db.commit()			


curs.close()
db.close()
			
	