# Zadanie 8 – Kategorie z liczbą produktów
# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
# do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.

import sqlite3

connection = sqlite3.connect("sklep.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

query = """
    SELECT nazwa_kategorii, COUNT(p.id_kategorii) AS ilosc FROM Kategorie AS k
    JOIN Produkty AS p
        ON p.id_kategorii = k.id_kategorii
    GROUP BY p.id_kategorii
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

connection.close()