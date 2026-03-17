"""
Zadanie 6 – Produkty droższe od średniej
Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie
"""

from db import get_db

with get_db() as cursor:
    query = """
    SELECT
        nazwa_produktu,
        cena
    FROM 
        Produkty
    WHERE cena > (SELECT AVG(CENA) FROM Produkty)
    
    """

    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(f"{row[0]} : {row[1]:.2f} zł")