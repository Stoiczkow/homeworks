"""
Zadanie 1 – Liczba produktów
Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
tabeli Produkty. Użyj funkcji COUNT().
"""

from db import get_db

with get_db() as cursor:
    query = """
    SELECT
        COUNT(id_produktu) as liczba_produktow
    FROM produkty
    """

    cursor.execute(query)
    result = cursor.fetchone()

    print(f'Number of products: {result[0]}')
