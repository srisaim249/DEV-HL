import xlrd
import os.path


book = xlrd.open_workbook("data2.xlsx","rb")

sheets=book.sheet_names()



for sheet_name in sheets:
	sh=book.sheet_by_name(sheet_name)
	
	for rownum in range(sh.nrows):
		row_values=sh.row_values(rownum)

		#row values are lists

		s=" "
		for line in row_values:
			s=s+str(line)+"	  "
		print s
			