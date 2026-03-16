# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii

import sqlite3

def znajdz_produkty_w_kategorii(nazwa_kategorii: str) -> list[tuple[str, float]]:

    conn = sqlite3.connect('sklep.db')
    cursor = conn.cursor()

    cursor.execute(f'''SELECT nazwa_produktu, cena FROM produkty as p
                    JOIN kategorie as k ON k.id_kategorii = p.id_kategorii
                    WHERE k.nazwa_kategorii = ?
                    ''', (nazwa_kategorii, ))

    result = cursor.fetchall()
    print(result)

    conn.commit()
    conn.close()

# Przykład użycia

znajdz_produkty_w_kategorii("Dom i ogród")