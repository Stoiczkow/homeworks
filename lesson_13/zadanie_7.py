import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

studenci = [
    ('Jan', 'Kowalski'),
    ('Anna', 'Nowak'),
    ('Piotr', 'Wisniewski'),
    ('Maria', 'Wojcik'),
]
c.executemany("INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)", studenci)

audytoria = [
    ('Budynek A', 101),
    ('Budynek B', 205),
    ('Budynek C', 312),
]
c.executemany("INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)", audytoria)

conn.commit()
print("Dodano studentow i audytoria.")

conn.close()
