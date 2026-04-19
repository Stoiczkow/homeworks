#  Zadanie 10 – Funkcja wyszukująca z JOIN

# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.

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

# Dodanie rekordów do nowej bazy ppowiązań

students_auditories = [
    (1, 2),
    (2, 1),
    (2, 3),
    (3, 1),
    (3, 1)
]

# wykonanie dodania danych powyzej

#exceutemany bo więcej niż 1 rekord
# uczen o takim id ma zajecia w sali na takim id
# cursor.executemany("""
#                 INSERT INTO studenci_audytoria (student_id , id_audytorium) VALUES (?, ?)
# """, students_auditories)


# pracujemy juz na tej nowej 3 tabeli studenc_audytoria
# Stisujemy JOIN pozwala krzystać z wyników 2 tabel tutak akurat audytora.nazwa_budynku i adytoria.numer_sali // wtniku dlacza dane z tabeli powiazanej

# on pozwala polaczyc dane 
cursor.execute("""
               SELECT audytoria.nazwa_budynku, audytoria.numer_sali
FROM studenci_audytoria 
JOIN audytoria ON studenci_audytoria.id_audytorium = audytoria.id_audytorium
JOIN studenci ON studenci.id_studenta = studenci_audytoria.student_id
WHERE studenci.nazwisko = 'Wyżykowski'
               """)

# 2 metoda z przypisaniami prostsza 
cursor.execute("""
SELECT *
FROM studenci_audytoria as sa
JOIN audytoria as a ON sa.id_audytorium = a.id_audytorium
JOIN studenci as s ON s.id_studenta = sa.student_id
WHERE s.nazwisko = 'Wyżykowski'
""")

result = cursor.fetchall()
print(result)

connection.commit()
connection.close()