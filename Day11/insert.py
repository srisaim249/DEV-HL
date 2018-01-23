import psycopg2

database= psycopg2.connect(host='localhost',user = 'postgres', password='test123',database='postgres')


curs = database.cursor()




#curs.execute("insert into user_profile values('1','gowtham','bobby','male')")

curs.execute("insert into user_profile values('2','sai','sri','female'),('3','rocky','bob','male'),('4','silvy','sekhar','male')")


database.commit()

curs.close()

database.close()

