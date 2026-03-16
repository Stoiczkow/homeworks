#  Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3
import random

connection = sqlite3.connect('uczelnia.db')

cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS studenci
               (id_studenta INTEGER PRIMARY KEY,
               imie TEXT,
               nazwisko TEXT
               )""")

cursor.execute("""
                CREATE TABLE IF NOT EXISTS audytoria
               (id_audytorium INTEGER PRIMARY KEY,
               nazwa_budynku TEXT,
               numer_sali INTEGER
               )
               """)

# 7. 🧠 Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
# najmniej 4 studentów i 3 audytoria.

students = [
    ("imie_1", "nazwisko_1"),
    ("imie_2", "nazwisko_2"),
    ("imie_3", "nazwisko_3"),
    ("imie_4", "nazwisko_4")
]


auditoriums = [
    ("budynek_1", 1),
    ("budynek_2", 2),
    ("budynek_3", 3),
]

# cursor.executemany("""
#                     INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)
#                    """, students)

# cursor.executemany("""
#                     INSERT INTO audytoria 
#                    (nazwa_budynku, numer_sali) VALUES (?, ?)
#                    """, auditoriums)

print("======== STUDENCI =========")
cursor.execute("""
                SELECT * FROM studenci
                """)

print(cursor.fetchall())

print("======== AUDYTORIA =========")
cursor.execute("""
                SELECT * FROM audytoria
                """)

print(cursor.fetchall())

# 8. 🧠 Zadanie 8 – Połącz tabele (Relacja)
# To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
# audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej
# samej bazie uczelnia.db. Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w
# tabeli studenci .
# id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli
# audytoria .

cursor.execute("""
                CREATE TABLE IF NOT EXISTS przypisania
               (id_przypisania INTEGER PRIMARY KEY,
               id_studenta INTEGER,
               id_audytorium INTEGER,
               FOREIGN KEY (id_studenta) REFERENCES studenci(id_studenta),
               FOREIGN KEY (id_audytorium) REFERENCES audytoria(id_audytorium)
               )
               """)

# 9. 🧠 Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów.

assignments = []

for s_index, student in enumerate(students, start=1):
    a_index = random.randint(1, len(auditoriums))
    assignments.append((s_index, a_index))

cursor.executemany("""
                   INSERT INTO przypisania (id_studenta, id_audytorium) 
                   VALUES (?, ?)
               """, assignments)

connection.commit()

connection.close()