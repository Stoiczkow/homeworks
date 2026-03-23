# Zadanie 2 – Walidator wieku
# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie zmieniać wartości.

class Uzytkownik:
    def __init__(self, wiek):
        self.__wiek = wiek

    @property
    def wiek(self):
        return self.__wiek
    
    @wiek.setter
    def wiek(self, poprawny_wiek):
        if poprawny_wiek < 0:
            raise ValueError("Wiek nie może być ujemny")
        elif poprawny_wiek > 120:
            raise ValueError("Wiek jest za duży")
        else:
            self.__wiek = poprawny_wiek

u = Uzytkownik(20)

u.wiek = 35
print(u.wiek)
           
