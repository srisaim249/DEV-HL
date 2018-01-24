fileread=open("big.txt","r")

data=set()

data_unique={}

for line in fileread:
	unique_words=line.split(" ")
	for word in unique_words:
		word=word.lower()

		if word not in data:

			if word.isdigit():
				pass
			
			elif word.endswith("\n"):
				word=word.strip()
				data.add(word)

			else:
				data.add(word)	

			data_unique[word]=1
		else:
			data_unique[word]+=1	

print len(data)			

for i,j in data_unique.items():
	print (i,j)


