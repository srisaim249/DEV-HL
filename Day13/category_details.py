import mysql.connector

database=mysql.connector.connect(host='localhost',user='root',password='password',database='COMPANY')

cusor=database.cursor()

cusor.execute("CREATE TABLE CATEGORY_DETAILS(companyCIN VARCHAR(30) ,categories VARCHAR(40) ,city_tier VARCHAR(40),FOREIGN KEY (companyCIN) REFERENCES COMPANY_CATEGORIES(companyCIN))")




cusor.close()
database.close()