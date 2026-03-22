# Zadanie 3 – Suma wartości

# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji SUM() oraz klauzuli WHERE z JOIN.

import sqlite3

Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
cursor = Connection.cursor() # tworzenie obiektu kursora
# musimy przy join uzyc tej pragmy
cursor.execute("PRAGMA foreign_keys = ON")

# uzywamy SUM  + JOIN

cursor.execute("""
          SELECT SUM(cena) FROM Produkty AS p
        JOIN Kategorie AS k
               ON k.id_kategorii = p.id_kategorii
            WHERE K.NAZWA_KATEGORII = "Elektronika"
               
                     
                """)
# JOIN - kategorie

result = cursor.fetchone() # wyświetla 1 wynik

print(result[0])
# sumuje przedmioty z id 1 bo elektronika 
# [0] poniewaz bierze pierwsza z lewej wartosc nie wszystkie po kolej

Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
Connection.close()