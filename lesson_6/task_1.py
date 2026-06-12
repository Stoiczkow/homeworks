'''
Kalkulator: Napisz funkcję kalkulator(a, b, operacja) , która przyjmuje dwie liczby i
string z operacją ( "+" , "-" , "*" lub / "). Funkcja powinna zwracać wynik
odpowiedniego działania.
'''

def kalkulator(a, b, operacja):
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b
    else:
        return "Nieznana operacja"
