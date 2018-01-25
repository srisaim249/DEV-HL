import mysql.connector

database=mysql.connector.connect(host='localhost',user='root',password='password',database='COMPANY')

cusor=database.cursor()

cusor.execute("CREATE TABLE COMPANY_DETAILS(companyCIN VARCHAR(30) PRIMARY KEY ,company_name VARCHAR(40) ,location VARCHAR(40),pin VARCHAR(40))")

cusor.execute("CREATE TABLE COMPANY_CATEGORIES(companyCIN VARCHAR(30) PRIMARY KEY ,categories VARCHAR(40) ,city_tier VARCHAR(40))")


cusor.close()
database.close()