'''
    Zadanie 3 - Konwerter Walut

    Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
    usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
    stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.
'''

class KalkulatorWalut:
    @staticmethod
    def usd_na_pln(kwota_usd):
        kurs = 4.0
        return kwota_usd * kurs


wynik = KalkulatorWalut.usd_na_pln(10)

print(f"Wynik: {wynik}") 
