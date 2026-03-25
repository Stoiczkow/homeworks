# Zadanie 2 – Najdroższy produkt
# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX().

import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# here
cursor.execute(
    """
        SELECT MAX(p.cena) FROM Produkty AS p
    """
)

(max_price,) = cursor.fetchone()
print(max_price)

connection.commit()

connection.close()