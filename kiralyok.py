from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='mysql',
                                 host='127.0.0.1',
                                 database='kiralyok')

#táblák megjelenítése
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
print("-------------")

#uralkodók megjelenítése
cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)
print("-------------")

#Mátyás király
cursor.execute("SELECT * FROM uralkodo WHERE nev = 'I. Mátyás'")
for uralkodo in cursor:
    print(uralkodo)
print("-------------")


#Mátyás király születése, halála
cursor.execute("SELECT szul,hal FROM uralkodo WHERE nev = 'I. Mátyás'")
for uralkodo in cursor:
    print(f"Mátyás király élt: {uralkodo[0]} - {uralkodo[1]} ")
print("-------------")

cnx.close()