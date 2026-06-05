'''
Zadanie 3 - Suma wartości

Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
SUM() oraz klauzuli WHERE z JOIN
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("""
SELECT SUM(Produkty.cena)
FROM Produkty
JOIN Kategorie ON Produkty.kategoria_id = Kategorie.id
WHERE Kategorie.nazwa = 'Elektronika'
""")

suma = cursor.fetchone()[0]

if suma is None:
    print("Brak produktów w kategorii Elektronika.")
else:
    print("Łączna wartość produktów z kategorii Elektronika:", suma)

conn.close()
