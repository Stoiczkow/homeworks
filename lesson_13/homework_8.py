# Zadanie 8 – Połącz tabele (Relacja)
# To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej samej bazie uczelnia.db. Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w tabeli studenci .
# id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli audytoria .

path = 'homeworks/lesson_13/'

import sqlite3

conn = sqlite3.connect(path+'uczelnia.db')
c = conn.cursor()

# włączenie referencji
c.execute("PRAGMA foreign_keys = ON")

c.execute(
    '''
CREATE TABLE IF NOT EXISTS przypisania (
    id_przypisania INTEGER PRIMARY KEY,
    id_studenta INTEGER,
    id_audytorium INTEGER,
    FOREIGN KEY (id_studenta) REFERENCES studenci(id_studenta),
    FOREIGN KEY (id_audytorium) REFERENCES audytoria(id_audytorium)
)
''')

conn.commit()

conn.close()

