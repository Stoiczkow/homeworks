# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.
import sqlite3

class Produkt:
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena
    
    def __str__(self):
        return f"{self.nazwa_produktu}"

def pobierz_wszystkie_produkty() -> list[Produkt]:

    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()

    cursor.execute(f'''SELECT id_produktu, nazwa_produktu, cena FROM produkty''')

    result = cursor.fetchall()

    products_list = []

    for i in result:
        products_list.append(Produkt(i[0], i[1], i[2]))

    conn.commit()
    conn.close()

    return products_list

# Przykład użycia:

produkty = pobierz_wszystkie_produkty()

for i in produkty:
    print(f"Nazwa produktu: {i}, ID: {i.id_produktu}")