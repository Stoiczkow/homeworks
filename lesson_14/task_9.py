# Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii.

import sqlite3

def search_prod_in_category(category_name):
    connection = sqlite3.connect('sklep.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    query = """
            SELECT p.product_name, p.price FROM Products AS p
            JOIN Categories AS k
                ON k.id_category = p.id_category
            WHERE k.category_name = ?
    """

    cursor.execute(query, (category_name,))
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result