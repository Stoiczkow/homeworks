'''
Zadanie 5 - Lista klientów

Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
cursor = conn.cursor()

cursor.execute("SELECT imie, email FROM Klienci")
klienci = cursor.fetchall()

for klient in klienci:
    print(klient)

conn.close()
