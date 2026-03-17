import sqlite3
from contextlib import contextmanager

DB_FILE = 'sklep.db'

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_FILE)
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    finally:
        conn.close()