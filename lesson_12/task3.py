# Zadanie 3 – Konwerter Walut
# Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.

# Dodać metode statyczną zwykła metoda zdefiniowana w klasie

# Służy on do tworzenia metody statycznej, czyli takiej, która:
# nie ma dostępu ani do instancji (self), ani do klasy (cls),
# działa jak zwykła funkcja, ale jest logicznie powiązana z klasą.

class KalkulatorWalut:

# stworzenie staticmethod
    @staticmethod
    def usd_na_pln(usd):
        return usd / 4.0
    
# wywołanie metody bez tworzenia obiektu
print(KalkulatorWalut.usd_na_pln(20))

