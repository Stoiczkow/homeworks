# Zadanie 4 – Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
# napisane przez Twojego ulubionego autora.

import sqlite3

connection = sqlite3.connect('biblioteka.db')

cursor = connection.cursor()

cursor.execute(
    """
        SELECT * FROM ksiazki
        WHERE autor = ?
    """, ("Tom Cruise",)
)

author = cursor.fetchall()

print(author)

connection.commit()

connection.close()