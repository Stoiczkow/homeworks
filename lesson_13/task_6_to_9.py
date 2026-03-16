# Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER). 

import sqlite3

def create_tables():
    conn = sqlite3.connect('lesson_13/uczelnia.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS studenci (
            id_studenta INTEGER PRIMARY KEY,
            imie TEXT,
            nazwisko TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audytoria (
            id_audytorium INTEGER PRIMARY KEY,
            nazwa_budynku TEXT,
            numer_sali INTEGER
        )
    ''')

    conn.commit()
    conn.close()

create_tables()

# Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
# najmniej 4 studentów i 3 audytoria.

def add_data():
    conn = sqlite3.connect('lesson_13/uczelnia.db')
    cursor = conn.cursor()

    students = [
        (1, 'Jan', 'Kowalski'),
        (2, 'Anna', 'Nowak'),
        (3, 'Piotr', 'Zieliński'),
        (4, 'Katarzyna', 'Wiśniewska')
    ]

    auditoriums = [
        (1, 'Budynek A', 101),
        (2, 'Budynek B', 202),
        (3, 'Budynek C', 303)
    ]

    cursor.executemany('''
        INSERT INTO studenci (id_studenta, imie, nazwisko) VALUES (?, ?, ?)
    ''', students)

    cursor.executemany('''
        INSERT INTO audytoria (id_audytorium, nazwa_budynku, numer_sali) VALUES (?, ?, ?)
    ''', auditoriums)

    conn.commit()
    conn.close()

add_data()

# Zadanie 8 – Połącz tabele (Relacja)
# To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
# audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej
# samej bazie uczelnia.db. Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w
# tabeli studenci .
# id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli
# audytoria .

def create_assignments_table():
    conn = sqlite3.connect('lesson_13/uczelnia.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS przypisania (
            id_przypisania INTEGER PRIMARY KEY,
            id_studenta INTEGER,
            id_audytorium INTEGER,
            FOREIGN KEY (id_studenta) REFERENCES studenci(id_studenta),
            FOREIGN KEY (id_audytorium) REFERENCES audytoria(id_audytorium)
        )
    ''')

    conn.commit()
    conn.close()

create_assignments_table()

# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów.

def add_assignments():
    conn = sqlite3.connect('lesson_13/uczelnia.db')
    cursor = conn.cursor()

    assignments = [
        (1, 1, 1),  # Jan Kowalski -> Budynek A, sala 101
        (2, 2, 2),  # Anna Nowak -> Budynek B, sala 202
        (3, 3, 3),  # Piotr Zieliński -> Budynek C, sala 303
        (4, 4, 1)   # Katarzyna Wiśniewska -> Budynek A, sala 101
    ]

    cursor.executemany('''
        INSERT INTO przypisania (id_przypisania, id_studenta, id_audytorium) VALUES (?, ?, ?)
    ''', assignments)

    conn.commit()
    conn.close()

add_assignments()