"""
Zadanie 3 – Suma wartości
Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
SUM() oraz klauzuli WHERE z JOIN
"""

from db import get_db

with get_db() as cursor:
    query = """
    SELECT 
        SUM(Produkty.cena) AS laczna_wartosc
    FROM 
        Produkty
    INNER JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
    WHERE Kategorie.nazwa_kategorii = 'Elektronika'
    """

    cursor.execute(query)
    result = cursor.fetchone()

    print(result)
