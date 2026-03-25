# Zadanie 6 – Produkty droższe od średniej
# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie.

import sqlite3

connection = sqlite3.connect("sklep.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

query = """
    SELECT p.nazwa_produktu, p.cena
    FROM Produkty AS p
    WHERE p.cena > (
        SELECT AVG(p2.cena)
        FROM Produkty AS p2
    )
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

connection.close()