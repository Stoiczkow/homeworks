while True:
    try:
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        operacja = input("Podaj operacje (+, -, *, /): ")

        if operacja == "+":
            wynik = a + b
        elif operacja == "-":
            wynik = a - b
        elif operacja == "*":
            wynik = a * b
        elif operacja == "/":
            wynik = a / b
        else:
            print("Nieznana operacja.")
            continue
    except ValueError:
        print("Blad: Podaj poprawna liczbe.")
    except ZeroDivisionError:
        print("Blad: Dzielenie przez zero!")
    else:
        print(f"Wynik: {a} {operacja} {b} = {wynik}")
    finally:
        print("Koniec obliczen.")
