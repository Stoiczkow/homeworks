# Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)

import sqlite3

connection = sqlite3.connect('biblioteka.db')

cursor = connection.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS ksiazki (
            id INTEGER PRIMARY KEY,
            tytul TEXT NOT NULL,
            autor TEXT NOT NULL,
            rok_wydania INTEGER
        );
    """
)

connection.commit()

connection.close()
