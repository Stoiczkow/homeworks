from sqlalchemy.orm import Session
from database import get_db
from models import Zadania, Tag, ZadaniaTag

def pokaz_zadania(db: Session):
    zadania = db.query(Zadania).all()
    print('--- Twoje zadania ---')
    for zadanie in zadania:
        print(f"ID: {zadanie.id} -> {zadanie.opis} [TAGI:] {zadanie.tags} {"[ZROBIONE]" if zadanie.zrobione else "[NIE ZROBIONE]"} data: {zadanie.data_utworzenia}")

def dodaj_zadanie(db: Session, nowy_opis: str):
    nowe_zadanie = Zadania(opis=nowy_opis)

    db.add(nowe_zadanie)
    db.commit()

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).first()

    # To samo tylko w jednym zapytaniu
    # zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).update({"zrobione": True})
    # db.commit()
    
    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie oznaczone jako wykonane.")
    else:
        print("Nie znaleziono takiego zadania")

def usun_zadanie(db: Session, id_zadania: int):

    # W jednym zapytaniu
    # zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).delete()
    # db.commit()

    zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).first()

    if zadanie:
        db.delete(zadanie)
        print("Usunięto zadanie.")
        db.commit()
    else:
        print("Nie znaleziono takiego zadania")

def dodaj_tag(db: Session, nowa_nazwa: str):
    nowy_tag = Tag(nazwa=nowa_nazwa)
    db.add(nowy_tag)
    db.commit()

def powiaz_zadanie_z_tagiem(db: Session, id_zadania: int, id_tagu: int):
    nowe_powiazanie = ZadaniaTag(zadanie_id = id_zadania,
                                tag_id = id_tagu)
    db.add(nowe_powiazanie)
    db.commit()

def pokaz_tagi(db: Session):
    tags = db.query(Tag).all()
    print('===Twoje tagi===')
    for tag in tags:
        print(f"ID {tag.id} - {tag.nazwa} - Przypisany do zadań: {tag.zadania}")

def szukaj_fraze(db: Session, fraza: str):
    zadania = db.query(Zadania).filter(Zadania.opis.contains(fraza)).all()

    if zadania:
        for zadanie in zadania:
            print(f"ID: {zadanie.id} -> {zadanie.opis} [TAGI:] {zadanie.tags} {"[ZROBIONE]" if zadanie.zrobione else "[NIE ZROBIONE]"} data: {zadanie.data_utworzenia}")
    else:
        print("Nie znaleziono zadań z tą frazą")

def edytuj_fraze(db: Session, id_zadania: int, fraza: str):
    
    zadanie = db.query(Zadania).filter(Zadania.id == id_zadania).first()
    zadanie.opis = fraza
    db.commit()

def main():
    db = get_db()

    while True:
        print('=================')
        print('Menu:')
        print('1. Pokaż zadania')
        print('2. Dodaj zadanie')
        print('3. Oznacz jako ukończone')
        print('4. Usuń zadanie')
        print('5. Dodaj nowy tag')
        print('6. Powiąż tag z zadaniem')
        print('7. Pokaż tagi')
        print('8. Szukaj zadania po frazie')
        print('9. Edytuj opis zadania')
        print('[exit] Zakończ program')

        choice = input("Podaj numer opcji: ")

        if choice == '1':
            pokaz_zadania(db)
        elif choice == '2':
            nowy_opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db, nowy_opis)
        elif choice == '3':
            try:
                id_zadania = int(input("Podaj numer zadania które chcesz ukończyć: "))
                oznacz_jako_zrobione(db, id_zadania)
            except ValueError:
                print(f"Nieprawidłowy format ID.")
        elif choice == '4':
            try:
                id_zadania = int(input("Podaj numer zadania które chcesz usunąć: "))
                usun_zadanie(db, id_zadania)
            except ValueError:
                print(f"Nieprawidłowy format ID.")
        elif choice == '5':
            nowy_tag = input("Podaj nazwę nowego tagu: ")
            dodaj_tag(db, nowy_tag)
        elif choice == '6':
            id_zadania = int(input("Podaj ID zadania"))
            id_tagu = int(input("Podaj ID tagu"))
            powiaz_zadanie_z_tagiem(db, id_zadania, id_tagu)
        elif choice == '7':
            pokaz_tagi(db)
        elif choice =='8':
            fraza = input("Podaj frazę po której chcesz szukać: ")
            szukaj_fraze(db, fraza)
        elif choice =='9':
            try:
                id_zadania = int(input("Podaj numer zadania które chcesz zmienić: "))
            except ValueError:
                print(f"Nieprawidłowy format ID.")
                continue
            fraza = input("Podaj nowy opis zadania: ")
            edytuj_fraze(db, id_zadania, fraza)
        elif choice == 'exit':
            break

if __name__ == "__main__":
    main()