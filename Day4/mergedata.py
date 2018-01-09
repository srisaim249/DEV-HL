import csv

firstfile =open("data1.csv","r")
secondfile=open("data2.csv","r")

thirdfile=open('withoutduplicates.csv', 'w')




global user_id

for line in firstfile:
	words_list_one = line.split(",")
	user_id = words_list_one[0]
	
	for line2 in secondfile:
		words_list_two=line2.split(",")
		user_id2 = words_list_two[0]
		if user_id == user_id2:
	 	 print words_list_two
	 	 thirdfile.write("%s\t" %(words_list_one[0]))
	 	 thirdfile.write("%s\t" %(words_list_one[1]))
	 	 thirdfile.write("%s\t" %(words_list_one[2]))
	 	 thirdfile.write("%s\t\t" %(words_list_one[3]))

	 	 thirdfile.write("%s\t" %(words_list_two[1]))
	 	 thirdfile.write("%s" %(words_list_two[2]))
	 	 break	 	 
		break



  