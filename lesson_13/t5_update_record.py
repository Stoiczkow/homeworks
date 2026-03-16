# Zadanie 5 – Zaktualizuj rok wydania
# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
# inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
# powiodła.

import sqlite3

connection = sqlite3.connect('biblioteka.db')

cursor = connection.cursor()

cursor.execute(
    """
        UPDATE ksiazki SET rok_wydania = ?
        WHERE id = ?
    """, (2025, 2)
)

connection.commit()

cursor.execute(
    """
        SELECT * FROM ksiazki
        WHERE id = 2
    """
)

print(cursor.fetchone())

connection.close()