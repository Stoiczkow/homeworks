# Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co najmniej 4 studentów i 3 audytoria.



path = 'homeworks/lesson_13/'

import sqlite3

conn = sqlite3.connect(path+'uczelnia.db')


c = conn.cursor()

students = [
    (1024, 'Gall',  'Anonim'),
    (2048, 'Mieszko', 'I'),
    (4096, 'Bolesław', 'Chrobry'),
    (8192, 'Mieszko', "II")
 ]

c.executemany('''
    insert into studenci (id_studenta, imie, nazwisko) values (?, ?, ?)
''', students
)

c.executemany('''
    insert into audytoria values(?, ?, ?)
''', 
[
    (102, 'Aula', '404'),
    (123, 'Hala duża', '246'),
    (691, 'Czytelnia', '555')
    ])

conn.commit()

conn.close()
