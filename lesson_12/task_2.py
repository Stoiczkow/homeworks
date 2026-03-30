# 2. ✏ Zadanie 2 – Walidator wieku
# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
# właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
# wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
# zmieniać wartości.
class Uzytkownik:
    def __init__(self, wiek):
        self._wiek = wiek

    @property
    def wiek(self):
        return self._wiek
            
    @wiek.setter
    def wiek(self, new_wiek):
        if 0 < new_wiek <= 120:
            self._wiek = new_wiek
        else:
            print("Błąd! Wiek musi być w przedziale 1-120")

user_1 = Uzytkownik(20)
print(user_1.wiek)
user_1.wiek = 80
user_1.wiek = 130
print(user_1.wiek)
    