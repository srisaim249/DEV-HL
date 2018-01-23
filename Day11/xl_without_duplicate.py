import xlrd
import psycopg2 

book=xlrd.open_workbook("/home/saisri/Desktop/duplicated_data.xlsx","rb")

sheets=book.sheet_by_index(0)

db=psycopg2.connect(host="localhost",user="postgres",password="test123",database="postgres")

cursor=db.cursor()

cursor.execute("create table xlfile(ids INTEGER PRIMARY KEY,first_name varchar(30),last_name varchar(30),email varchar(40),gender varchar(30))")

sql_query="insert  into xlfile (ids,first_name,last_name,email,gender) values (%s,%s,%s,%s,%s)"

for row in range(1,sheets.nrows):
	ids=sheets.cell(row,0).value

	first_name=sheets.cell(row,1).value
	last_name=sheets.cell(row,2).value
	email=sheets.cell(row,3).value
	gender=sheets.cell(row,4).value
	
	data=(ids,first_name,last_name,email,gender)
	
	print data
	try:
		cursor.execute(sql_query,data)
	except:
		pass
	
	db.commit()			


cursor.close()
db.close()
			
	