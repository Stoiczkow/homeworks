# 8. 🧠 Zadanie 8 – Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
# obliczeń.".

print("Calculator")
    
while True:
    try:
        number_1 = float(input("Podaj pierwszą liczbę: "))        
        number_2 = float(input("Podaj drugą liczbę: "))        
        operator = input("Podaj operator (+, -, *, /) ")

        if operator == '+':
            result = number_1 + number_2
        elif operator == '-':                
            result = number_1 - number_2
        elif operator == '*':
            result = number_1 * number_2
        elif operator == '/':
            result = number_1 / number_2
    except ValueError:
        print("Błąd! Nie podałeś liczby!")
    except ZeroDivisionError:
        print("Błąd! Nie można dzielić przez 0!")
    except KeyboardInterrupt:
        print("Zakończono działanie kalkulatora")
    else:
        print(f"{number_1} {operator} {number_2} = {result}")
    finally:
        print("Koniec obliczeń")