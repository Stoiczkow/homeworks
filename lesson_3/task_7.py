'''
Niemutowalność krotki:
- Utwórz krotkę punkt = (10, 20, 30) .
- Spróbuj zmienić pierwszy element krotki на 15 .
- Wyjaśnij w komentarzu do kodu, dlaczego wystąpił błąd
'''

punkt = (10, 20, 30)

# Próba zmiany pierwszego elementu

punkt[0] = 15

# Ten kod spowoduje błąd typu:
# TypeError: 'tuple' object does not support item assignment
#
# Wyjaśnienie:
# Krotki (tuple) w Pythonie są niemutowalne, co oznacza,
# że po ich utworzeniu nie można zmieniać ich elementów.
# Można je tylko odczytywać, ale nie modyfikować.
