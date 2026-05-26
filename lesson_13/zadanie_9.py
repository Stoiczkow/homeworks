import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

c.execute("SELECT id_studenta FROM studenci")
studenci = c.fetchall()

c.execute("SELECT id_audytorium FROM audytoria")
audytoria = c.fetchall()

przypisania = []
for i, (id_studenta,) in enumerate(studenci):
    id_audytorium = audytoria[i % len(audytoria)][0]
    przypisania.append((id_studenta, id_audytorium))

c.executemany(
    "INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)",
    przypisania
)

conn.commit()
print("Dokonano przypizan studentow do audytoriow.")

conn.close()
