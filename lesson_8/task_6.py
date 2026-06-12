"""
Przerzucanie wyjątku:
Napisz funkcję przetworz_dane(dane), która w try...except łapie KeyError,
loguje go, a następnie rzuca nowy wyjątek BladPrzetwarzaniaDanychError
z informacją, którego klucza brakowało.
"""

class BladPrzetwarzaniaDanychError(Exception):
    pass


def przetworz_dane(dane):
    try:
        return dane["wartosc"]
    except KeyError as e:
        brakujacy = e.args[0]
        print(f"Log: Brakuje klucza: {brakujacy}")
        raise BladPrzetwarzaniaDanychError(
            f"Nie można przetworzyć danych — brak klucza: {brakujacy}"
        )



przetworz_dane({"inna": 123})
