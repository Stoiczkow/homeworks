'''
    Zadanie 5 - Odczyt pliku

    Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
    try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
    użytkownikowi.
'''
plik = None

try:
    plik = open("nieistniejacy.txt", "r", encoding='utf-8')
    zawartosc = plik.read()

except FileNotFoundError:
    print("Błąd plik nie istnieje.")

else:
    print("Plik odczytany pomyślnie.")
    print("Zawartość:", zawartosc)
finally:
# Ten blok wykona się zawsze
    if plik:
        plik.close()
        print("Blok finally: Plik został zamknięty.")
    else:
        print("Blok finally: Nie było czego zamykać.")