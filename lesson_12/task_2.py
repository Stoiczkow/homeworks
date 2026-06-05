'''
    Zadanie 2 - Walidator wieku

    Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
    właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
    wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
    zmieniać wartości
'''

class User:
    def __init__(self, wiek):
        self._wiek = wiek

    @property
    def wiek(self):
        print("Odczyt wieku....")
        return self._wiek
    
    @wiek.setter
    def wiek(self, nowa_wartosc):
        if nowa_wartosc >= 0 and nowa_wartosc <= 120:
            print("Zapisano nową wartość...")
            self._wiek = nowa_wartosc
        else:
            print("Nowa wartość musi mieścić się w zakresie od 0 do 120")    
    
jan = User(35)

# Odczyt 1
print(f"Wiek Jana: {jan.wiek}")

jan.wiek = 48
jan.wiek = 121

# Odczyt 2 
print(f"Wiek Jana: {jan.wiek}")