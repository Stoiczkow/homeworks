'''
    Zadanie 5 - Zaktualizuj rok wydania

    Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
    inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
    powiodła
'''

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.c()


tytul = input("Podaj tytuł książki, której rok chcesz zaktualizować: ")
nowy_rok = int(input("Podaj nowy rok wydania: "))

c.execute("""
UPDATE ksiazki
SET rok_wydania = ?
WHERE tytul = ?
""", (nowy_rok, tytul))

conn.commit()

c.execute("SELECT * FROM ksiazki WHERE tytul = ?", (tytul,))
wynik = c.fetchone()

if wynik:
    print("Zaktualizowana książka:")
    print(wynik)
else:
    print("Nie znaleziono książki o podanym tytule.")

conn.close()
