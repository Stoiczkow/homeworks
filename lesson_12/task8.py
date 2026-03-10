# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
# obliczeń.".

while True:
    try:
        first_number = float(input("Podaj pierwszą liczbę: "))
        second_number = float(input("Podaj drugą liczbę: "))
        operator = input("Podaj operator, dostępne: [+], [-], [*], [/]: ")

        match operator:
            case "+":
                calculation = first_number + second_number
            case "-":
                calculation = first_number - second_number
            case "*":
                calculation = first_number * second_number
            case "/":
                calculation = first_number / second_number

    except ValueError:
        print("Podano nieprawidłową wartość")
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")
    else:
        print(calculation)
    finally:
        print("Koniec obliczeń\n\n")