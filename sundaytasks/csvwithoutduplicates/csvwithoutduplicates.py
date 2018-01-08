filereader = open('duplicatecsvfile.csv').read().split('\n')
newlist = []
for val in filereader:
    if val not in newlist:
         newlist.append(val)
         

outputfile = open('withoutduplicates.csv', 'w')
outputfile.write('\n'.join(newlist))