fileread=open("message.txt")
for val in fileread:
      print(val)


print(open("message.txt", "r").readlines()[1])
