# TASK 1

# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().

import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute('SELECT COUNT(*) FROM produkty')

result = cursor.fetchone()

print(result)

conn.commit()
conn.close()