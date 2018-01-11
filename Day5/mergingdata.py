
file1= open("data1.csv")
file2 =open("data2.csv")
file3="data3.csv"

file3_write=open(file3,"w")

record1=dict()
record2  = dict()


file2.next()
file2.next()

for line1 in file1:
	row = line1.split(",")
	id1 = row[0]
	if id1 not in record1:
		record1[id1]=row


for line2 in file2:
	row2 = line2.split(",")
	id2 = row2[0]
	if id2 not in record2:
		record2[id2]=row2

for id1 in record1:
	if id1 in record2:
		(record1[id1].extend(record2[id1][1:]))
	
file3_write.write("%s"%record1)