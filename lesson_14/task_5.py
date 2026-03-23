import sqlite3

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

# task 5
sql_query = "SELECT imie, email FROM Klienci"

cursor.execute(sql_query)

result = cursor.fetchall()

for index, user in enumerate(result, start=1):
    print(f"{index} - {user}")

connection.commit()
connection.close()