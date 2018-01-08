import csv

readerfordata2=csv.reader(open('data2.csv', 'r'), delimiter=',')
writerfordata2=csv.writer(open('data2withoutduplicates.csv', 'w'), delimiter=',')

listofdata2 = set()
for row in readerfordata2:
    if row[0] not in listofdata2:
        writerfordata2.writerow(row)
        listofdata2.add( row[0] )

readerfordata1=csv.reader(open('data1.csv','r'),delimiter=',')
writerfordata1=csv.writer(open('data1withoutduplicates.csv', 'w'), delimiter=',')

listofdata1 = set()
for row in readerfordata1:
    if row[0] not in listofdata1:
        writerfordata1.writerow(row)
        listofdata1.add( row[0] )




print listofdata1
print listofdata2        