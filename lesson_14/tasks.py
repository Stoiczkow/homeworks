#  ----- KOD STARTOWY DO ZADAŃ -----
# import sqlite3
# def przygotuj_baze():
# """Tworzy i wypełnia bazę danych na potrzeby zadań."""
# conn = sqlite3.connect('sklep.db') # Tworzy plik sklep.db
# cursor = conn.cursor()
# # Usunięcie tabel, jeśli istnieją, dla czystego startu
# cursor.execute("DROP TABLE IF EXISTS Zamowienia_Produkty")
# cursor.execute("DROP TABLE IF EXISTS Zamowienia")
# cursor.execute("DROP TABLE IF EXISTS Produkty")
# cursor.execute("DROP TABLE IF EXISTS Kategorie")
# cursor.execute("DROP TABLE IF EXISTS Klienci")
# # Tworzenie tabel
# cursor.execute('''
# CREATE TABLE Kategorie (
# id_kategorii INTEGER PRIMARY KEY,
# nazwa_kategorii TEXT UNIQUE NOT NULL
# )''')
# cursor.execute('''
# CREATE TABLE Produkty (
# id_produktu INTEGER PRIMARY KEY,
# nazwa_produktu TEXT NOT NULL,
# cena REAL NOT NULL,
# id_kategorii INTEGER,
# FOREIGN KEY (id_kategorii) REFERENCES Kategorie(id_kategorii)
# )''')
# cursor.execute('''
# CREATE TABLE Klienci (
# id_klienta INTEGER PRIMARY KEY,
# imie TEXT NOT NULL,
# email TEXT UNIQUE NOT NULL
# )''')
# cursor.execute('''
# CREATE TABLE Zamowienia (
# id_zamowienia INTEGER PRIMARY KEY,
# id_klienta INTEGER,
# data_zamowienia DATE,
# FOREIGN KEY (id_klienta) REFERENCES Klienci(id_klienta)
# )''')
# cursor.execute('''
# CREATE TABLE Zamowienia_Produkty (
# id_zamowienia INTEGER,
# id_produktu INTEGER,
# ilosc INTEGER NOT NULL,
# PRIMARY KEY (id_zamowienia, id_produktu),
# FOREIGN KEY (id_zamowienia) REFERENCES Zamowienia(id_zamowienia),
# FOREIGN KEY (id_produktu) REFERENCES Produkty(id_produktu)
# )''')
# # Wstawianie danych
# kategorie = [('Elektronika',), ('Książki',), ('Dom i ogród',)]
# klienci = [('Anna Nowak', 'anna.n@example.com'), ('Jan Kowalski',
# 'jan.k@example.com'), ('Zofia Wiśniewska', 'zofia.w@example.com')]
# produkty = [
# ('Laptop Pro', 5200.00, 1), ('Smartfon X', 2500.00, 1),
# ('Python dla każdego', 89.99, 2), ('Wzorce projektowe', 120.50, 2),
# ('Kosiarka elektryczna', 750.00, 3), ('Zestaw narzędzi', 300.00, 3),
# Zadania proste
# ('Słuchawki bezprzewodowe', 450.00, 1)
# ]
# zamowienia = [(1, '2023-10-01'), (2, '2023-10-02'), (1, '2023-10-05')]
# zamowienia_produkty = [(1, 1, 1), (1, 7, 1), (2, 3, 2), (3, 5, 1)]
# cursor.executemany("INSERT INTO Kategorie (nazwa_kategorii) VALUES (?)",
# kategorie)
# cursor.executemany("INSERT INTO Klienci (imie, email) VALUES (?,?)",
# klienci)
# cursor.executemany("INSERT INTO Produkty (nazwa_produktu, cena,
# id_kategorii) VALUES (?,?,?)", produkty)
# cursor.executemany("INSERT INTO Zamowienia (id_klienta, data_zamowienia)
# VALUES (?,?)", zamowienia)
# cursor.executemany("INSERT INTO Zamowienia_Produkty (id_zamowienia,
# id_produktu, ilosc) VALUES (?,?,?)", zamowienia_produkty)
# conn.commit()
# conn.close()
# print("Baza 'sklep.db' została przygotowana.")
# # Wywołaj funkcję, aby stworzyć bazę przed rozpoczęciem pracy
# przygotuj_baze()
# 1. ✏ Zadanie 1 – Liczba produktów
# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().
# (proste)
# 2. ✏ Zadanie 2 – Najdroższy produkt
# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX().
# (proste)
# 3. ✏ Zadanie 3 – Suma wartości
# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
# SUM() oraz klauzuli WHERE z JOIN.
# (proste)
# 4. ✏ Zadanie 4 – Średnia cena książki
# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().
# Zadania "challenge"
# (proste)
# 5. ✏ Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.
# (proste)
# 6. 🧠 Zadanie 6 – Produkty droższe od średniej
# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie.
# (challenge)
# 7. 🧠 Zadanie 7 – Zamówienia Anny Nowak
# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
# imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
# Zamowienia, Zamowienia_Produkty i Produkty.
# (challenge)
# 8. 🧠 Zadanie 8 – Kategorie z liczbą produktów
# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
# do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.
# (challenge)
# 9. 🧠 Zadanie 9 – Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii.
# (challenge)
# 10. 🧠 Zadanie 10 – Prosta symulacja ORM
# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.


