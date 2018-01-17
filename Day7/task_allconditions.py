import csv
import os
import sys

if(len(sys.argv)==1):
	print("Hai you didn't give any file or condition  here")
	print("example file is samplefile.txt and the condition is  name=abc")	
	exit(11233)

elif(len(sys.argv)==2):
	print("Hai you didn't give any condition here")
	print("example condition is name=abc")	
	exit(1111)


file_path=sys.argv[1]
condition=sys.argv[2]

if not os.path.isfile(file_path):
	print("Sorry , file doesnt exists")
	exit(12)

file_argument=csv.DictReader(open(file_path))	


def unique(condition):
	
	data={}
	
	c=0

	header=condition.split("=")[0]
	value=condition.split("=")[1]

	for line in file_argument:
		if(line.has_key(header)):
			if(line[header]==value):
				if line['id'] not in data:
					c+=1
					data[line['id']]=line
		
		else:
			print "the header :",header,"is not present in your data"
			break

	print data
	print "the count is ",c		
	



unique(condition)
