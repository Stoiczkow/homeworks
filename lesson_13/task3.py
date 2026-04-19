#Zadanie 3 – Wyświetl całą bibliotekę

#Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z tabeli ksiazki

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
# jest odpowiedzialne za pobranie wszystkich wyników zapytania SQL, które wcześniej wykonaliśmy przez cursor.execute()
# cursor.fetchall() → pobiera wszystkie rekordy z zapytania SELECT


# zamknięcie połaczenia
connection.close()


# Inne podobne metody
# fetchone() → pobiera tylko jeden rekord
# fetchmany(n) → pobiera n rekordów
# fetchall() → pobiera wszystkie rekordy

# execute() → wysyła zapytanie
# fetchall() → odbiera wszystkie wyniki z bazy.