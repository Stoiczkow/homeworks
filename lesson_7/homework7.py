# bez 7 i 9
# lesson - 1, 2, 3, 4
#5
from functools import reduce

liczby = [1, 2, 3, 4, 5]

iloczyn = reduce(lambda x, y: x * y, liczby)

print(iloczyn)
#6
def stworz_licznik():
    licznik = 0
    
    def licznik_wewnetrzny():
        nonlocal licznik  # sięga do zmiennej z zewnętrznej funkcji
        licznik += 1
        return licznik
    
    return licznik_wewnetrzny

licznik = stworz_licznik()
print(licznik())  # 1
print(licznik())  # 2
print(licznik())  # 3
#8
liczby = [-3, -1, 0, 2, 4, 6]

wynik = list(map(lambda x: x**2, filter(lambda x: x > 0, liczby)))
print(wynik)

#10
uzytkownicy = [
{"imie": "Jan", "wiek": 30, "aktywny": True},
{"imie": "Anna", "wiek": 17, "aktywny": False},
{"imie": "Piotr", "wiek": 25, "aktywny": True}
]

aktywni = [i["imie"].upper() for i in uzytkownicy if i["aktywny"] == True and i["wiek"]>18]
print(aktywni)