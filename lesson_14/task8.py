# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
# do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY

import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute('''SELECT nazwa_kategorii, COUNT(p.id_kategorii) FROM Kategorie as k
                JOIN Produkty as p ON k.id_kategorii = p.id_kategorii
                GROUP BY p.id_kategorii
                ''')

result = cursor.fetchall()

for name, liczba in result:
    print(f"Nazwa: {name}, liczba: {liczba}")

conn.commit()
conn.close()