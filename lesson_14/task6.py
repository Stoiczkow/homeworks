# Zadanie 6 – Produkty droższe od średniej

# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie

import sqlite3

Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
cursor = Connection.cursor() # tworzenie obiektu kursora
# musimy przy join uzyc tej pragmy

querry = """

        SELECT nazwa_produktu, cena FROM Produkty 
        WHERE cena > (SELECT AVG(cena) FROM Produkty)
"""

# wykonujemy select w selecie podzapytanie. średnia jest w nawiasach i 2 slecet

cursor.execute(querry)

result = cursor.fetchall()

for product in result:
    print(product)
# wyświetli wynik jeden pod drugim


Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
Connection.close()