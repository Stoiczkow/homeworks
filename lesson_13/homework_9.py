# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis do tabeli przypisania, łącząc go z jednym z audytoriów


path = 'homeworks/lesson_13/'

import sqlite3

conn = sqlite3.connect(path+'uczelnia.db')
c = conn.cursor()

przypisania_studentow = [
    (1, 1024, 102),
    (2, 2048, 123),
    (3, 4096, 691),
    (4, 8192, 102)
]

# włączenie referencji
c.execute("PRAGMA foreign_keys = ON")
c.executemany(
    '''
        insert into przypisania (id_przypisania, id_studenta, id_audytorium)values(?,?,?)
    ''',
    przypisania_studentow
)


conn.commit()

conn.close()
