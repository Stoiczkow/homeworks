# Prosta symulacja ORM
# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.

import sqlite3
class Products:
    def __init__(self, id_products, product_name, price):
        self.id_products = id_products
        self.product_name = product_name
        self.price = price

def download_all_products():
    connection = sqlite3.connect('sklep.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    query = "SELECT id_products, product_name, price FROM Products"
    cursor.execute(query)
    result = cursor.fetchall()

    all_products = [Products(id_products, product_name, price) for id_products, product_name, price in result]

    connection.commit()
    connection.close()

    return all_products
