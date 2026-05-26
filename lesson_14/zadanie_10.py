import sqlite3


class Produkt:
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena

    def __repr__(self):
        return f"Produkt(id={self.id_produktu}, nazwa='{self.nazwa_produktu}', cena={self.cena})"


def pobierz_wszystkie_produkty():
    conn = sqlite3.connect('sklep.db')
    c = conn.cursor()

    c.execute("SELECT id_produktu, nazwa_produktu, cena FROM Produkty")
    wiersze = c.fetchall()
    conn.close()

    return [Produkt(id_p, nazwa, cena) for id_p, nazwa, cena in wiersze]


produkty = pobierz_wszystkie_produkty()
for produkt in produkty:
    print(produkt)
