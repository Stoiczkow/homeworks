# Zadanie 3 – Konwerter Walut
# Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.

class KalkulatorWalut:
    pass

    @staticmethod
    def usd_na_pln(usd):
        return usd * 4
    
wynik = KalkulatorWalut.usd_na_pln(4)

print(wynik)