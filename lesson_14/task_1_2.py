import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

# task 1

cursor.execute("""
               SELECT COUNT(id_produktu) FROM Produkty
               """)

#result = cursor.fetchall()
#result = cursor.fetchone()

#print(result)

# task 2

cursor.execute("""
               SELECT MAX(cena), nazwa_produktu FROM Produkty 
               """)

result = cursor.fetchone()

print(result)
connection.commit()
connection.close()