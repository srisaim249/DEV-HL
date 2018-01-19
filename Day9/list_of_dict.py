import xlrd
import os.path
import sys

argument1=sys.argv[1]

rowx=argument1.split(",")[0]
colx=argument1.split(",")[1]

rowspawn=int(sys.argv[2])
colspawn=int(sys.argv[3])

rowspawn+=1
colspawn+=1

dict_list = []
dictionary = {}

s=""

file_path="data1.xlsx"

book = xlrd.open_workbook(file_path,"rb")

sheets=book.sheet_by_index(0)

dic_keys= [sheets.cell(0, col_index).value for col_index in range(sheets.ncols)]




for rows in range(int(rowx),int(rowspawn)):
	for cols in range(int(colx),int(colspawn)):
		dictionary[dic_keys[cols]] = sheets.cell(rows, cols).value
	
	
	dict_list.append(dictionary.copy())
print dict_list	