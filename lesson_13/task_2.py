import sqlite3
import random

conn = sqlite3.connect('uczelnia.db')
cursor = conn.cursor()

# zadanie 6
cursor.execute("""
CREATE TABLE IF NOT EXISTS studenci (
    id_studenta INTEGER PRIMARY KEY,
    imie TEXT,
    nazwisko TEXT
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS audytoria (
    id_audytorium INTEGER PRIMARY KEY,
    nazwa_budynku TEXT,
    numer_sali INTEGER
    );
""")

# zadanie 7
students_data = [
    ("Adam", "Nowak"),
    ("Jerzy", "Urban"),
    ("Bartek", "Kowalski"),
    ("Adrian", "Nowakowski")
]

audytoria_data = [
    ("Nowa Kreślarnia", 112),
    ("Kotłownia", 999),
    ("Gmach Główny", 100)
]

# cursor.executemany("""
#                         INSERT INTO studenci (imie, nazwisko) VALUES (?,?)
#                    """, students_data)
#
# cursor.executemany("""
#                         INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?,?)
#                    """, audytoria_data)

# zadanie 8
cursor.execute("""
CREATE TABLE IF NOT EXISTS przypisania (
    id_przypisania INTEGER PRIMARY KEY,
    id_studenta INTEGER,
    id_audytorium INTEGER,
    FOREIGN KEY (id_studenta) REFERENCES studenci (id_studenta),
    FOREIGN KEY (id_audytorium) REFERENCES audytoria (id_audytorium)
    );
""")

# # zadanie 9
# cursor.execute("""SELECT * FROM studenci;""")
# students_fetch = cursor.fetchall()
#
# cursor.execute("""SELECT * FROM audytoria;""")
# audytoria_fetch = cursor.fetchall()
#
# for student in students_fetch:
#     student_id = student[0]
#     audytoria_id = random.choice(audytoria_fetch)[0]
#
#     cursor.execute("""
#                     INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?);
#                     """, (student_id, audytoria_id)
#                    )
#
#     conn.commit()
#     conn.close()

# zadanie 10
def znajdz_sale_studenta(nazwisko):
    conn = sqlite3.connect('uczelnia.db')
    cursor = conn.cursor()

    querry = """
        SELECT s.nazwisko, a.nazwa_budynku, a.numer_sali
        FROM studenci s
        JOIN przypisania p ON s.id_studenta = p.id_studenta
        JOIN audytoria a ON p.id_audytorium = a.id_audytorium
        WHERE s.nazwisko = ?;
    """

    cursor.execute(querry, (nazwisko,))
    results = cursor.fetchall()

    if results:
        print(f"Student: {results[0][0]}, znajduje się w budynku: {results[0][1]}, sala nr {results[0][2]}")
    else:
        print(f"Nie odnaleziono studenta o nazwisku {nazwisko}")

    conn.close()

znajdz_sale_studenta("Nowak")

conn.commit()
conn.close()