import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS studenci (
        id_studenta INTEGER PRIMARY KEY,
        imie TEXT NOT NULL,
        nazwisko TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS audytoria (
        id_audytorium INTEGER PRIMARY KEY,
        nazwa_budynku TEXT NOT NULL,
        numer_sali INTEGER NOT NULL
    )
''')

conn.commit()
print("Tabele 'studenci' i 'audytoria' zostaly utworzone.")

conn.close()
