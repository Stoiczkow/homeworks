import sqlite3

DATABASE_NAME = 'todo_raw.db'


# ZADANIE 8
class TaskManagerRaw:
    """Zarządza operacjami na bazie danych dla listy zadań."""

    def __init__(self, database_name: str = DATABASE_NAME):
        self.database_name = database_name
        self.init_db()

    def init_db(self):
        """Inicjalizuje bazę danych i tworzy tabelę, jeśli nie istnieje."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS zadania (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                opis TEXT NOT NULL,
                zrobione BOOLEAN NOT NULL CHECK (zrobione IN (0, 1)),
                priorytet INTEGER DEFAULT 1
            )
    ''')
            cursor.execute("PRAGMA table_info(zadania)")
            kolumny = [kolumna[1] for kolumna in cursor.fetchall()]
            if "priorytet" not in kolumny:
                cursor.execute("ALTER TABLE zadania ADD COLUMN priorytet INTEGER DEFAULT 1")
            conn.commit()

    def dodaj_zadanie(self, opis: str, priorytet: int):
        """Dodaje nowe zadanie do bazy danych."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO zadania (opis, zrobione, priorytet) VALUES (?, ?, ?)",
                (opis, False, priorytet),
            )
            conn.commit()

    def pobierz_zadania(self):
        """Pobiera wszystkie zadania z bazy danych."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, opis, zrobione FROM zadania")
            return cursor.fetchall()

    def wyszukaj_zadania(self, fraza: str):
        """Wyszukuje zadania, których opis zawiera podaną frazę."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, opis, zrobione FROM zadania WHERE opis LIKE ?",
                (f"%{fraza}%",),
            )
            return cursor.fetchall()

    def oznacz_jako_zrobione(self, id_zadania: int):
        """Oznacza zadanie jako zrobione."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE zadania SET zrobione = ? WHERE id = ?",
                (True, id_zadania),
            )
            conn.commit()

    def usun_zadanie(self, id_zadania: int):
        """Usuwa zadanie z bazy danych po ID."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM zadania WHERE id = ?", (id_zadania,))
            conn.commit()
            return cursor.rowcount
# koniec zadania