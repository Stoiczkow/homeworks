'''
Zadanie 2 - Najdroższy produkt

Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
MAX()
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("""
SELECT nazwa, cena
FROM Produkty
WHERE cena = (SELECT MAX(cena) FROM Produkty)
""")

wynik = cursor.fetchone()

if wynik:
    print("Najdroższy produkt:")
    print("Nazwa:", wynik[0])
    print("Cena:", wynik[1])
else:
    print("Brak produktów w bazie.")

conn.close()
