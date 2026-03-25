# Zadanie 8 – Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec obliczeń.".
end = False

while True:
    number_1 = input("Podaj pierwsza cyfrę: ")
    number_2 = input("Podaj drugą cyfrę: ")
    user_ops = input("Podaj żądane działanie (+,-,*,/): ")
    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
        if user_ops == "+":
            result = number_1 + number_2
        elif user_ops == "-":
            result = number_1 - number_2
        elif user_ops == "*":
            result = number_1 * number_2
        elif user_ops == "/":
            result = number_1 / number_2
        else:
            raise ValueError
    except ValueError:
        print("Podałeś niepoprawne liczby lub operacje.")
    except ZeroDivisionError:
        print("Nie dzieli się przez zero.")
    else:
        print(result)    

    finally:
        print("Koniec obliczeń.")
    while True:        
        continue_choice = input("Chcesz kontynuować? (tak/nie): ")
        if continue_choice == "tak":
            break
        elif continue_choice == "nie":
            end = True
            break
        else:
            print("Wpisz tak, albo nie: ")
    if end:
        break