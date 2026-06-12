"""
Bezpieczne pobieranie ze słownika:
Napisz funkcję pobierz_wartosc(slownik, klucz), która zwraca wartość lub None,
bez użycia try...except (użyj .get()).
Następnie napisz drugą wersję z try...except KeyError.
"""

def pobierz_wartosc(slownik, klucz):
    return slownik.get(klucz)


def pobierz_wartosc_try(slownik, klucz):
    try:
        return slownik[klucz]
    except KeyError:
        return None


print(pobierz_wartosc({"a": 1}, "b"))
print(pobierz_wartosc_try({"a": 1}, "b"))
