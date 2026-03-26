from sqlalchemy.orm import Session

from database import get_db
from models import Zadania, Tag, ZadaniaTag

def pokaz_zadania(db: Session):
    zadania = db.query(Zadania).all()
    
    print('--- Twoje zadania ---')
    
    for zadanie in zadania:
        print(f"ID {zadanie.id} - {zadanie.opis} - Zrobione {zadanie.zrobione} Tagi {zadanie.tags}")

def pokaz_tagi(db: Session):
    tags = db.query(Tag).all()
    
    print('--- Tagi ---')
    
    for tag in tags:
        print(f"ID {tag.id} - {tag.nazwa} - zadania {tag.zadania}")

def dodaj_zadanie(db: Session, nowy_opis: str):
    nowe_zadanie = Zadania(opis=nowy_opis)
    
    db.add(nowe_zadanie)
    db.commit()

def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
    
    if zadanie:
        zadanie.opis = nowy_opis
        db.commit()
        print(f"Opis zadania z ID {id_zadania} został zaktualizowany")
    else:
        print(f"Nie znaleziono zadania o ID {id_zadania}")
    
def filtruj_zadania_po_opisie(db: Session, fraza: str):
    zadania = db.query(Zadania).filter(Zadania.opis.contains(fraza)).all()
    
    if zadania:
        print('--- Twoje zadania ---')
    
        for zadanie in zadania:
           
            print(f"ID {zadanie.id} - {zadanie.opis} - Zrobione {zadanie.zrobione}  ")
    else:
        print(f"Nie znaleziono zadań z frazą {fraza} w opisie")
    
def dodaj_tag(db: Session, nowa_nazwa: str):
    nowy_tag = Tag(nazwa=nowa_nazwa)
    
    db.add(nowy_tag)
    db.commit()

def powiaz_zadanie_z_tagiem(db: Session, id_zadania: int, id_tagu: int):
    nowe_powiazanie = ZadaniaTag(zadanie_id=id_zadania, tag_id=id_tagu)
    db.add(nowe_powiazanie)
    db.commit()

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).first()
    # zadanie = db.query(Zadania).filter(Zadania.id==id_zadania).update({"zrobione": True})
    # db.commit() update przy użyciu jednego zapytania
    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zostało zaktualizowane!")
    else:
        print(f"Nie znaleziono zadania o id {id_zadania}")
        
def main():
    db = get_db()
    
    while True:
        print('==================')
        print('Menu: ')
        print('1 - Pokaż zadania')
        print('2 - Dodaj zadanie')
        print('3 - Zaktualizuj zadanie')
        print('4 - Filtruj zadania')
        print('5 - Dodaj tag')
        print('6 - Dodaj tag do zadania')
        print('7 - Pokaz tagi')
        print('8 - Edytuj zadanie')
        print('9 - Wyjdź')
        
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
                print(f"Nieprawidłowy format ID. Musi być podany int")
        elif choice == '4':
            fraza = input('Podaj szukaną frazę: ')
            filtruj_zadania_po_opisie(db, fraza)
        elif choice == '5':
            nowy_tag = input('Podaj nazwę tagu: ')
            dodaj_tag(db, nowy_tag)         
        elif choice == '6':
            id_tagu = int(input('Podaj id tagu: '))
            id_zadania = int(input('Podaj id zadania: '))
            powiaz_zadanie_z_tagiem(db, id_zadania, id_tagu)    
        elif choice == '7':
            pokaz_tagi(db)
        elif choice == '8':
            try:
                id = int(input('Podaj numer zadania '))
                nowy_opis = input('Wpisz nowy opis zadania ')
                edytuj_zadanie(db, id, nowy_opis)
            except ValueError:
                print(f"Nieprawidłowy format ID. Musi być podany int")
        elif choice == '9':
            print('Koniec działania programu')
            break


if __name__ == "__main__":
    main()