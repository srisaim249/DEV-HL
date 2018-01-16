import sys
import os
import csv

file_path=sys.argv[1]

name=sys.argv[2]

file_pointer=open(file_path,"r")

if not os.path.isfile(file_path):
	print("Sorry , file doesnt exists")
	exit(12)


lists=[]	
record1=dict()
count=0

for line in file_pointer:	
	#print(type(line))	
	val=line.split(",")
	user_id=val[0]
	first_name = val[1]
	last_name=val[2]
	email=val[3]

	if(first_name==name):
		if user_id not in record1:
			print user_id
			count+=1
			print "count is ",count
			record1[user_id]=line
			print record1[user_id]

	elif(last_name==name):
		if user_id not in record1:
			print user_id
			count+=1
			print "count is ",count
			record1[user_id]=line
			print record1[user_id]


	elif(email==name):
		if user_id not in record1:
			print user_id
			count+=1
			print "count is ",count
			record1[user_id]=line
			print record1[user_id]

	elif(user_id==name):
		count+=1
		
		if(count<=1):
			print line
			
	