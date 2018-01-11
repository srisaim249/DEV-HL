
file1= open("data1.csv")
file2 =open("data2.csv")
file3=open("data3.csv","w")

record1=dict()

list1=[]

for line1 in file1:
	row = line1.split(",")
	id1 = row[0]
	
	if id1 not in record1:
		record1[id1]=row
	
	for line2 in file2:
		row2 = line2.split(",")
		id2 = row2[0]

		if id2  in record1[id1]:
		
		
		 
		 if len(record1[id1])==5:
		  
		  
 		  record1[id1].extend(row2[1:])
 		  list1=record1[id1]
 		  
 		  
 		 
 		  
		  
		  file3.write("%s\t"%list1[0])
		  file3.write("%s\t"%list1[1])
		  file3.write("%s\t"%list1[2])
		  file3.write("%s\t"%list1[3])
		  file3.write("%s\t"%list1[4].rstrip("\n"))
		  file3.write("%s\t"%list1[5])
		  file3.write("%s"%list1[6])#file3.write("%s\n"%list_of_records[7])


		 

		  break
		break 
		

