from task_manager_raw import TaskManagerRaw


def main():
    manager = TaskManagerRaw()

    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Wyszukaj zadania")
        print("5. Usuń zadanie")
        print("6. Wyjdź")
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            zadania = manager.pobierz_zadania()
            if not zadania:
                print("Brak zadań na liście.")
            else:
                print("\n--- Twoja lista zadań ---")
                for zadanie in zadania:
                    status = "✓" if zadanie[2] else "✗"
                    print(f"[{status}] ID: {zadanie[0]}, Opis: {zadanie[1]}, Priorytet: {zadanie[3]}")
                print("------------------------\n")

        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            priorytet = int(input("Podaj priorytet do zadania: "))
            manager.dodaj_zadanie(opis, priorytet)
            print("Zadanie dodane!")

        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                manager.oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == '4':
            fraza = input("Podaj frazę do wyszukania: ")
            zadania = manager.wyszukaj_zadania(fraza)
            if not zadania:
                print(f"Brak zadań o opisie: {fraza}")
            else:
                print("\n--- Twoja lista zadań ---")
                for zadanie in zadania:
                    print(f"ID: {zadanie[0]}, Opis: {zadanie[1]}")
                print("------------------------\n")

        elif wybor == '5':
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                manager.usun_zadanie(id_zadania)
                print(f"Zadanie o id: {id_zadania} usunięte")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == '6':
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()