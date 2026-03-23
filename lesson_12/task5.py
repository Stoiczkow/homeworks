# Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat użytkownikowi.

try: 
    with open("nieistniejący.txt", "r", encoding="utf-8") as f:
        plik = f.read()
except FileNotFoundError:
    print("Plik nie istnieje.")