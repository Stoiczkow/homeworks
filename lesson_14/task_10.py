"""
Zadanie 10 – Prosta symulacja ORM
Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
jak ORM automatyzuje mapowanie wierszy na obiekty.
"""

from db import get_db


class Produkt:
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena

    def __repr__(self):
        return f"Produkt(id={self.id_produktu}, nazwa='{self.nazwa_produktu}', cena={self.cena:.2f} zł)"

def pobierz_wszystkie_produkty():
    with get_db() as cursor:
        query = """
        SELECT 
            id_produktu, 
            nazwa_produktu, 
            cena 
        FROM Produkty
        """

        cursor.execute(query)
        result = cursor.fetchall()

        products = [Produkt(row[0], row[1], row[2]) for row in result]

        return products

all_products = pobierz_wszystkie_produkty()

for produkt in all_products:
    print(produkt)


