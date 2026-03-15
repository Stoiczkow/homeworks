# Zadanie 2 – Walidator wieku
# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie zmieniać wartości.

class Uzytkownik: # tworzymy kalsę
    def __init__(self, wiek):    # atrybuty / 
            self._wiek = wiek # Konstruktor uruchamia się przy tworzeniu obiektu.

    
    #@property się czesniej używa ni seter - pomoze wybrać dane z obiektu seter pozwala zmienić wartość za pomocą przypisania pracownik_1
    # seter - pozawala ustawiac nowe wlasciowsci nie za pomocą wywolania
    # @property → getter (odczyt)
    # @nazwa.setter → setter (zmiana)
    # setter jest opcjonalny.
    # jak chcemy zmienić dane

    @property
    def wiek(self):     # getter zwraca wiek
          return self._wiek     #Getter pozwala odczytać wartość.
    
    # setter                    # setter i getter mają tu 1 nazwę set.wiek bez dekora
    @wiek.setter        # Setter – zmiana wartości
    def wiek(self, nowy_wiek):
        if nowy_wiek > 0 and nowy_wiek < 120:
            self._wiek = nowy_wiek  # przypisuje atrybut do funkcji age
        else:
             print("Wiek nie jest w zakresie 0 do 120")      # wyświetlenie błedu

        
# dsotajemy się teraz do wieku

#Tworzymy obiekt klasy
# self._wiek = 20
user = Uzytkownik(20)
user.wiek = 85      # tym setterem mozemy nadpisac wiek

#Wyderuowanie wieku
print(user.wiek)







# age to po prostu parametr (argument) funkcji settera — czyli nowa wartość wieku, którą próbujesz ustawić.

# Wzór / przykład
# @pensja.setter

# def pensja(self, nowa_wartosc):!!!!!!!!!!!!!!!! Wzór

# """Setter - wywoływany przy próbie przypisania nowej wartości."""
# if nowa_wartosc < 0:
# print("Błąd: Pensja nie może być ujemna!")
# else:
# print("Ustawiono nową pensję...")
# self._pensja = nowa_wartosc
