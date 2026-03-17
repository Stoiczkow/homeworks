"""
Zadanie 8 – Kategorie z liczbą produktów
Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.
"""

from db import get_db

with get_db() as cursor:
    query = """
    SELECT 
        Kategorie.nazwa_kategorii,
        COUNT(Produkty.id_produktu) AS liczba_produktow
    
    FROM Kategorie
    INNER JOIN Produkty ON Kategorie.id_kategorii = Produkty.id_kategorii
    GROUP BY Kategorie.nazwa_kategorii
    """

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"{row[0]}: {row[1]}")
