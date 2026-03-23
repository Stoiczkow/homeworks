# Zadanie 8 – Kategorie z liczbą produktów
# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY

import sqlite3

path = 'homeworks/lesson_14/'
conn = sqlite3.connect(path+'sklep.db')
c = conn.cursor()
c.execute('''
select k.nazwa_kategorii, count(p.id_kategorii) from Kategorie k join Produkty p on k.id_kategorii = p.id_kategorii group by p.id_kategorii
''')

kat = c.fetchall()

for nazwa, liczba in kat:
    print (f"Produktów {nazwa} jest {liczba}")

conn.commit()
conn.close()