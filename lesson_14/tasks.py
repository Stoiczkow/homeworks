import sqlite3

#  Zadanie 1 – Liczba produktów
# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().
# (proste)

connection = sqlite3.connect('sklep.db')
cursor = connection.cursor()

cursor.execute("""
                SELECT COUNT(id_produktu) as liczba_wszystkich_produktów FROM Produkty
               """)

print(cursor.fetchone())

# 2. ✏ Zadanie 2 – Najdroższy produkt
# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX().
# (proste)

cursor.execute("""
                SELECT MAX(cena), nazwa_produktu FROM Produkty
               """)

print(cursor.fetchone())

# 3. ✏ Zadanie 3 – Suma wartości
# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
# SUM() oraz klauzuli WHERE z JOIN.
# (proste)

cursor.execute("""
                SELECT SUM(cena) FROM Produkty AS p JOIN Kategorie as k ON p.id_kategorii = k.id_kategorii
                WHERE k.nazwa_kategorii = "Elektronika"
               """)

print(cursor.fetchone())

# 4. ✏ Zadanie 4 – Średnia cena książki
# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().

cursor.execute("""
                SELECT AVG(cena) FROM Produkty AS p JOIN Kategorie as k ON p.id_kategorii = k.id_kategorii
                WHERE k.nazwa_kategorii = "Książki"
               """)
print(cursor.fetchone())

#  Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.

cursor.execute("""
                SELECT imie, email FROM Klienci
               """)
print(cursor.fetchall())

# Zadanie 6 – Produkty droższe od średniej
# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie.
# (challenge)

cursor.execute("""
                SELECT nazwa_produktu, cena FROM Produkty WHERE
                cena > (SELECT AVG(cena) FROM Produkty)
               """)

expensive_products = cursor.fetchall()

print("\nProdukty, których cena jest wyższa niż średnia cena wszystkich produktów w sklepie to:")

for name, price in expensive_products:
    print(f"{name}, cena {price}")

# 7. 🧠 Zadanie 7 – Zamówienia Anny Nowak
# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
# imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
# Zamowienia, Zamowienia_Produkty i Produkty.
# (challenge)

client = 'Anna Nowak'

cursor.execute("""
               SELECT nazwa_produktu from Produkty as p
               JOIN Zamowienia_Produkty as zm 
               ON p.id_produktu = zm.id_produktu 
               JOIN Zamowienia as z
               ON z.id_zamowienia = zm.id_zamowienia
               JOIN Klienci as k
               ON k.id_klienta = z.id_klienta
               WHERE k.imie = ?
               """, (client,))

print(f"\nProdukty zakupione przez klienta {client}:")
client_products = cursor.fetchall()

for product in client_products:
    print(product[0])

# 8. 🧠 Zadanie 8 – Kategorie z liczbą produktów
# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
# do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.
# (challenge)

print("\nLiczba produktów w poszczególnych kategoriach: ")

cursor.execute("""
                SELECT nazwa_kategorii, COUNT(id_produktu) 
                FROM Produkty as p 
                JOIN Kategorie as k 
                ON p.id_kategorii = k.id_kategorii
                GROUP BY p.id_kategorii
               """)

categories_amount = cursor.fetchall()

for category_name, amount in categories_amount:
    print(f"Kategoria {category_name} posiada {amount} produktów")

# 9. 🧠 Zadanie 9 – Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii.
# (challenge)

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    cursor.execute("""
                SELECT nazwa_produktu, cena
                FROM Produkty as p 
                JOIN Kategorie as k 
                ON p.id_kategorii = k.id_kategorii
                WHERE nazwa_kategorii = ?
               """, (nazwa_kategorii,))
    
    return cursor.fetchall()

selected_category = "Elektronika"

category_products = znajdz_produkty_w_kategorii(selected_category)

print(f"\nProdukty w kategorii {selected_category} to:")

for product in category_products:
    print(product[0])

# 10. 🧠 Zadanie 10 – Prosta symulacja ORM
# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.

class Produkt:
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena

    def __str__(self):
        return f"Id produktu: {self.id_produktu}, nazwa: {self.nazwa_produktu}, cena: {self.cena}"
    


def pobierz_wszystkie_produkty():
    cursor.execute("""
                SELECT id_produktu, nazwa_produktu, cena
                FROM Produkty 
                """)
    products_raw = cursor.fetchall()
    products = []

    for p_id, p_name, p_price in products_raw:
        products.append(Produkt(p_id, p_name, p_price))

    return products

products_objects = pobierz_wszystkie_produkty()

print("\nLista produktów - obiektów klasy Produkt: ")
for product in products_objects:
    print(product)



connection.commit()
connection.close()