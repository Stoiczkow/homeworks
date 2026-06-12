'''
Tworzenie profilu: Napisz funkcję stworz_profil(imie, **dane_dodatkowe) , która
przyjmuje imię oraz dowolną liczbę nazwanych argumentów (np. wiek=30 ,
miasto="Warszawa" ). Funkcja powinna zwrócić słownik z profilem użytkownika, gdzie
klucz 'imie' jest obowiązkowy, a reszta danych jest pobierana z **dane_dodatkowe .
'''

def stworz_profil(imie, **dane_dodatkowe):
    profil = {"imie": imie}
    profil.update(dane_dodatkowe)
    return profil

print(stworz_profil("Ala", wiek=30, miasto="Warszawa"))
