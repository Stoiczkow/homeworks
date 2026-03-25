# Zadanie 9 – Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii.

import sqlite3


def znajdz_produkty_w_kategorii(nazwa_kategorii):
    connection = sqlite3.connect("sklep.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    query = """
        SELECT p.nazwa_produktu, p.cena
        FROM Produkty AS p
        JOIN Kategorie AS k
            ON p.id_kategorii = k.id_kategorii
        WHERE k.nazwa_kategorii = ?
    """

    cursor.execute(query, (nazwa_kategorii,))
    result = cursor.fetchall()
    connection.close()
    return result


if __name__ == "__main__":
    produkty = znajdz_produkty_w_kategorii("Elektronika")
    for produkt in produkty:
        print(produkt)
