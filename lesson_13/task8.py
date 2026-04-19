# Zadanie 8 – Połącz tabele (Relacja)

# o zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej samej bazie uczelnia.db. Tabela powinna mieć strukturę: id_przypisania (INTEGER, klucz główny) id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w tabeli studenci . id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli audytoria 


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
# cursor.executemany("""
#                    INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)
#                   """, students)
# dane audytoria
auditories = [
    ('Budynek Główny', 1),
    ('Kotłownia', 11),
    ('Wydział Fizyki', 22)
]
# Dodanie danych audytoria
# cursor.executemany("""
#                    INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)
#                   """, auditories)

# tabela relacji powiązań - w jakiej sali studenci maja zajecia

# Stworzenie samej tabeli
# Stworzyliśmy 3 tabelkę powiazań z powiazaniem kluczy (tak najlpeiej)
cursor.execute("""
                CREATE TABLE IF NOT EXISTS studenci_audytoria (id_przypisania INTEGER PRIMARY KEY,
                
               student_id INTEGER REFERENCES studenci (id_studenta),

               id_audytorium INTEGER REFERENCES audytoria (id_audytorium)
               
               )
               

               
            """)
# studenci_audytoria sama nazwa juz oznacza powazanie 
#REFERENCES  - oznacza powiazanie 
# studenci nazwa tabeli - sprawdzamy primary key w studenci zeby powaziac 
# audytorium nazwa tabeli - sprawdzamy primary key w auditorium zeby powaziac
connection.commit()
connection.close()