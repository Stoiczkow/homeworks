import sqlite3

DATABASE_NAME = 'todo_raw.db'

def init_db():
    """Inicjalizuje bazę danych i tworzy tabelę, jeśli nie istnieje."""
    
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS zadania (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            opis TEXT NOT NULL,
            zrobione BOOLEAN NOT NULL CHECK (zrobione IN (0, 1)),
            priorytet INTEGER DEFAULT 1
            )
        ''')
    conn.commit()

def dodaj_zadanie(opis: str):
    """Dodaje nowe zadanie do bazy danych."""
    
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO zadania (opis, zrobione) VALUES (?, ?)",
    (opis, False))
    conn.commit()

def pobierz_zadania():
    """Pobiera wszystkie zadania z bazy danych."""
    
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, opis, zrobione FROM zadania")
        return cursor.fetchall()
    
def oznacz_jako_zrobione(id_zadania: int):
    """Oznacza zadanie o podanym ID jako zrobione."""
    
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE zadania SET zrobione = ? WHERE id = ?",
        (True, id_zadania))
        conn.commit()