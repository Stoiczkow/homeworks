import sqlite3


class TaskManagerRaw:
    def __init__(self, database_name='todo_raw.db'):
        self.database_name = database_name
        self.init_db()

    def _connect(self):
        return sqlite3.connect(self.database_name)

    def init_db(self):
        """Inicjalizuje bazę danych i tworzy tabelę, jeśli nie istnieje."""
        with self._connect() as conn:
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

    def dodaj_zadanie(self, opis: str, priorytet: int):
        """Dodaje nowe zadanie do bazy danych."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO zadania (opis, zrobione, priorytet) VALUES (?, ?, ?)",
                           (opis, False, priorytet))
            conn.commit()

    def pobierz_zadania(self):
        """Pobiera wszystkie zadania z bazy danych."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, opis, zrobione, priorytet FROM zadania")
            return cursor.fetchall()

    def wyszukaj_zadania(self, fraza: str):
        """Wyszukuje zadania po frazie w opisie."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, opis FROM zadania WHERE opis LIKE ?", (f"%{fraza}%",))
            return cursor.fetchall()

    def oznacz_jako_zrobione(self, id_zadania: int):
        """Oznacza zadanie o podanym ID jako zrobione."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE zadania SET zrobione = ? WHERE id = ?",
                           (True, id_zadania))
            conn.commit()

    def usun_zadanie(self, id_zadania: int):
        """Usuwa zadanie o podanym ID."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM zadania WHERE id = ?", (id_zadania,))
            conn.commit()