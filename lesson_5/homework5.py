#mini projekt
kursy = {"USD": 4.0, "EUR": 4.3}

while True:
    # Pobranie danych od użytkownika
    kwota_pln = float(input("Podaj kwotę w PLN: "))
    waluta = input("Podaj walutę (USD/EUR): ").upper()

    # Sprawdzenie wybranej waluty
    if waluta == "USD":
        wynik = kwota_pln / kursy["USD"]
        print(f"Otrzymasz {wynik:.2f} USD")
    elif waluta == "EUR":
        wynik = kwota_pln / kursy["EUR"]
        print(f"Otrzymasz {wynik:.2f} EUR")
    else:
        print("Nieprawidłowa waluta! Wybierz USD lub EUR.")

    # Pytanie o kontynuację
    kontynuuj = input("Czy chcesz kontynuować? (tak/nie): ").lower()
    if kontynuuj == "nie":
        print("Koniec programu.")
        break