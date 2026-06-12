'''
Walidator wieku: Stwórz funkcję rejestruj_uzytkownika(wiek) , która rzuca własnym,
zdefiniowanym przez Ciebie wyjątkiem WiekNiepoprawnyError , jeśli wiek jest mniejszy niż
'''

class WiekNiepoprawnyError(Exception):
    """Wyjątek zgłaszany, gdy użytkownik ma mniej niż 18 lat."""
    pass


def rejestruj_uzytkownika(wiek: int):
    if wiek < 18:
        raise WiekNiepoprawnyError("Użytkownik musi mieć co najmniej 18 lat.")
    print("Rejestracja przebiegła pomyślnie!")


try:
    wiek = int(input("Podaj wiek: "))
    rejestruj_uzytkownika(wiek)
except WiekNiepoprawnyError as e:
    print("Błąd rejestracji:", e)

