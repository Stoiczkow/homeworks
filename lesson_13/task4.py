# Zadanie 4 – Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały napisane przez Twojego ulubionego autor


import sqlite3

connection = sqlite3.connect("biblioteka.db") # obiekt połączenia - połączenie z baz danych jeśli nie istnieje zostanie utworzona

# obiekt kursora którymi robimy execute
# kursor musi być przypisany do zmiennej
 
cursor = connection.cursor()

# # Lista książek do dodania
# ksiazki = [
#     ("tytul1", "autor1", 2000),
#     ("tytul2", "autor2", 2005),
#     ("tytul3", "autor3", 2010)
# ]

# # Dodanie książek do tabeli przez executemany
# cursor.executemany("""
#                 INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)
#                 """, ksiazki)

# zapisanie zmian
connection.commit() # do zapisywania operacji update albo insert

##### Musimy to dać przed close bo inaczej tabela zamknieta

# wywołanie
# # print("Tablea został utworzona ")

# # wyświetlenie dodanych listy ksaizek
# cursor.execute("""
#                 SELECT * FROM ksiazki
# """)

# print(cursor.fetchall()) # to jest metoda wiec nawiasy ()
# jest odpowiedzialne za pobranie wszystkich wyników zapytania SQL, które wcześniej wykonaliśmy przez cursor.execute()
# cursor.fetchall() → pobiera wszystkie rekordy z zapytania SELECT

###############################################
#Task 4
cursor.execute("""
                SELECT * FROM ksiazki WHERE autor = "autor2"

""")
print(cursor.fetchall()) # jest odpowiedzialne za pobranie wszystkich wyników zapytania SQL        

# zamknięcie połaczenia
connection.close() 


# Inne podobne metody
# fetchone() → pobiera tylko jeden rekord
# fetchmany(n) → pobiera n rekordów
# fetchall() → pobiera wszystkie rekordy

# execute() → wysyła zapytanie
# fetchall() → odbiera wszystkie wyniki z bazy.