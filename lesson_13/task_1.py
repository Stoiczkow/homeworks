import sqlite3

conn = sqlite3.connect('biblioteka.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ksiazki (
    id INTEGER PRIMARY KEY,
    tytul TEXT NOT NULL,
    autor TEXT NOT NULL,
    rok_wydania INTEGER
);
""")

add_books = [
    ("Potop", "Henryk Sienkiewicz", 1800),
    ("Pan Tadeusz", "Adam Mickiewicz", 1850),
    ("Harry Potter", "J.K. Rowling", 2000)
]

# cursor.executemany("""
#                         INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?,?,?)
#                    """, add_books)

# cursor.execute("""
#                 SELECT * FROM ksiazki
#                """)

# cursor.execute("""
#                 SELECT * FROM ksiazki WHERE autor = 'Henryk Sienkiewicz';
#                 """)

cursor.execute("""
                UPDATE ksiazki SET rok_wydania = ? WHERE id = ?
               """, (2002, 3)
               )
cursor.execute("""
                SELECT * FROM ksiazki WHERE id = 3;
                """
               )

all_books = cursor.fetchall()
print(all_books)



conn.commit()
conn.close()