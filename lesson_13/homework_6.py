#  Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele: 
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),numer_sali (INTEGER)

path = 'homeworks/lesson_13/'

import sqlite3

conn = sqlite3.connect(path+'uczelnia.db')


c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS studenci (
id_studenta INTEGER PRIMARY KEY,
imie TEXT NOT NULL,
nazwisko TEXT NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS audytoria (
id_audytorium INTEGER PRIMARY KEY,
nazwa_budynku TEXT NOT NULL,
numer_sali INTEGER
)
''')

conn.commit()

conn.close()

