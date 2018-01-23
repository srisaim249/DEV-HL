import xlrd
import mysql.connector

file_path = "/home/saisri/Desktop/duplicated_data.xlsx"
book = xlrd.open_workbook(file_path,'rb')

sheet= book.sheet_by_index(0)

con = mysql.connector.connect(user= 'root', password='password', host='localhost', database= 'user_info')

cursor = con.cursor()

cursor.execute("CREATE TABLE xl_data(Id INT PRIMARY KEY, first_name VARCHAR(20), last_name VARCHAR(20), email VARCHAR(40), gender VARCHAR(8))")

sql="INSERT IGNORE INTO xl_data(Id,first_name,last_name,email,gender) VALUES (%s, %s, %s, %s, %s)"

for row in range (1,sheet.nrows):
	Id =sheet.cell(row,0).value 
	first_name = sheet.cell(row,1).value
	last_name = sheet.cell(row,2).value
	email = sheet.cell(row,3).value
	gender = sheet.cell(row,4).value

	values = (Id,first_name,last_name,email,gender)
	cursor.execute(sql,values)

con.commit()
cursor.close()
con.close()


