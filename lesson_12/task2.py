# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
# właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
# wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
# zmieniać wartości.

class Uzytkownik:
    def __init__(self):
        self._wiek = None
    
    @property
    def return_wiek(self):
        return self._wiek
    
    @return_wiek.setter
    def set_wiek(self, age):
        if age > 0 and age < 120:
            self._wiek = age
        else:
            print("Wiek poza skalą")
        

user1 = Uzytkownik()
print(user1.return_wiek)
user1.set_wiek = 30
print(user1.return_wiek)
