class Uzytkownik:
    def __init__(self, wiek):
        self._wiek = None
        self.wiek = wiek

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, wartosc):
        if 0 <= wartosc <= 120:
            self._wiek = wartosc
        else:
            print("Blad: Wiek musi byc w zakresie od 0 do 120.")


u = Uzytkownik(25)
print(u.wiek)

u.wiek = 150
print(u.wiek)

u.wiek = 30
print(u.wiek)
