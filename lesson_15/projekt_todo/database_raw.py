import sqlite3


class TaskManagerRaw:
    def __init__(self):
        self.database_name = "todo_raw.db"

    def init_db(self):
        """Inicjalizuje bazę danych i tworzy tabelę, jeśli nie istnieje."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS zadania (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    opis TEXT NOT NULL,
                    zrobione BOOLEAN NOT NULL CHECK (zrobione IN (0, 1)),
                    priorytet INTEGER DEFAULT 1
                )
            """)

            conn.commit()

    def dodaj_zadanie(self, opis: str, priorytet: int):
        """Dodaje nowe zadanie do bazy danych."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO zadania (opis, zrobione, priorytet) VALUES (?, ?, ?)",
                (opis, False, priorytet)
            )

            conn.commit()

    def pobierz_zadania(self):
        """Pobiera wszystkie zadania z bazy danych."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT id, opis, zrobione FROM zadania")
            return cursor.fetchall()

    def oznacz_jako_zrobione(self, id_zadania: int):
        """Oznacza zadanie o podanym ID jako zrobione."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE zadania SET zrobione = ? WHERE id = ?",
                (True, id_zadania)
            )

            conn.commit()

    def usun_zadanie(self, id_zadania: int):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute("DELETE FROM zadania WHERE id = ?", (id_zadania,))

            conn.commit()

    def wyszukiwanie_po_opisie(self, opis_zadania: str):
        szukana_fraza = f"%{opis_zadania}%"
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, opis, zrobione FROM zadania WHERE opis LIKE ?",
                (szukana_fraza,)
            )
            return cursor.fetchall()
    
    def edytuj_zadanie(self, id_zadania: int, nowy_opis: str):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute("UPDATE zadania SET opis = ? WHERE id = ?", (nowy_opis, id_zadania))

            conn.commit