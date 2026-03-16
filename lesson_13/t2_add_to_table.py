# Zadanie 2 – Dodaj książki
# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem.

import sqlite3

connection = sqlite3.connect('biblioteka.db')

cursor = connection.cursor()

books_list = [
    ("HP", "Tom Cruise", 1995),
    ("LOTR", "ABC", 1956),
    ("Kosmos", "Helen", 2005)
]

cursor.executemany(
    """
        INSERT INTO ksiazki (tytul, autor, rok_wydania)
        VALUES (?, ?, ?)
    """, books_list
)

connection.commit()

connection.close()
