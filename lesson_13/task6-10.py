# Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3

conn = sqlite3.connect("uczelnia.db")
c = conn.cursor()

c.execute("""
        CREATE TABLE IF NOT EXISTS studenci(
          id_studenta INTEGER PRIMARY KEY,
          imie TEXT,
          nazwisko TEXT
          )
        """)

c.execute("""
        CREATE TABLE IF NOT EXISTS audytoria(
          id_audytorium INTEGER PRIMARY KEY,
          nazwa_budynku TEXT,
          numer_sali INTEGER)
          """)

conn.commit()
# conn.close()

# Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co najmniej 4 studentów i 3 audytoria.

lista_studentow = [
                    ("Daniel", "Chomiak"),
                     ("Jan", "Kowalski"),
                     ("Janina", "Kowalska"),
                     ("Kowal", "Janowski")
]
lista_audytoriow = [
                    ("A", 111),
                    ("B", 222),
                    ("C", 333)
]   

c.executemany("INSERT INTO studenci(imie, nazwisko) VALUES(?, ?)", lista_studentow)

c.executemany("INSERT INTO audytoria(nazwa_budynku, numer_sali) VALUES(?, ?)", lista_audytoriow)

conn.commit()

# Zadanie 8 – Połącz tabele (Relacja)
# To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
# audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej samej bazie uczelnia.db. Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w
# tabeli studenci .
# id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli
# audytoria .

c.execute("""
            CREATE TABLE IF NOT EXISTS przypisania(
          id_przypisania INTEGER PRIMARY KEY,
          id_studenta INTEGER,
          id_audytorium INTEGER,
          FOREIGN KEY(id_studenta) REFERENCES studenci(id_studenta),
          FOREIGN KEY(id_audytorium) REFERENCES audytoria(id_audytorium)
          )
""")
# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis do tabeli przypisania, łącząc go z jednym z audytoriów.

lista_przypisan = [
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 3)
]

c.executemany("INSERT INTO przypisania(id_studenta, id_audytorium) VALUES (?, ?)", lista_przypisan)

conn.commit()

# Zadanie 10 – Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.

def znajdz_sale_studenta(nazwisko):
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()

    c.execute("SELECT audytoria.nazwa_budynku, audytoria.numer_sali FROM studenci JOIN przypisania ON studenci.id_studenta = przypisania.id_studenta JOIN audytoria ON przypisania.id_audytorium = audytoria.id_audytorium WHERE studenci.nazwisko = ?", (nazwisko, ))

    wyszukanie = c.fetchone()

    if wyszukanie:
        print(f"Student: {nazwisko} jest w sali {wyszukanie[1]} w budynku {wyszukanie[0]}")
    else:
        print("Nie znaleziono studenta.")
    conn.close()

znajdz_sale_studenta("Chomiak")
