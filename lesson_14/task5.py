# Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.

import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute('''SELECT imie, email FROM Klienci''')

result = cursor.fetchall()

for i in result:
    print(f"Imię: {i[0]}, adres e-mail: {i[1]}")

conn.commit()
conn.close()