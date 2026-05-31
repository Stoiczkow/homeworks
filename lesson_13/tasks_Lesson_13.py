import sqlite3

#1
conn = sqlite3.connect("biblioteka.db")

c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER
            )
""")
#2
new_books = [
  ("Diuna", "Frank Herbert", 1965),
  ("Folwark zwierzecy", "George Orwell", 1943),
  ("Hrabia Monte Christo", "Aleksandra Dumasa", 1844)
]

c.executemany("INSERT INTO books (title, author,publication_year) VALUES (?, ?, ?)", new_books)

#3

c.execute("SELECT * FROM books")
download = c.fetchall()

for book in download:
    print(book)

#4
favorite_author = ("Aleksandra Dumasa",)

c.execute("SELECT * FROM books WHERE author = ?", favorite_author)
download = c.fetchone()
print(f"Favorite author and his book:\n{download}")

#5

c.execute("UPDATE books SET publication_year = ? WHERE title = ?", (1845, "Hrabia Monte Christo",))

c.execute("SELECT * FROM books WHERE title = ?", ("Hrabia Monte Christo",))
download = c.fetchone()
print(f"After changes:\n{download}")
conn.commit()

c.close()




import sqlite3

#6
conn = sqlite3.connect("uczelnia.db")

c = conn.cursor()

c.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id_student INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                UNIQUE(name, surname)
          )
""")

c.execute("""
            CREATE TABLE IF NOT EXISTS auditoriums(
                id_auditorium INTEGER PRIMARY KEY,
                building_name TEXT NOT NULL,
                room_number INTEGER UNIQUE
          )
""")
#7
new_students = [
    ("Jan", "Kowalski"),
    ("Anna", "Kowalska"),
    ("Janusz", "Nowak"),
    ("Mateusz", "Kwasniewski"),
    ("Tomasz", "Kot")
]

# c.executemany("INSERT INTO students (name, surname) VALUES (?, ?)",new_students)

new_auditoriums = [
    ("Seminar Hall", 11),
    ("Seminar Hall", 23),
    ("Assembly hall", 9)
]

# c.executemany("INSERT INTO auditoriums (building_name, room_number) VALUES (?, ?)",new_auditoriums)

#8
c.execute("""
        CREATE TABLE IF NOT EXISTS assignments(
          ID_assignments INTEGER PRIMARY KEY,
          id_students INTEGER,
          id_auditorium INTEGER,
          FOREIGN KEY (id_students) REFERENCES students (id_student),
          FOREIGN KEY (id_auditorium) REFERENCES auditoriumS (id_auditorium)
          )
          """)

#9

create_assignments = [
    (1, 2),
    (2, 3),
    (3, 2),
    (4, 3),
    (5, 1)
]

#10

# c.executemany("INSERT INTO assignments (id_students, id_auditorium) VALUES (?, ?)", create_assignments)


c.execute("""SELECT s.name, s.surname, a.building_name, a.room_number
FROM assignments asg
JOIN students s ON asg.id_assignments = s.id_student
JOIN auditoriums a ON asg.id_auditorium = a.id_auditorium
""")

download = c.fetchall()
for x in download:
    full_name = f"{x[0]} {x[1]}" 
    print(f"{full_name:<25} {x[2]:<15} {x[3]}")


conn.commit()

c.close()