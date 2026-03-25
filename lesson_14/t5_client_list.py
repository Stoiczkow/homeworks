# Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.


import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

query = "SELECT imie, email FROM Klienci"
cursor.execute(query)

result = cursor.fetchall()

for user in result:
    print(user)

for index, user in enumerate(result):
    print(f"{index} -> {user}")

connection.commit()

connection.close()