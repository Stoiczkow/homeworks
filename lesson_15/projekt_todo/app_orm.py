from sqlalchemy.orm import Session

from database import get_db
from models import Zadanie, Tag


def pokaz_zadania(db: Session):
    zadania = db.query(Zadanie).all()
    print("---- Twoje zadania ----")
    for z in zadania:
        tagi_str = ', '.join(t.nazwa for t in z.tagi) if z.tagi else 'brak'
        print(f"ID {z.id} - {z.opis} - Zrobione: {z.zrobione} - Priorytet: {z.priorytet} - Tagi: [{tagi_str}]")


def dodaj_zadanie(db: Session, opis: str, priorytet: int = 1):
    nowe = Zadanie(opis=opis, priorytet=priorytet)
    db.add(nowe)
    db.commit()


def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        zadanie.zrobione = True
        db.commit()


def usun_zadanie(db: Session, id_zadania: int):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        db.delete(zadanie)
        db.commit()


def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        zadanie.opis = nowy_opis
        db.commit()


def dodaj_tag_do_zadania(db: Session, id_zadania: int, nazwa_tagu: str):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if not zadanie:
        print("Nie znaleziono zadania.")
        return

    tag = db.query(Tag).filter(Tag.nazwa == nazwa_tagu).first()
    if not tag:
        tag = Tag(nazwa=nazwa_tagu)
        db.add(tag)

    if tag not in zadanie.tagi:
        zadanie.tagi.append(tag)
    db.commit()


def main():
    db = get_db()

    while True:
        print("=" * 40)
        print("1 - Pokaz zadania")
        print("2 - Dodaj zadanie")
        print("3 - Oznacz jako zrobione")
        print("4 - Usun zadanie")
        print("5 - Edytuj zadanie")
        print("6 - Dodaj tag do zadania")
        print("9 - Wyjdz")

        choice = input("Wybierz opcje: ")

        if choice == "1":
            pokaz_zadania(db)

        elif choice == "2":
            opis = input("Opis zadania: ")
            try:
                priorytet = int(input("Priorytet (domyslnie 1): ") or "1")
            except ValueError:
                priorytet = 1
            dodaj_zadanie(db, opis, priorytet)
            print("Zadanie dodane.")

        elif choice == "3":
            try:
                id_z = int(input("ID zadania: "))
                oznacz_jako_zrobione(db, id_z)
                print("Oznaczono jako zrobione.")
            except ValueError:
                print("Nieprawidlowe ID.")

        elif choice == "4":
            try:
                id_z = int(input("ID zadania do usuniecia: "))
                usun_zadanie(db, id_z)
                print("Zadanie usuniete.")
            except ValueError:
                print("Nieprawidlowe ID.")

        elif choice == "5":
            try:
                id_z = int(input("ID zadania do edycji: "))
                nowy_opis = input("Nowy opis: ")
                edytuj_zadanie(db, id_z, nowy_opis)
                print("Zadanie zaktualizowane.")
            except ValueError:
                print("Nieprawidlowe ID.")

        elif choice == "6":
            try:
                id_z = int(input("ID zadania: "))
                nazwa_tagu = input("Nazwa tagu: ")
                dodaj_tag_do_zadania(db, id_z, nazwa_tagu)
                print("Tag dodany.")
            except ValueError:
                print("Nieprawidlowe ID.")

        elif choice == "9":
            print("Koniec programu.")
            break


if __name__ == "__main__":
    main()
