"""
Zadanie 2 – Najdroższy produkt
Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
MAX()
"""

from db import get_db

with get_db() as cursor:
    query = """
    SELECT MAX(cena) as max_cena
    FROM produkty
    
    """

    cursor.execute(query)
    result = cursor.fetchone()

    print(result[0])
