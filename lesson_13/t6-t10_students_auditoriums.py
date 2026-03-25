# Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).
# ZADANIA od 6-10

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute(
    """
         CREATE TABLE IF NOT EXISTS studenci(
            id_studenta INTEGER PRIMARY KEY,
            imie TEXT,
            nazwisko TEXT
         )
    """
)

cursor.execute(
    """
         CREATE TABLE IF NOT EXISTS audytoria(
            id_audytorium INTEGER PRIMARY KEY,
            nazwa_budynku TEXT,
            numer_sali INTEGER
         )
    """
)

students = [
    ('Jarek', 'Abacz'),
    ('Jan', 'Kowalski'),
    ('Marcin', 'Baka'),
    ('Marian', 'Gałązka')
]

# cursor.executemany(
#     """
#         INSERT INTO studenci (imie, nazwisko)
#         VALUES (?, ?)
#     """,
#     students
# )

auditories = [
    ('Budynek główny', 1),
    ('Wydział chemiczny', 2),
    ('Wydział fizyczny', 3),
]

# cursor.executemany(
#     """
#         INSERT INTO audytoria (nazwa_budynku, numer_sali)
#         VALUES (?, ?)
#     """,
#     auditories
# )

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS studenci_audytoria(
            id_przypisania INTEGER PRIMARY KEY,
            student_id INTEGER REFERENCES studenci(id_studenta),
            id_audytorium INTEGER REFERENCES audytoria(id_audytorium)
        )
    """
)

students_auditories = [
    (1, 2),
    (2, 1),
    (2, 3),
    (3, 1),
    (3, 1)
]

# cursor.executemany(
#     """
#         INSERT INTO studenci_audytoria (student_id, id_audytorium)
#         VALUES (?, ?)
#     """, students_auditories
# )

cursor.execute(
    """
        SELECT * FROM studenci_audytoria as sa
            JOIN audytoria AS a 
                ON sa.id_audytorium = a.id_audytorium
            JOIN studenci  AS s 
                ON s.id_studenta = sa.student_id
        WHERE s.nazwisko = "Labuzek"
    """
)
result = cursor.fetchall()
print(result)

connection.commit()

connection.close()