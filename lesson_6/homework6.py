# lessons -> done 1, 2, 3
# 4
def oblicz_srednia(*args: float) -> float:
    if not args:  # jeśli nie podano żadnych argumentów
        return 0
    return sum(args) / len(args)

# 5
# zmienna globalna
POZIOM_DOSTEPU = "user"

def zmien_poziom():
    # zmienna lokalna o tej samej nazwie (NIE używamy global)
    POZIOM_DOSTEPU = "admin"
    print("Wewnątrz funkcji:", POZIOM_DOSTEPU)

# sprawdzenie
print("Przed wywołaniem funkcji:", POZIOM_DOSTEPU)

zmien_poziom()

print("Po wywołaniu funkcji:", POZIOM_DOSTEPU)

# 6
def wielokrotne_powitanie(imie: str, ilosc: int) -> None:
    print((f"Cześć, {imie}!\n") * ilosc)

def wielokrotne_powitanie2(imie: str, ilosc: int) -> None:
    for _ in range(ilosc):
        print(f"Cześć, {imie}!")

wielokrotne_powitanie("JACEK", 4)

# 7
def analiza_listy(lista: list[int]):
    minimum = min(lista)
    maksimum = max(lista)
    suma = sum(lista)
    slownik = {"min": minimum, "max":maksimum, "sum": suma}
    print(slownik)
    krotka = (minimum, maksimum, suma)
    print("krotka:", krotka)

lista=[1,2,3,4,5,6]
analiza_listy(lista)

# 7 faster way:
def min_max_sum(lista: list[int]):
    return min(lista), max(lista), sum(lista)
  # zwraca krotkę

wynik = min_max_sum(lista)
print(wynik)

# 8
def stworz_profil(imie: str, **dane_dodatkowe):
    imie=imie
    slownik = {"imie":imie}
    for klucz, wartosc in dane_dodatkowe.items():
        slownik[klucz] = wartosc
    
    return slownik
profil = stworz_profil("Jan", wiek=30, miasto="Warszawa")
print(profil)
# 9
def silnia(n:int):
    t = 1
    while n > 0:
        t*=n
        n-=1
    return t
print(silnia(5))
# rekurencyjnie
def silnia(n: int) -> int:
    if n == 0 or n == 1:  # warunek stopu
        return 1
    return n * silnia(n - 1)

print(silnia(5))  # 120


# 10
duza_litera = ["A", "B", "C", "D"]
cyfra = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

def sprawdz_haslo() -> bool:
    while True:
        haslo: str = input("Podaj hasło: ")
        
        if len(haslo) < 8:
            print("Hasło musi mieć min. 8 znaków, spróbuj ponownie")
        elif not any(znak in duza_litera for znak in haslo):
            print("Użyj dużej litery (A-D), spróbuj ponownie")
        elif not any(znak in cyfra for znak in haslo):
            print("Uzupełnij o cyfrę, spróbuj ponownie")
        else:
            print("Hasło jest poprawne!")
            return True

sprawdz_haslo()