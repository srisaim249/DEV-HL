import sys
import os.path
import csv

file_path=sys.argv[1]

name=sys.argv[2]

if not  os.path.isfile(file_path):
	print("Sorry , file doesnt exists")
	exit(12)

file_pointer=open(file_path)

csv_reader = csv.DictReader(file_pointer)



list1=[]
	
count=0

for line in csv_reader:
	
	if(line['first_name']==name):
		if line['id'] not in list1:
			count+=1
			print line
			print "the count is ",count

	elif(line['last_name']==name):
		if line['id'] not in list1:
			count+=1
			print line
			print "the count is ",count

	elif(line['id']==name):
		if line['id'] not in list1:
			count+=1
			print line
			print "the count is ",count

	elif(line['email']==name):
		if line['id'] not in list1:
			count+=1
			print line
			print "the count is ",count
	