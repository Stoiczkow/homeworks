# Zadanie 9 – Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich produktów w tej kategorii.
import sqlite3
path = 'homeworks/lesson_14/'

def znajdz_produkty_w_kategorii(nazwa_kategorii: str) -> list[tuple[str, float]]:

    conn = sqlite3.connect(path+'sklep.db')
    c = conn.cursor()

    c.execute('''
    select p.nazwa_produktu, p.cena from Kategorie k JOIN Produkty p on p.id_kategorii = k.id_kategorii  WHERE k.nazwa_kategorii = ?;
    ''', (nazwa_kategorii, ))
    tup = c.fetchall()

    conn.close()
    return tup


tup = znajdz_produkty_w_kategorii("Elektronika")

print(f"obiekt {tup}")

for nazwa_produktu, cena in tup:
    print(f"Produkt \"{nazwa_produktu}\" ma cenę: {cena}")

