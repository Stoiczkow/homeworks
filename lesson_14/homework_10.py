# Prosta symulacja ORM
# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena. Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych, pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci, jak ORM automatyzuje mapowanie wierszy na obiekty.

import sqlite3

class Produkt ():
    def __init__(self,  id_produktu: int, nazwa_produktu: str, cena: float):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena

    def __repr__(self):
        return f"{self.id_produktu}. \"{self.nazwa_produktu}\" kosztuje {self.cena}"

def pobierz_wszystkie_produkty():
    produkt = []
    con = sqlite3.connect('sklep.db')

    c = con.cursor()

    c.execute('''
                select  id_produktu, nazwa_produktu, cena from  Produkty
                ''')
    
    tuple_list = c.fetchall()

    for tup in tuple_list:
        produkt.append(Produkt(*tup))   #unpacking

    con.close()

    return produkt

list_produkt = pobierz_wszystkie_produkty()

for prod in list_produkt:
    print(prod)


