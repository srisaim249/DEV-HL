import xlrd
import os.path



file_path="/home/saisri/Desktop/file_for_xlsx.xlsx"

book = xlrd.open_workbook(file_path,"rb")

sheets=book.sheet_names()


dictionary={}



for sheet_name in sheets:
	sh=book.sheet_by_name(sheet_name)
	for rownum in range(sh.nrows):
		
		row_values=sh.row_values(rownum)
		val=row_values[0]

		if val not in dictionary:
			dictionary[val]=row_values

print dictionary