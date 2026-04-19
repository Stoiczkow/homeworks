# Zadanie 9 – Funkcja do wyszukiwania produktów

# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich produktów w tej kategorii.

import sqlite3

def znajdz_produkty_w_kategorii(nazwa_kategorii): # Funkcja która przyjmuje nazwe kategorii

    Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
    cursor = Connection.cursor() # tworzenie obiektu kursora
    # musimy przy join uzyc tej pragmy

    cursor.execute('''
    SELECT p.nazwa_produktu, p.cena
    FROM Produkty p
    JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
    WHERE k.nazwa_kategorii = ?
    ''', (nazwa_kategorii,))

    result = cursor.fetchall() # pobranie wszystkich jako krotki

    Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
    Connection.close()

    return result

produkty = znajdz_produkty_w_kategorii("Elektronika") # wywołanie funkcji

print("Produkty w kategorii Elektronika:")

for nazwa, cena in produkty:
     print(f"{nazwa} - {cena} zł")