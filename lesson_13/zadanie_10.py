import sqlite3


def znajdz_sale_studenta(nazwisko):
    conn = sqlite3.connect('uczelnia.db')
    c = conn.cursor()

    c.execute('''
        SELECT s.imie, s.nazwisko, a.nazwa_budynku, a.numer_sali
        FROM studenci s
        JOIN przypisania p ON s.id_studenta = p.id_studenta
        JOIN audytoria a ON p.id_audytorium = a.id_audytorium
        WHERE s.nazwisko = ?
    ''', (nazwisko,))

    wyniki = c.fetchall()

    if wyniki:
        for imie, nazwisko, budynek, sala in wyniki:
            print(f"{imie} {nazwisko} -> {budynek}, sala {sala}")
    else:
        print(f"Nie znaleziono studenta o nazwisku '{nazwisko}'.")

    conn.close()


znajdz_sale_studenta('Kowalski')
znajdz_sale_studenta('Nowak')
znajdz_sale_studenta('Nieistniejacy')
