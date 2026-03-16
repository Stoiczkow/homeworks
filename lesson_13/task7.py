# 🧠 Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
# najmniej 4 studentów i 3 audytoria

import sqlite3

connection = sqlite3.connect('uczelnia.db')
cursor = connection.cursor()

studenci = [("Krzysztof", "Waszczykowski"),
            ("Anna", "Kalemba"),
            ("Grzegorz", "Przykładowy"),
            ("Karolina", "Testowa")]

audytoria = [("Instytut Filologiczny", 24),
            ("Insytyut Geograficzny", 46),
            ("Collegium Novum", 32)]

cursor.executemany('''
                INSERT INTO studenci (imie, nazwisko) VALUES (?, ?);
                ''', studenci)

cursor.executemany('''
                INSERT INTO audytorium (nazwa_budynku, numer_sali) VALUES (?, ?);
                ''', audytoria)

connection.commit()
connection.close()