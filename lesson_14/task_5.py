"""
Zadanie 5 – Lista klientów
Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.
"""

from db import get_db

with get_db() as cursor:
    query = """
    SELECT 
        imie,
        email
    From Klienci
        
    """

    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(f"Imie: {row[0].split()[0]}, email: {row[1]}")