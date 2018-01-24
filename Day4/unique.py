file = open('/home/saisri/Desktop/DEV-HL/Day3/message.txt','r')

totalwords = []

for line in file:
	word_list = line.split()
	for word in word_list:
		word = word.lower()
		totalwords=word
		print totalwords
		count=0
		if word not in totalwords:
	 	 count = 1
	 	 totalwords.append(word+"\t")
	 	 totalwords.append(count)
		else:
	 		count += 1

			totalwords.append(word+"\t")
			totalwords.append(count)	 
 
print((totalwords))
