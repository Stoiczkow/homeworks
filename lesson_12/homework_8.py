# Zadanie 8 – Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec obliczeń.".




while True:
    result = 0

    try:
        number_1 = int(input("podaj pierwszą liczbę: "))
        number_2 = int(input("podaj drugą liczbę: "))
    
        sign = input("Podaj znak, +, -, *, /: ")

        if sign not in [ "+", "-", "*", "/"]:
            raise ValueError

        if '/' == sign:
            result = number_1 / number_2
        elif '-' == sign:
            result = number_1 - number_2
        elif '+' == sign:
            result = number_1 + number_2
        elif '*' == sign:
            result = number_1 * number_2


    except ZeroDivisionError:
        print("Nie dziel przez zero.")
    except ValueError:
        print("Błędna wartość")
        continue
    else:
        print(f"Wynik dzielenia {number_1} {sign} {number_2} = {result}")
    finally:
        print("Koniec obliczeń.")
    # break

