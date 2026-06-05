'''
    Zadanie 4 - Wyszukaj książki autora

    Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
    napisane przez Twojego ulubionego autora.
'''

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

autor = input("Podaj autora, którego książki chcesz wyświetlić: ")

c.execute("SELECT * FROM ksiazki WHERE autor = ?", (autor,))
wyniki = c.fetchall()

if wyniki:
    for ksiazka in wyniki:
        print(ksiazka)
else:
    print("Brak książek tego autora w bazie.")

conn.close()
