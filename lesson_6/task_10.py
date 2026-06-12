'''
Mini-projekt: Walidator hasła: Stwórz funkcję sprawdz_haslo(haslo: str) -> bool .
- Funkcja powinna sprawdzać, czy hasło spełnia następujące warunki i zwracać True lub False :
- Ma co najmniej 8 znaków.
- Zawiera co najmniej jedną wielką literę.
- Zawiera co najmniej jedną cyfrę. Napisz do niej pełną dokumentację (docstring i
adnotacje)
'''

def sprawdz_haslo(haslo: str) -> bool:
    """
    Sprawdza, czy hasło spełnia wymagania bezpieczeństwa.

    Wymagania:
    - minimum 8 znaków,
    - co najmniej jedna wielka litera,
    - co najmniej jedna cyfra.

    Parametry:
    haslo (str): hasło do sprawdzenia

    Zwraca:
    bool: True, jeśli hasło spełnia wymagania; False w przeciwnym razie.
    """
    if len(haslo) < 8:
        return False
    if not any(znak.isupper() for znak in haslo):
        return False
    if not any(znak.isdigit() for znak in haslo):
        return False
    return True

# Przykład:
print(sprawdz_haslo("Test1234"))
