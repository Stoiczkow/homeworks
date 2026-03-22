# Zadanie 7 – Zamówienia Anny Nowak

# napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci, Zamowienia, Zamowienia_Produkty i Produkty.

#  wyświetli nazwy wszystkich produktów zamówionych przez klienta o imieniu 'Anna Nowak'
#  Będziesz potrzebować połączyć dane z czterech tabel: Klienci, Zamowienia, Zamowienia_Produkty i Produkty


import sqlite3

Connection = sqlite3.connect("sklep.db") # połączenie z bazą danych
cursor = Connection.cursor() # tworzenie obiektu kursora
# musimy przy join uzyc tej pragmy

cursor.execute('''SELECT nazwa_produktu FROM produkty as p
                JOIN Zamowienia_Produkty as zp ON p.id_produktu = zp.id_produktu
                JOIN Zamowienia as z ON z.id_zamowienia = zp.id_zamowienia
                JOIN Klienci as k ON k.id_klienta = z.id_klienta
                WHERE k.imie = "Anna Nowak"
                ''')

result = cursor.fetchall()
print(result)

Connection.commit()# połączenie z bazą + wykonywanie SQL, zatwierdza zmiany w bazie danych po co commit dane są trwale zapisane w bazie
Connection.close()