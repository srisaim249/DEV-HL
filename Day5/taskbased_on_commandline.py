import sys
import os
import csv

file_argument=sys.argv[1]

name=sys.argv[2]



file=open(file_argument,'r')

"""if not os.path.isfile(file):
	print("Sorry , file doesnt exists")
	exit()
"""


record1={}
	
count=0


for line in file:	
	
	
	
	val=line.split(",")
	#print val
	
	user_id=val[0]
	#print user_id
	
	first_name = val[1]
	#print first_name
	
	if first_name  is name:
		print name
		print first_name
	
		print user_id
	
		if user_id not in record1:
			count+=1
			
			record1[user_id]=line
			
			print record1[user_id]
			
			break
print "count is ",count