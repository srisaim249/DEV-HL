import psycopg2

database= psycopg2.connect(host='localhost',user = 'postgres', password='test123',database='postgres')


curs = database.cursor()




curs.execute("delete from  user_profile  where first_name='sai'")

database.commit()

curs.close()

database.close()

