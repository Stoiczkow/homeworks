'''
Zadanie 4 - Średnia cena książki

Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG()
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("""
SELECT AVG(Produkty.cena)
FROM Produkty
JOIN Kategorie ON Produkty.kategoria_id = Kategorie.id
WHERE Kategorie.nazwa = 'Książki'
""")

srednia = cursor.fetchone()[0]

if srednia is None:
    print("Brak produktów w kategorii Książki.")
else:
    print("Średnia cena produktów w kategorii Książki:", srednia)

conn.close()
