"""
Zadanie 8 – Kalkulator z pełną obsługą błędów
Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
Całość umieść w pętli while True , aby program działał do momentu przerwania.
Użyj bloku try...except do obsługi:
ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
ZeroDivisionError przy próbie dzielenia przez zero.
Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
obliczeń.".
"""

class Calculator:
    def __init__(self, number_1, number_2, operator):
        self.number_1 = number_1
        self.number_2 = number_2
        self.operator = operator

    def sum(self):
        return self.number_1 + self.number_2

    def sub(self):
        return self.number_1 - self.number_2

    def mul(self):
        return self.number_1 * self.number_2

    def div(self):
        return self.number_1 / self.number_2


while True:
    try:
        data = input("Input mathematical expression (ex: 2 * 6): ")
        parts = data.split()
        first_number = float(parts[0])
        second_number = float(parts[2])
        operator = parts[1]

        calculator = Calculator(first_number, second_number, operator)
        if operator == "+":
            result = calculator.sum()
        elif operator == "-":
            result = calculator.sub()
        elif operator == "*":
            result = calculator.mul()
        elif operator == "/":
            result = calculator.div()
        else:
            print(f"Unknown operator")

    except ValueError as e:
        print(f"Input error: {e}")

    except ZeroDivisionError:
        print(f"The division by zero resulted in zero.")

    except IndexError:
        print(f"Wrong input. The format should be: 'number1' 'operator' 'number2' ex: 2 + 2")

    else:
        print(f"The result is {result}")

    finally:
        print("End of calculation.")






