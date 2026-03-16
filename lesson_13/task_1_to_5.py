# Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)

import sqlite3

def create_books_table():
    conn = sqlite3.connect('lesson_13/biblioteka.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ksiazki (
            id INTEGER PRIMARY KEY,
            tytul TEXT NOT NULL,
            autor TEXT NOT NULL,
            rok_wydania INTEGER
        )
    ''')

    conn.commit()
    conn.close()

create_books_table()

# Zadanie 2 – Dodaj książki
# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem

def add_books():
    conn = sqlite3.connect('lesson_13/biblioteka.db')
    cursor = conn.cursor()

    books = [
        ('Wiedźmin', 'Andrzej Sapkowski', 1990),
        ('Harry Potter i Kamień Filozoficzny', 'J.K. Rowling', 1997),
        ('Mistrz i Małgorzata', 'Michaił Bułhakow', 1967)
    ]

    cursor.executemany('''
        INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)
    ''', books)

    conn.commit()
    conn.close()

add_books()

# Zadanie 3 – Wyświetl całą bibliotekę
# Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
# tabeli ksiazki.

def display_books():
    conn = sqlite3.connect('lesson_13/biblioteka.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ksiazki')
    books = cursor.fetchall()

    for book in books:
        print(book)

    conn.close()

display_books()

# Zadanie 4 - Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
# napisane przez Twojego ulubionego autora.

def search_books_by_author(author):
    conn = sqlite3.connect('lesson_13/biblioteka.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ksiazki WHERE autor = ?', (author,))
    books = cursor.fetchall()

    for book in books:
        print(book)

    conn.close()

search_books_by_author('Andrzej Sapkowski')

# Zadanie 5 - Zaktualizuj rok wydania
# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
# inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
# powiodła.

def update_book_year(title, new_year):
    conn = sqlite3.connect('lesson_13/biblioteka.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE ksiazki SET rok_wydania = ? WHERE tytul = ?', (new_year, title))
    conn.commit()

    cursor.execute('SELECT * FROM ksiazki WHERE tytul = ?', (title,))
    book = cursor.fetchone()
    print(book)

    conn.close()

update_book_year('Wiedźmin', 1995)