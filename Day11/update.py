import psycopg2

database= psycopg2.connect(host='localhost',user = 'postgres', password='test123',database='postgres')


curs = database.cursor()




curs.execute("update user_profile set first_name='richhi' where id='1'")

database.commit()

curs.close()

database.close()

