fileread=open("message.txt")
for val in fileread:
      print(val)


print(open("message.txt", "r").readlines()[0]) # it reads the perticular line data present in the file