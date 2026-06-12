"""
Mini-projekt: Lista zadań

Program powinien:
1. Przy starcie próbować wczytać zadania z pliku zadania.json.
2. Pozwalać użytkownikowi dodać nowe zadanie.
3. Pozwalać wyświetlić wszystkie zadania.
4. Przy zamknięciu (lub na polecenie) zapisywać aktualną listę zadań do pliku zadania.json.
"""

import json
import os

PLIK = "zadania.json"


def wczytaj_zadania():
    """Wczytuje zadania z pliku JSON, jeśli istnieje."""
    if os.path.exists(PLIK):
        try:
            with open(PLIK, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Błąd: plik istnieje, ale jest uszkodzony. Tworzę pustą listę.")
    return []


def zapisz_zadania(zadania):
    """Zapisuje zadania do pliku JSON."""
    with open(PLIK, "w", encoding="utf-8") as f:
        json.dump(zadania, f, ensure_ascii=False, indent=4)


def menu():
    print("\n--- LISTA ZADAŃ ---")
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Zapisz i zakończ")
    print("4. Zakończ bez zapisywania")


def main():
    zadania = wczytaj_zadania()

    while True:
        menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            zadanie = input("Wpisz treść zadania: ")
            zadania.append(zadanie)
            print("Dodano zadanie.")

        elif wybor == "2":
            if not zadania:
                print("Brak zadań.")
            else:
                print("\nTwoje zadania:")
                for i, z in enumerate(zadania, start=1):
                    print(f"{i}. {z}")

        elif wybor == "3":
            zapisz_zadania(zadania)
            print("Zapisano. Do zobaczenia!")
            break

        elif wybor == "4":
            print("Zakończono bez zapisywania.")
            break

        else:
            print("Nieznana opcja.")


if __name__ == "__main__":
    main()
