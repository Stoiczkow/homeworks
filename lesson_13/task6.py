# 6. 🧠 Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS studenci (id_studenta INTEGER PRIMARY KEY,
                imie TEXT, nazwisko TEXT);
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS audytorium (id_audytorium INTEGER PRIMARY KEY,
                nazwa_budynku TEXT, numer_sali INTEGER);
                ''')

connection.close()