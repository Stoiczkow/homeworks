from database_raw import TaskManagerRaw


def main():
    manager = TaskManagerRaw()

    while True:
        print("=" * 40)
        print("1 - Pokaz zadania")
        print("2 - Dodaj zadanie")
        print("3 - Oznacz jako zrobione")
        print("4 - Usun zadanie")
        print("5 - Edytuj zadanie")
        print("6 - Wyszukaj zadanie")
        print("9 - Wyjdz")

        choice = input("Wybierz opcje: ")

        if choice == "1":
            zadania = manager.pokaz_zadania()
            print("---- Twoje zadania ----")
            for z in zadania:
                print(f"ID {z[0]} - {z[1]} - Zrobione: {bool(z[2])} - Priorytet: {z[3]}")

        elif choice == "2":
            opis = input("Opis zadania: ")
            try:
                priorytet = int(input("Priorytet (domyslnie 1): ") or "1")
            except ValueError:
                priorytet = 1
            manager.dodaj_zadanie(opis, priorytet)
            print("Zadanie dodane.")

        elif choice == "3":
            try:
                id_z = int(input("ID zadania: "))
                manager.oznacz_jako_zrobione(id_z)
                print("Oznaczono jako zrobione.")
            except ValueError:
                print("Nieprawidlowe ID.")

        elif choice == "4":
            try:
                id_z = int(input("ID zadania do usuniecia: "))
                manager.usun_zadanie(id_z)
                print("Zadanie usuniete.")
            except ValueError:
                print("Nieprawidlowe ID.")

        elif choice == "5":
            try:
                id_z = int(input("ID zadania do edycji: "))
                nowy_opis = input("Nowy opis: ")
                manager.edytuj_zadanie(id_z, nowy_opis)
                print("Zadanie zaktualizowane.")
            except ValueError:
                print("Nieprawidlowe ID.")

        elif choice == "6":
            fraza = input("Fraza do wyszukania: ")
            wyniki = manager.wyszukaj_zadania(fraza)
            for z in wyniki:
                print(f"ID {z[0]} - {z[1]} - Zrobione: {bool(z[2])}")

        elif choice == "9":
            print("Koniec programu.")
            break


if __name__ == "__main__":
    main()
