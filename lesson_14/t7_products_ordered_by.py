# Zadanie 7 – Zamówienia Anny Nowak
# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
# imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
# Zamowienia, Zamowienia_Produkty i Produkty.

import sqlite3

connection = sqlite3.connect("sklep.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

query = """
    SELECT nazwa_produktu FROM Produkty as p
    JOIN Zamowienia_Produkty as zp 
        ON p.id_produktu = zp.id_produktu
    JOIN Zamowienia as z 
        ON z.id_zamowienia = zp.id_zamowienia
    JOIN Klienci as k
        ON k.id_klienta = z.id_klienta
    WHERE k.imie = "Anna Nowak"
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

connection.close()