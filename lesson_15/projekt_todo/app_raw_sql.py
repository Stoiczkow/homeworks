from database_raw import TaskManagerRaw


def pokaz_zadania(db):
    """Wyświetla listę wszystkich zadań."""
    zadania = db.pobierz_zadania()

    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie[2] else "✗"
        print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}")
    print("------------------------\n")


def main():
    db = TaskManagerRaw()
    db.init_db()

    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie po opisie")
        print("6. Edytuj opis")
        print("7. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_zadania(db)

        elif wybor == "2":
            opis = input("Podaj opis zadania: ")
            try:
                priorytet = int(input("Podaj priorytet zadania: "))
                db.dodaj_zadanie(opis, priorytet)
                print("Zadanie dodane!")
            except ValueError:
                print("Błędna wartość. Podaj liczbę.")
        elif wybor == "3":
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                db.oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == "4":
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                db.usun_zadanie(id_zadania)
                print("Zadanie usunięte!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == "5":
            opis_zadania = input("Wpisz frazę występującą w opisie zadania: ")
            wyniki = db.wyszukiwanie_po_opisie(opis_zadania)

            if wyniki:
                for zadanie in wyniki:
                    status = "✓" if zadanie[2] else "✗"
                    print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}")
            else:
                print("Brak wyników")
        
        elif wybor == "6":
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                nowy_opis = input("Podaj nowy opis")
                db.edytuj_zadanie(id_zadania, nowy_opis)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == "7":
            print("Do zobaczenia!")
            break

        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()