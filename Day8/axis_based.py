import xlrd
import os.path
import sys


file_path="/home/saisri/Desktop/clientdetails.xlsx"

book = xlrd.open_workbook(file_path,"rb")


sheets=book.sheet_by_index(0)


argument1=sys.argv[1]

row1=argument1.split(",")[0]
col1=argument1.split(",")[1]

row2=int(sys.argv[2])
col2=int(sys.argv[3])

if(col2<col1 or row2<row1):
	print("please enter columns properly")
	exit(2345)

row2+=1
col2+=1


file_path="/home/saisri/Desktop/clientdetails.xlsx"

book = xlrd.open_workbook(file_path,"rb")


sheets=book.sheet_by_index(0)


for row in range(int(row1),int(row2)):

	for cols in range(int(col1),int(col2)):
		row_values=sheets.row_values(row)

		print row_values
		
