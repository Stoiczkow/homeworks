# Zadanie 8 – Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
# obliczeń.".

class Calculator:
    def calculate(self, a, b, operation):
        if operation == "+":
            return a + b
        if operation == "-":
            return a - b
        if operation == "*":
            return a * b
        if operation == "/":
            return a / b

        raise ValueError("Nieprawidłowa operacja.")

    def run(self):
        while True:
            try:
                a = float(input("Podaj pierwszą liczbę: "))
                b = float(input("Podaj drugą liczbę: "))
                operation = input("Podaj operację (+, -, *, /): ").strip()

                result = self.calculate(a, b, operation)

            except ValueError as e:
                print(f"Błąd: {e}")

            except ZeroDivisionError:
                print("Błąd: nie można dzielić przez zero.")

            else:
                print(f"Wynik: {result}")

            finally:
                print("Koniec obliczeń.")


calculator = Calculator()
calculator.run()