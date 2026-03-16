# Zadanie 3 – Wyświetl całą bibliotekę
# Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
# tabeli ksiazki.

import sqlite3

connection = sqlite3.connect('biblioteka.db')

cursor = connection.cursor()

cursor.execute(
    """
        SELECT * from ksiazki
    """
)

list = cursor.fetchall()

print(list)

connection.commit()

connection.close()