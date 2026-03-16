# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie

import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute('''SELECT nazwa_produktu, cena FROM produkty
                WHERE cena > (SELECT AVG(cena) FROM produkty)''')

result = cursor.fetchall()

print(result)

conn.commit()
conn.close()