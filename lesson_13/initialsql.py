import sqlite3

connection = sqlite3.connect('kurs.db')

cursor = connection.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS miasta (
            id INTEGER PRIMARY KEY,
            nazwa TEXT NOT NULL,
            populacja INTEGER 
        );
    """
)

# pojedynczy rekord
# cursor.execute(
#     """
#         INSERT INTO miasta (nazwa, populacja)
#         VALUES (
#             ?, ?
#         );
#     """, 
#     (
#         "Warszawa", 
#         2000000
#     )
# )

# kilka rekordow na raz
# cities_to_add = [
#     ("Połock", 300001),
#     ("Kraków", 750000),
#     ("Gdańsk", 345000)
# ]

# cursor.executemany(
#     """
#         INSERT INTO miasta (nazwa, populacja)
#         VALUES (
#             ?, ?
#         );
#     """, cities_to_add
# )

cursor.execute(
    "SELECT * FROM miasta;"
)

all_cities = cursor.fetchall()
print(all_cities)


cursor.execute(
    """
        UPDATE miasta SET populacja = ?
        WHERE nazwa = ?
    """, (
        1000894, "Kraków"
    )
)


connection.commit()

print(f"Zmieniono: {cursor.rowcount} rekordów")
cursor.execute(
    """
    SELECT * FROM miasta
    WHERE nazwa = ?
    """,
    ("Kraków",)
)
print(f"Zmieniony rekord: {cursor.fetchone()}")

connection.close()