"""
Zadanie 9 – Funkcja do wyszukiwania produktów
Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
produktów w tej kategorii
"""

from db import get_db

def znajdz_produkty_w_kategorii(nazwa_kategorii: str) -> list:
    with get_db() as cursor:
        query = """
        SELECT
            Produkty.nazwa_produktu,
            Produkty.cena
        FROM Produkty
        INNER JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
        WHERE Kategorie.nazwa_kategorii = ?
        """

        cursor.execute(query, (nazwa_kategorii,))
        results = cursor.fetchall()

        return results

produkty = znajdz_produkty_w_kategorii('Elektronika')
for nazwa, cena in produkty:
    print(f"{nazwa}: {cena:.2f} zł")