# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

# students_map - student_id, audytorium_id

students_map = [(1, 3),
                (2, 3),
                (3, 1),
                (4, 2)]

cursor.executemany('''
                INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?);
                ''', students_map)

connection.commit()
connection.close()