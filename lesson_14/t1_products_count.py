# Zadanie 1 – Liczba produktów
# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().

import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# here
cursor.execute(
    """
        SELECT COUNT() FROM Produkty
    """
)
result = cursor.fetchone()
print(result[0])

connection.commit()

connection.close()