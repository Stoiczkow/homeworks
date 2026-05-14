# bez 9
# lesson -> 1, 2, 3, 4, 5, 6
#7
# Wersja 1 – bez try...except, z użyciem .get()
def pobierz_wartosc(slownik, klucz):
    return slownik.get(klucz)  # zwraca None gdy ne istnieje

# Wersja 2 – z użyciem try...except KeyError
def pobierz_wartosc_v2(slownik, klucz):
    try:
        return slownik[klucz]
    except KeyError:
        return None

# Testowanie
dane = {"imie": "Anna", "wiek": 30, "miasto": "Kraków"}

print(pobierz_wartosc(dane, "imie"))    # Anna
print(pobierz_wartosc(dane, "hobby"))   # None

print(pobierz_wartosc_v2(dane, "wiek")) # 30
print(pobierz_wartosc_v2(dane, "auto")) # None
#8
class BladWalidacjiError(Exception):
    def __init__(self, bledy):
        self.bledy = bledy
        super().__init__(f"Błędy walidacji: {bledy}")


def waliduj_haslo(haslo):
    bledy = []

    if len(haslo) < 8:
        bledy.append("Hasło musi mieć co najmniej 8 znaków.")

    if not any(znak.isupper() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną wielką literę.")

    if not any(znak.islower() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną małą literę.")

    if not any(znak.isdigit() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną cyfrę.")

    znaki_specjalne = "!@#$%^&*"
    if not any(znak in znaki_specjalne for znak in haslo):
        bledy.append(f"Hasło musi zawierać co najmniej jeden znak specjalny ({znaki_specjalne}).")

    if bledy:
        raise BladWalidacjiError(bledy)

    return True


# Testowanie
hasla = ["abc", "poprawneHaslo1!", "bezCyfry!"]

for haslo in hasla:
    try:
        waliduj_haslo(haslo)
        print(f" Hasło '{haslo}' jest poprawne.")
    except BladWalidacjiError as e:
        print(f"\n Hasło '{haslo}' ma błędy:")
        for blad in e.bledy:
            print(f"   - {blad}")
#10
def sumuj_liczby_z_pliku():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    suma = 0
    przetworzone = 0
    pominiete = 0

    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            for numer_linii, linia in enumerate(plik, start=1):
                linia = linia.strip()
                try:
                    liczba = float(linia)
                    suma += liczba
                    przetworzone += 1
                except ValueError:
                    print(f"Linia {numer_linii}: '{linia}' – nie jest liczbą, pomijam.")
                    pominiete += 1

    except FileNotFoundError:
        print(f"Błąd: Plik '{nazwa_pliku}' nie istnieje!")

    finally:
        print(f"\nPodsumowanie:")
        print(f"Suma liczb:        {suma}")
        print(f"Linie przetworzone: {przetworzone}")
        print(f"Linie pominięte:    {pominiete}")


sumuj_liczby_z_pliku()