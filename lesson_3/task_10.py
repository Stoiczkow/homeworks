'''
Mini-projekt "Formater danych": Napisz program, który poprosi użytkownika o jego imię i
nazwisko w jednej linii (np. " jan kowalski "). Program powinien:
- Oczyścić zbędne białe znaki.
- Sprawić, aby każde słowo zaczynało się wielką literą (metoda .title() ).
- Wyświetlić sformatowane dane oraz ich długość
'''

dane = input("Podaj swoje imię i nazwisko: ")

# 1. Usunięcie zbędnych białych znaków
oczyszczone = dane.strip()

# 2. Każde słowo zaczyna się wielką literą
sformatowane = oczyszczone.title()

# 3. Wyświetlenie wyniku i jego długości
print(f"Sformatowane dane: {sformatowane}")
print(f"Długość: {len(sformatowane)}")
