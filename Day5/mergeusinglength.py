
file1= open("data1.csv")
file2 =open("data2.csv")


record1=dict()



file1.next()
file2.next()

for line1 in file1:
	row = line1.split(",")
	id1 = row[0]
	
	if id1 not in record1:
		record1[id1]=row
	
	for line2 in file2:
		row2 = line2.split(",")
		id2 = row2[0]

		if id2  in record1[id1]:
		
		 print id2
		 
		 if len(record1[id1])==5:
		  
		  print record1[id1]
 		 
 		  record1[id1].extend(row2[1:])
		  print record1[id1]

		  break
		break 
		

