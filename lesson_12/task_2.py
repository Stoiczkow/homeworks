# Zadanie 2 – Walidator wieku

class Uzytkownik:
    def __init__(self, wiek):
        self._wiek = wiek

    @property
    def wiek(self):
        return self._wiek
    
    @wiek.setter
    def wiek(self, age):
        if age > 0 and age < 120:
            self._wiek = age
        else:
            print("Wiek nie jest w zakresie 0 : 120")
    

user = Uzytkownik(20)
user.wiek = 89
print(user.wiek)