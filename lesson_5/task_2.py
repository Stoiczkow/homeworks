'''
Kalkulator zniżek: Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, przysługuje mu 50%
zniżki. Użyj operatorów or i and .
'''

cena_bazowa = 100

student = input("Czy jesteś studentem? (tak/nie): ").lower()
wiek = int(input("Podaj swój wiek: "))

ma_znizke = (student == "tak") or (wiek < 18)

if ma_znizke:
    cena = cena_bazowa * 0.5
else:
    cena = cena_bazowa

print(f"Cena biletu: {cena} PLN")
