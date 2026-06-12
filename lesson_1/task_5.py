'''
Kantor wymiany walut:
Utwórz plik task5_exchange.py .
Załóż, że kurs dolara wynosi 4.0 zł. Zapytaj użytkownika o kwotę w złotówkach.
Oblicz i wyświetl, ile to będzie w dolarach.
'''

kurs_usd = 4.0

zl = float(input("Podaj kwotę w złotówkach: "))
usd = zl / kurs_usd

print(f"{zl} zł to około {usd} dolarów.")
