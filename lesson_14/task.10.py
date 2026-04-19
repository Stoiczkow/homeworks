import sqlite3

class Produkt:   # stworzenie klasy produkt z obiektami 
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

def pobierz_wszystkie_rzeczy():
    Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
    cursor = Connection.cursor() # tworzenie obiektu kursora
    # musimy przy join uzyc tej pragmy

    cursor.execute("SELECT id_produktu, nazwa_produktu, cena FROM Produkty")

    result = cursor.fetchall() # lista krotek

# Tworzenie obiektów, bierzmy dane z bazy, tworzymy obiekt, dodajmy go do listy
    lista = []
    for id, nazwa, cena in result:
        lista.append(Produkt(id, nazwa, cena))

    Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
    Connection.close()

    return lista # zwrócenie listy

# wywołanie funkcji 
Produkty = pobierz_wszystkie_rzeczy() # pobranie wszystkich produktów do produkty

for p in Produkty:
    print(p.id, "-", p.nazwa, "-", p.cena, "zł") # wypisanie z kalsy obiektw
