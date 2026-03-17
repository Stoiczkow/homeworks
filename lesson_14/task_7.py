"""
Zadanie 7 – Zamówienia Anny Nowak
Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
Zamowienia, Zamowienia_Produkty i Produkty.
"""

from db import get_db

with get_db() as cursor:
    query = """
    SELECT 
        Produkty.nazwa_produktu
    FROM 
        Klienci
    INNER JOIN Zamowienia ON Klienci.id_klienta = Zamowienia.id_klienta
    INNER JOIN Zamowienia_Produkty ON Zamowienia.id_zamowienia = Zamowienia_produkty.id_zamowienia
    INNER JOIN Produkty ON Zamowienia_produkty.id_produktu = Produkty.id_produktu
    
    WHERE Klienci.imie = 'Anna Nowak'
    """


    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"{row[0]}")
