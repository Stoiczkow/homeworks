"""
Logowanie błędów:
Zmodyfikuj zadanie 1 tak, aby każdy napotkany wyjątek (wraz z jego treścią)
był zapisywany do pliku log.txt, a program kontynuował działanie.
Użyj finally, aby upewnić się, że plik z logami jest zawsze zamykany.
"""

while True:
    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        operacja = input("Podaj operację (+, -, *, /): ")

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

    except Exception as e:
        with open("log.txt", "a", encoding="utf-8") as log:
            log.write(f"Błąd: {type(e).__name__} — {e}\n")
        print("Wystąpił błąd, zapisano do logów.")

    else:
        print("Wynik:", wynik)

    finally:
        print("Kolejna operacja...\n")
