# Zadanie 2 – Dodaj książki

# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki. Użyj metody executemany do dodania wszystkich książek za jednym razem.

# na początku zawsze trzeba pamietać przy pracy z tymi bibliotekami to commit
# i conection close 

import sqlite3

connection = sqlite3.connect("biblioteka.db") # obiekt połączenia - połączenie z baz danych jeśli nie istnieje zostanie utworzona

# obiekt kursora którymi robimy execute
# kursor musi być przypisany do zmiennej
 
cursor = connection.cursor()

# Lista książek do dodania
ksiazki = [
    ("tytul1", "autor1", 2000),
    ("tytul2", "autor2", 2005),
    ("tytul3", "autor3", 2010)
]

# Dodanie książek do tabeli przez executemany
cursor.executemany("""
                INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)
                """, ksiazki)



# zapisanie zmian
connection.commit() # do zapisywania operacji update albo insert

##### Musimy to dać przed close bo inaczej tabela zamknieta

# wywołanie
print("Tablea został utworzona ")

# wyświetlenie dodanych listy ksaizek
cursor.execute("""
                SELECT * FROM ksiazki
""")

print(cursor.fetchall()) # to jest metoda wiec nawiasy ()



# zamknięcie połaczenia
connection.close()

