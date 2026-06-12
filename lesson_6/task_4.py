'''
Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . Napisz
funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego
global . Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. Wyświetl wartość
zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę.
'''

POZIOM_DOSTEPU = "user"   # zmienna globalna

def zmien_poziom():
    # Tworzymy zmienną LOKALNĄ o tej samej nazwie
    POZIOM_DOSTEPU = "admin"
    print("Wewnątrz funkcji:", POZIOM_DOSTEPU)

zmien_poziom()
print("Poza funkcją:", POZIOM_DOSTEPU)

# Zmienna o tej samej nazwie wewnątrz funkcji jest lokalna.
# Nie zmienia globalnej zmiennej POZIOM_DOSTEPU, ponieważ nie użyliśmy słowa 'global'.
