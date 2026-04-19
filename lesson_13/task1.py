# Zadanie 1 – Stwórz tabelę książek

# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)

# na początku zawsze trzeba pamietać przy pracy z tymi bibliotekami to commit
# i conection close 

import sqlite3

connection = sqlite3.connect("biblioteka.db") # obiekt połączenia - połączenie z baz danych jeśli nie istnieje zostanie utworzona

# obiekt kursora którymi robimy execute
# kursor musi być przypisany do zmiennej
 
cursor = connection.cursor()

# tworzenie tabeli ksiazki      # nie trzeba dodawać średników ta biblioteka sama dodaje je, ale w innym wypadku trzeba je dodać 
cursor.execute("""CREATE TABLE IF NOT EXISTS ksiazki 
               (id INTEGER PRIMIARY KEY,
                tytul TEXT NOT NULL, 
               autor TEXT NOT NULL,
               rok_wydania INTEGER )
               """)


# zapisanie zmian
connection.commit() # do zapisywania operacji update albo insert

# zamknięcie połaczenia
connection.close()

# wywołanie
print("Tablea został utworzona ")