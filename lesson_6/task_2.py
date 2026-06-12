'''
Informacje o książce: Stwórz funkcję opis_ksiazki(tytul, autor,
rok_wydania=2024) . Funkcja powinna zwracać sformatowany string, np. "Książka
'[Tytuł]' została napisana przez [Autor] i wydana w roku [Rok wydania]." .
Przetestuj ją, wywołując z argumentami pozycyjnymi i nazwanymi.
'''

def opis_ksiazki(tytul, autor, rok_wydania=2024):
    return f"Książka '{tytul}' została napisana przez {autor} i wydana w roku {rok_wydania}."

print(opis_ksiazki("Wiedźmin", "A. Sapkowski"))
print(opis_ksiazki(autor="S. King", tytul="IT", rok_wydania=1986))
