# Zadanie 6 – Dwie tabele: Studenci i Audytoria
#Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele: studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko (TEXT). audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT), numer_sali (INTEGER)

import sqlite3
from turtle import st

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON") # jak tego nie dodamy to mopżemy dodawać id studentów których nie ma

# dodanie tabli
cursor.execute("""
               CREATE TABLE IF NOT EXISTS studenci (
                   id_studenta INTEGER PRIMARY KEY,
                   imie TEXT,
                   nazwisko TEXT
               )
               
               """)
# stworzenie tabeli audtoria
cursor.execute("""
               CREATE TABLE IF NOT EXISTS audytoria (
                   id_audytorium INTEGER PRIMARY KEY,
                   nazwa_budynku TEXT,
                   numer_sali INTEGER
               )
               """)
# Dodanie studentów
students = [
    ('Paweł', 'Wyżykowski'),
    ('Jan', "Kowalski"),
    ('Janusz', 'Nowak'),
    ('Czesław', 'Michniewicz')
]
# Dodanie danych studentów
# executemany() – wiele rekordów Używasz gdy masz listę danych i chcesz je dodać naraz.
cursor.executemany("""
                   INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)
                  """, students)
# dane audytoria
auditories = [
    ('Budynek Główny', 1),
    ('Kotłownia', 11),
    ('Wydział Fizyki', 22)
]
# Dodanie danych audytoria
cursor.executemany("""
                   INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)
                  """, auditories)


connection.commit()
connection.close()