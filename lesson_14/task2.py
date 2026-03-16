# TASK 2

# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX()

import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute('SELECT MAX(cena), nazwa_produktu FROM produkty')

result = cursor.fetchone()

print(result)

conn.commit()
conn.close()