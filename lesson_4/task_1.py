'''
Mini-kalkulator: Napisz program, który prosi użytkownika o podanie dwóch liczb, a
następnie wyświetla wynik ich dodawania, odejmowania, mnożenia i dzielenia. Pamiętaj o
konwersji typów z input() .
'''

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("Dodawanie:", a + b)
print("Odejmowanie:", a - b)
print("Mnożenie:", a * b)

if b != 0:
    print("Dzielenie:", a / b)
else:
    print("Dzielenie: błąd – nie można dzielić przez zero.")
