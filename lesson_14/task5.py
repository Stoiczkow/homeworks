#Zadanie 5 – Lista klientów

# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.

import sqlite3

Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
cursor = Connection.cursor() # tworzenie obiektu kursora
# musimy przy join uzyc tej pragmy
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""

            SELECT imie, email FROM Klienci 

""")

result = cursor.fetchall()

for user in result: # wyświetli wynik jeden pod drugim 
    print(user)
# print(result)

# sztucznie dodane indesky 1,2,3
for index,user in enumerate(result, start=1): # wyświetli wynik jeden pod drugim , dodane wyśiwetlanie od 1
    print(f"{index} - {user}")

Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
Connection.close()