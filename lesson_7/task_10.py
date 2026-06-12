'''
Mini-projekt: Przetwarzanie danych: Masz listę słowników reprezentujących
użytkowników:
Napisz jednolinijkowy kod (używając kombinacji filter , map lub list comprehension),
który zwróci listę imion aktywnych użytkowników, którzy mają 18 lat lub więcej, pisanych
wielkimi literami
'''

uzytkownicy = [
    {"imie": "Anna", "wiek": 22, "aktywny": True},
    {"imie": "Piotr", "wiek": 17, "aktywny": True},
    {"imie": "Kasia", "wiek": 30, "aktywny": False},
    {"imie": "Jan", "wiek": 19, "aktywny": True}
]

wynik = [u["imie"].upper() for u in uzytkownicy if u["aktywny"] and u["wiek"] >= 18]

print(wynik)
