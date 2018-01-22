import xlrd
import os.path
import sys
import xlwt


argument1=sys.argv[1]
argument2=sys.argv[2]

rowx=argument1.split(",")[0]
colx=argument1.split(",")[1]

rowspawn=int(argument1.split(",")[2])
colspawn=int(argument1.split(",")[3])

rowspawn+=1
colspawn+=1

file_row=argument2.split(",")[0]
file_col=argument2.split(",")[1]

file_rowspawn=int(argument2.split(",")[2])
file_colspawn=int(argument2.split(",")[3])

file_rowspawn+=1
file_colspawn+=1



s1=[]

# data reading from file1

file_path="data1.xlsx"
book = xlrd.open_workbook(file_path,"rb")

sheets=book.sheet_by_index(0)

filepath = "/home/saisri/Desktop/new_file.xlsx"


workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')


for rows in range(int(rowx),int(rowspawn)):	

	row_values=sheets.row_values(rows)	
	for cols in range(int(colx),int(colspawn)):
		
		s1.append(str(row_values[cols]))

print s1



i=0

for row in range(int(file_row)-1,int(file_rowspawn)-1):
	for col in range(int(file_col)-1,int(file_colspawn)-1):
		
		if(i>=(len(s1))):
			break
								
		else:
			sheet.write(row,col,s1[i])
			i+=1

		
workbook.save(filepath)