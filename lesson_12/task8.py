# Zadanie 8 – Kalkulator z pełną obsługą błędów

#Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /). Całość umieść w pętli while True , aby program działał do momentu przerwania. Użyj bloku try...except do obsługi: ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą. ZeroDivisionError przy próbie dzielenia przez zero. Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu. Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec obliczeń."

# Pętla while ture
while True:
    try:
        a = float(input("Podaj liczbę: "))
        b = float(input("podaj drugą liczbę: "))
        operations = input("Podaj operację (+, -, *, /):")

        # instrukcja warunkowa if
        if operations == "+":
            result = a + b
        elif operations == "-":
            result = a - b
        elif operations == "*":
            result = a * b
        elif operations == "/":
            result = a / b
        else:
            print("Niepoprawna operacja")

    # Walidacja błędów
    except ValueError:
        print("Error wpisano coś innego niż liczbę ")
    except ZeroDivisionError:
        print("Nie można dzielić przez zero ")
    else:
        print(f"wynik {result}")
    finally:      # zawsze wyświetla komunikat „Koniec obliczeń.” po każdej iteracji.
        print("Koniec oblcizeń \n")
        