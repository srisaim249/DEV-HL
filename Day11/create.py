import psycopg2

database= psycopg2.connect(host='localhost',user = 'postgres', password='test123',database='postgres')


curs = database.cursor()




curs.execute("create table  user_profile(id integer primary key,first_name varchar(30),last_name varchar(30),gender varchar(30))")

database.commit()

curs.close()

database.close()


