import sqlite3


def znajdz_produkty_w_kategorii(nazwa_kategorii):
    conn = sqlite3.connect('sklep.db')
    c = conn.cursor()

    c.execute('''
        SELECT p.nazwa_produktu, p.cena
        FROM Produkty p
        JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
        WHERE k.nazwa_kategorii = ?
    ''', (nazwa_kategorii,))

    wyniki = c.fetchall()
    conn.close()
    return wyniki


produkty = znajdz_produkty_w_kategorii('Elektronika')
for nazwa, cena in produkty:
    print(f"{nazwa}: {cena} zl")
