import sqlite3


class TaskManagerRaw:
    def __init__(self, db_path='todo_raw.db'):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS zadania (
                    id INTEGER PRIMARY KEY,
                    opis TEXT NOT NULL,
                    zrobione INTEGER DEFAULT 0,
                    priorytet INTEGER DEFAULT 1
                )
            ''')
            conn.commit()

    def pokaz_zadania(self):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                "SELECT id, opis, zrobione, priorytet FROM zadania"
            ).fetchall()

    def dodaj_zadanie(self, opis, priorytet=1):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO zadania (opis, priorytet) VALUES (?, ?)",
                (opis, priorytet)
            )
            conn.commit()

    def oznacz_jako_zrobione(self, id_zadania):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE zadania SET zrobione = 1 WHERE id = ?",
                (id_zadania,)
            )
            conn.commit()

    def usun_zadanie(self, id_zadania):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "DELETE FROM zadania WHERE id = ?",
                (id_zadania,)
            )
            conn.commit()

    def edytuj_zadanie(self, id_zadania, nowy_opis):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE zadania SET opis = ? WHERE id = ?",
                (nowy_opis, id_zadania)
            )
            conn.commit()

    def wyszukaj_zadania(self, fraza):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                "SELECT id, opis, zrobione, priorytet FROM zadania WHERE opis LIKE ?",
                (f'%{fraza}%',)
            ).fetchall()
