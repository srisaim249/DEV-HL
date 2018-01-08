fileread=open("MOCK_DATA.csv")

first_name=[]
email_name=[]
for val in fileread:
 eachrow=val.split(",")
 if(eachrow[1].startswith("A")):
  first_name.append(eachrow[1])
 if(eachrow[3].endswith("@amazon.com")):
  email_name.append(eachrow[3])


print(first_name) 
print(email_name) 

