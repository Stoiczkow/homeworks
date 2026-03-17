"""
Zadanie 4 – Średnia cena książki
Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG()
"""

from db import get_db

with get_db() as cursor:
    query = """
    SELECT 
        AVG(cena) as avg_cena
    FROM 
        produkty
    INNER JOIN kategorie ON produkty.id_kategorii = kategorie.id_kategorii
    WHERE kategorie.nazwa_kategorii = 'Książki'
    
    """


    cursor.execute(query)
    result = cursor.fetchone()

    print(result)
