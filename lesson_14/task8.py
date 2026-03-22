# Zadanie 8 – Kategorie z liczbą produktów

# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY

import sqlite3

Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
cursor = Connection.cursor() # tworzenie obiektu kursora
# musimy przy join uzyc tej pragmy

# zrobić count i pogrupowac

cursor.execute('''
select k.nazwa_kategorii, count(p.id_kategorii) from Kategorie k join Produkty p on k.id_kategorii = p.id_kategorii group by p.id_kategorii
''')

result = cursor.fetchall()

for nazwa, liczba in result:
    print(f"Produktów {nazwa}, jest {liczba}")

Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
Connection.close()

# Bierzesz tabelę Kategorie i nadajesz jej alias k.
