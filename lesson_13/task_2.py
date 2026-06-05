'''
    Zadanie 2 - Dodaj książki

    Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
    Użyj metody executemany do dodania wszystkich książek za jednym razem.
'''

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

ksiazki = [
    ("Wiedźmin: Ostatnie życzenie", "Andrzej Sapkowski", 1993),
    ("Hobbit", "J.R.R. Tolkien", 1937),
    ("Rok 1984", "George Orwell", 1949)
]

c.executemany("""
INSERT INTO ksiazki (tytul, autor, rok_wydania)
VALUES (?, ?, ?)
""", ksiazki)

conn.commit()
conn.close()

print("Dodano 3 książki do tabeli.")
