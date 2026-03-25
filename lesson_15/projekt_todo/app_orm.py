from sqlalchemy.orm import Session

from database import get_db
from models import Zadania, Tag, ZadaniaTag

def pokaz_zadania(db: Session):
    zadania = db.query(Zadania).all()
    
    print('--- Twoje zadania ---')

    for zadanie in zadania:
        print(f"ID {zadanie.id} - {zadanie.opis} - Zrobione {zadanie.zrobione}, data utworzenia {zadanie.data_utworzenia}, Tagi {zadanie.tags}")

def dodaj_zadanie(db: Session, nowy_opis: str):
    nowe_zadanie = Zadania(opis=nowy_opis)

    db.add(nowe_zadanie)
    db.commit()

def filtruj_zadania_po_opisie(db: Session, fraza: str):
    zadania = db.query(Zadania).filter(Zadania.opis.contains(fraza)).all()

    if zadania:
        print('--- Twoje zadania ---')

        for zadanie in zadania:
            print(f"ID {zadanie.id} - {zadanie.opis} - Zrobione {zadanie.zrobione}, data utworzenia {zadanie.data_utworzenia}")
    else:
        print(f"Nie znaleziono zadań z frazą {fraza} w opisie.")


def usun_zadanie(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
    # zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).delete()
    if not zadanie:
        print("Nie znaleziono takiego zadania.")
        return
    
    db.delete(zadanie)
    db.commit()

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
    # zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).update({"zrobione": True})
    # db.commit()
    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zostało zaktualizowane!")
    else:
        print(f"Nie znaleziono zadania o id {id_zadania}")

def edytuj_zadanie(db: Session, id_zadania: int, edytowany_opis: str):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
                                       
    if zadanie:
        zadanie.opis = edytowany_opis
        db.commit()
        print(f"Zaktualizowano opis zadania ID: {id_zadania}")
    else:
        print(f"Nie znaleziono zadania ID: {id_zadania} ")

def dodaj_tag(db: Session, nowa_nazwa: str):
    nowy_tag = Tag(nazwa=nowa_nazwa)
    
    db.add(nowy_tag)
    db.commit()

def poiwaz_zadanie_z_tagiem(db: Session, id_zadania: int, id_tagu: int):
    nowe_powiazanie = ZadaniaTag(zadanie_id=id_zadania,
                                 tag_id=id_tagu)
    
    db.add(nowe_powiazanie)
    db.commit()

def pokaz_tagi(db: Session):
    tags = db.query(Tag).all()

    print('==== Twoje tagi ====')
    for tag in tags:
        print(f'ID {tag.id} - {tag.nazwa} - {tag.zadania}')

def main():
    db = get_db()

    while True:
        print('=================')
        print('Menu:')
        print('1 - Pokaż zadania')
        print('2 - Dodaj zadanie')
        print('3 - Zaktualizuj zadanie')
        print('4 - Usuń zadanie')
        print('5 - Filtruj zadania')
        print('6 - Edytuj opis zadania')
        print('7 - Dodaj nowy tag')
        print('8 - Dodaj tag do zadania')
        print('9 - Pokaż tagi')
        print('10 - Wyjdź')

        choice = input('Wybierz opcję: ')

        if choice == '1':
            pokaz_zadania(db)
        elif choice == '2':
            nowy_opis = input('Podaj opis zadania: ')
            dodaj_zadanie(db, nowy_opis)
        elif choice == '3':
            try:
                id = int(input('Podaj numer zadania: '))
                oznacz_jako_zrobione(db, id)
            except ValueError:
                print(f"Nieprawidłowy format ID. Musi być int")
        elif choice == '4':
            id = int(input('Podaj id zadania które chcesz usunąć: '))
            usun_zadanie(db, id)
        elif choice == '5':
            fraza = input('Podaj szukaną frazę: ')
            filtruj_zadania_po_opisie(db, fraza)
        elif choice == '6':
            try:
                id = int(input('Podaj numer zadania do edycji: '))
                edytowany_opis = input('Podaj nowy opis: ')
                edytuj_zadanie(db, id, edytowany_opis)
            except ValueError:
                print(f"Nieprawidłowy format ID. Musi być int")
        elif choice == '7':
            nowy_tag = input('Podaj nazwę tagu: ')
            dodaj_tag(db, nowy_tag)
        elif choice == '8':
            id_zadania = int(input("Podaj id zadania: "))
            id_tagu = int(input("podaj id tagu: "))
            poiwaz_zadanie_z_tagiem(db, id_zadania, id_tagu)
        elif choice == '9':
            pokaz_tagi(db)
        elif choice == '10':
            print('Koniec działania programu.')
            break


if __name__ == '__main__':
    main()