'''
    Zadanie 1 - Liczba produktów

    Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
    tabeli Produkty. Użyj funkcji COUNT()
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM Produkty")
liczba = cursor.fetchone()[0]

print("Liczba produktów w tabeli:", liczba)

conn.close()
