file = open('big.txt','r')

total_data= {}

for line in file:
	word_list = line.split()
	for word in word_list:
	word = word.lower()
	if word not in total_data:
	totalwords[word] = 1
	else:
	totalwords[word] += 1
 
for data1,data2 in totalwords.items():
 print (data1,data2)

print(len(totalwords))