# Zadanie 1 – Liczba produktów

# Policzenie liczby rekordów w tabeli Produkty.

# import sqlite3

# conn = sqlite3.connect("sklep.db")
# cursor = conn.cursor()

# cursor.execute("SELECT COUNT(*) FROM Produkty")
# wynik = cursor.fetchone()

# print("Liczba produktów:", wynik[0])

# conn.close()
# Zadanie 2 – Najdroższy produkt

# Znalezienie produktu z najwyższą ceną.

# import sqlite3

# conn = sqlite3.connect("sklep.db")
# cursor = conn.cursor()

# cursor.execute("""
# SELECT nazwa_produktu, cena
# FROM Produkty
# WHERE cena = (SELECT MAX(cena) FROM Produkty)
# """)

# produkt = cursor.fetchone()

# print("Najdroższy produkt:", produkt[0])
# print("Cena:", produkt[1])

# conn.close()
# Zadanie 3 – Suma wartości produktów z kategorii „Elektronika”
# import sqlite3

# conn = sqlite3.connect("sklep.db")
# cursor = conn.cursor()

# cursor.execute("""
# SELECT SUM(cena)
# FROM Produkty
# JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
# WHERE nazwa_kategorii = 'Elektronika'
# """)

# wynik = cursor.fetchone()

# print("Łączna wartość produktów Elektronika:", wynik[0])

# conn.close()
# Zadanie 4 – Średnia cena książki
# import sqlite3

# conn = sqlite3.connect("sklep.db")
# cursor = conn.cursor()

# cursor.execute("""
# SELECT AVG(cena)
# FROM Produkty
# JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
# WHERE nazwa_kategorii = 'Książki'
# """)

# wynik = cursor.fetchone()

# print("Średnia cena książek:", wynik[0])

# conn.close()
# Zadanie 5 – Lista klientów
# import sqlite3

# conn = sqlite3.connect("sklep.db")
# cursor = conn.cursor()

# cursor.execute("SELECT imie, email FROM Klienci")

# for klient in cursor.fetchall():
#     print(klient[0], "-", klient[1])

# conn.close()
# Zadanie 6 – Produkty droższe od średniej
# import sqlite3

# conn = sqlite3.connect("sklep.db")
# cursor = conn.cursor()

# cursor.execute("""
# SELECT nazwa_produktu, cena
# FROM Produkty
# WHERE cena > (SELECT AVG(cena) FROM Produkty)
# """)

# produkty = cursor.fetchall()

# for p in produkty:
#     print(p[0], "-", p[1])

# conn.close()
# Zadanie 7 – Zamówienia Anny Nowak
# import sqlite3

# conn = sqlite3.connect("sklep.db")
# cursor = conn.cursor()

# cursor.execute("""
# SELECT Produkty.nazwa_produktu
# FROM Klienci
# JOIN Zamowienia ON Klienci.id_klienta = Zamowienia.id_klienta
# JOIN Zamowienia_Produkty ON Zamowienia.id_zamowienia = Zamowienia_Produkty.id_zamowienia
# JOIN Produkty ON Zamowienia_Produkty.id_produktu = Produkty.id_produktu
# WHERE Klienci.imie = 'Anna Nowak'
# """)

# for produkt in cursor.fetchall():
#     print(produkt[0])

# conn.close()
# Zadanie 8 – Kategorie z liczbą produktów
# import sqlite3

# conn = sqlite3.connect("sklep.db")
# cursor = conn.cursor()

# cursor.execute("""
# SELECT Kategorie.nazwa_kategorii, COUNT(Produkty.id_produktu)
# FROM Kategorie
# LEFT JOIN Produkty ON Kategorie.id_kategorii = Produkty.id_kategorii
# GROUP BY Kategorie.nazwa_kategorii
# """)

# for row in cursor.fetchall():
#     print(row[0], "-", row[1])

# conn.close()
# Zadanie 9 – Funkcja wyszukiwania produktów w kategorii
# import sqlite3

# def znajdz_produkty_w_kategorii(nazwa_kategorii):
#     conn = sqlite3.connect("sklep.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     SELECT nazwa_produktu, cena
#     FROM Produkty
#     JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
#     WHERE nazwa_kategorii = ?
#     """, (nazwa_kategorii,))

#     wyniki = cursor.fetchall()
#     conn.close()

#     return wyniki


# print(znajdz_produkty_w_kategorii("Elektronika"))
# Zadanie 10 – Prosta symulacja ORM
# Klasa Produkt
# class Produkt:
#     def __init__(self, id_produktu, nazwa_produktu, cena):
#         self.id_produktu = id_produktu
#         self.nazwa_produktu = nazwa_produktu
#         self.cena = cena

#     def __repr__(self):
#         return f"{self.nazwa_produktu} ({self.cena} zł)"
# Funkcja pobierająca produkty
# import sqlite3

# def pobierz_wszystkie_produkty():
#     conn = sqlite3.connect("sklep.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT id_produktu, nazwa_produktu, cena FROM Produkty")

#     produkty = []
#     for row in cursor.fetchall():
#         produkt = Produkt(row[0], row[1], row[2])
#         produkty.append(produkt)

#     conn.close()
#     return produkty


# lista = pobierz_wszystkie_produkty()

# for p in lista:
#     print(p)