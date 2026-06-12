'''
Adnotacje i docstring: Weź funkcję kalkulator z zadania 1. Dodaj do niej pełne
adnotacje typów dla wszystkich parametrów i wartości zwracanej. Napisz również
kompletny docstring opisujący jej działanie.
'''

def kalkulator(a: float, b: float, operacja: str) -> float:
    """
    Wykonuje działanie matematyczne na dwóch liczbach.

    Parametry:
    a (float): pierwsza liczba
    b (float): druga liczba
    operacja (str): rodzaj działania — '+', '-', '*', '/'

    Zwraca:
    float: wynik działania matematycznego

    Jeśli operacja jest nieznana, funkcja zgłasza ValueError.
    """
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b
    else:
        raise ValueError("Nieznana operacja.")
