# Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS ksiazki (
          id INTEGER PRIMARY KEY,
          tytul TEXT NOT NULL,
          autor TEXT NOT NULL,
          rok_wydania INTEGER
          )
            """)
conn.commit()
# conn.close()

# Zadanie 2 – Dodaj książki
# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki. Użyj metody executemany do dodania wszystkich książek za jednym razem.

ksiazki = [
            ("Koniec dzieciństwa", "Arthur C.Clarke", 2025),
            ("Python: Instrukcje dla programisty", "Eric Matthes", 2023),
            ("Nienazwane", "H.P. Lovecraft", 2017)
            ]

c.executemany("INSERT INTO ksiazki(tytul, autor, rok_wydania) VALUES(?,?,?)", ksiazki)

# Zadanie 3 – Wyświetl całą bibliotekę
# Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z tabeli ksiazki.

c.execute("SELECT * FROM ksiazki")
ksiazki = c.fetchall()

for ksiazka in ksiazki:
    print(f"| ID: {ksiazka[0]} | Tytul: {ksiazka[1]} | Autor: {ksiazka[2]} | Rok wydania: {ksiazka[3]} |")

# Zadanie 4 – Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały napisane przez Twojego ulubionego autora.

c.execute("SELECT * FROM ksiazki WHERE autor = ?", ("Arthur C.Clarke", ))

ksiazki_autora = c.fetchall()

for ksiazka in ksiazki_autora:
    print(ksiazka)

# Zadanie 5 – Zaktualizuj rok wydania
# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się powiodła.

c.execute("UPDATE ksiazki SET rok_wydania = ? WHERE tytul =?", (1957, "Koniec dzieciństwa"))

conn.commit()

c.execute("SELECT * FROM ksiazki WHERE tytul = ?", ("Koniec dzieciństwa", ))
nowa_ksiazka = c.fetchone()

print(nowa_ksiazka)

conn.close()