# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
# imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
# Zamowienia, Zamowienia_Produkty i Produkty

# TASK 7

import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute('''SELECT nazwa_produktu FROM produkty as p
                JOIN Zamowienia_Produkty as zp ON p.id_produktu = zp.id_produktu
                JOIN Zamowienia as z ON z.id_zamowienia = zp.id_zamowienia
                JOIN Klienci as k ON k.id_klienta = z.id_klienta
                WHERE k.imie = "Anna Nowak"
                ''')

result = cursor.fetchall()

print(result)

conn.commit()
conn.close()