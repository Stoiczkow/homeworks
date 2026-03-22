#Zadanie 2 – Najdroższy produkt

#Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji MAX().

import sqlite3

Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
cursor = Connection.cursor() # tworzenie obiektu kursora

# uzycie najdrozszy przedmiot w sklepie funkcja MAX() - cena jest w produkty

cursor.execute("""
                SELECT MAX(cena), nazwa_produktu FROM Produkty
                """)
# uzycie max i GROUP BY
# nazwa produktu wystarczy bo pobiera nadrozszy przedmiot
result = cursor.fetchone() # wyświetla 1 wynik

print(result)

Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
Connection.close()