# Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
# obliczeń.".

def calc():
    while True:
        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            op = input("Podaj operację (+, -, *, /): ")

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b
            else:
                print("Nieznana operacja.")
                continue

        except ValueError:
            print("Błąd: Proszę podać prawidłową liczbę.")
        except ZeroDivisionError:
            print("Błąd: Nie można dzielić przez zero.")
        else:
            print(f"Wynik: {result}")
        finally:
            print("Koniec obliczeń.\n")

calc()