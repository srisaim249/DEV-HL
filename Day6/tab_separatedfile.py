import csv

file_argument=open("NEWCSVFILE.csv","r")

outputfile = open('withoutduplicate.csv', 'w')

for row in file_argument:
	outputfile.write(row.replace(",","	"))



