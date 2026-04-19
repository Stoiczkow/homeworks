# Zadanie 1 – Liczba produktów

# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w tabeli Produkty. Użyj funkcji COUNT()

import sqlite3

Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
cursor = Connection.cursor() # tworzenie obiektu kursora

# uzycie coint ile produktów w bazie produty

cursor.execute("""
                SELECT COUNT(id_produktu) FROM Produkty
                """)
# uzycie count

result = cursor.fetchone() # wyświetla 1 wynik
result = cursor.fetchall() # gdyby było kilka produktów
print(result)

Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
Connection.close()




















# SELECT – pobieranie danych
# INSERT – dodawanie danych
# UPDATE – aktualizacja danych
# DELETE – usuwanie danych
# CREATE TABLE – tworzenie tabel
# JOIN – łączenie tabel