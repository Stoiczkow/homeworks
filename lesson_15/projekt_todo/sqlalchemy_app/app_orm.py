from sqlalchemy.orm import Session
from sqlalchemy_app.database import get_db
from sqlalchemy_app.models import Zadanie, Tag


def pokaz_zadania(db: Session):
    zadania = db.query(Zadanie).all()

    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
    print("------------------------\n")


def dodaj_zadanie(db: Session, opis: str):
    nowe_zadanie = Zadanie(opis=opis)
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie)


def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")

def usun_zadanie(db: Session, id_zadania: int):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    
    if zadanie:
        db.delete(zadanie)
        db.commit()
        print("Zadanie usunięte!")
    else:
        print("Nie znaleziono zadania o podanym ID")

def wyszukaj_po_opisie(db: Session, fraza: str):
    wyniki = db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()
    return wyniki

def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if zadanie:
        zadanie.opis = nowy_opis
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")

def dodaj_tag_do_zadania(db: Session, id_zadania: int, nazwa_tagu: str):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    
    if not zadanie:
        print("Nie znaleziono zadania o podanym ID.")
        return
    
    tag = db.query(Tag).filter(Tag.nazwa == nazwa_tagu).first()

    if not tag:
        tag = Tag(nazwa=nazwa_tagu)
        db.add(tag)
        db.commit()
        db.refresh(tag)

    if tag not in zadanie.tagi:
        zadanie.tagi.append(tag)
        db.commit()
        print("Tag został dodany do zadania.")
    else:
        print("To zadanie już ma taki tag.")

def main():
    db_generator = get_db()
    db_session = next(db_generator)

    while True:
        print("Menu (SQLAlchemy):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadania po opisie")
        print("6. Edytuj opis")
        print("7. Dodaj tag do zadania")
        print("8. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_zadania(db_session)
        elif wybor == "2":
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db_session, opis)
            print("Zadanie dodane!")
        elif wybor == "3":
            try:
                id_zadania = int(input("Podaj ID zadania do oznaczenia: "))
                oznacz_jako_zrobione(db_session, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == "4":
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                usun_zadanie(db_session, id_zadania)
                print("Zadanie usunięte!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == "5":
            fraza = input("Wpisz fraze występującą w opisie zadania: ")
            wyniki = wyszukaj_po_opisie(db_session, fraza)
            if wyniki:
                for zadanie in wyniki:
                    status = "✓" if zadanie.zrobione else "✗"
                    print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
            else:
                print("Brak wyników")
        elif wybor == "6":
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                nowy_opis = input("Podaj nowy opis: ")
                edytuj_zadanie(db_session, id_zadania, nowy_opis)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == "7":
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                nazwa_tagu = input("Podaj nazwę tagu: ")
                dodaj_tag_do_zadania(db_session, id_zadania, nazwa_tagu)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == "8":
            print("Do zobaczenia!")
            db_session.close()
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()