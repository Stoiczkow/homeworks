'''
    Zadanie 3 - Wyświetl całą bibliotekę

    Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
    tabeli ksiazki.
'''

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

c.execute("SELECT * FROM ksiazki")
wyniki = c.fetchall()

for ksiazka in wyniki:
    print(ksiazka)

conn.close()
