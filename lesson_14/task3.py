# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
# SUM() oraz klauzuli WHERE z JOIN.

import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute('''SELECT SUM(p.cena) FROM produkty as p
                JOIN kategorie as k
                ON k.id_kategorii = p.id_kategorii
                WHERE k.nazwa_kategorii = "Elektronika"''')

result = cursor.fetchone()

print(f"Wynik: {result[0]}")

conn.commit()
conn.close()