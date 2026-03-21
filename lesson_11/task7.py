# Zadanie 7 – Enkapsulacja w Telewizorze
# Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal (domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne metody do zarządzania telewizorem:
# wlacz() i wylacz() zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
# glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV jest włączony.
# info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
# 100. (challenge

class Telewizor:
    def __init__(self):
        self.__kanal = 1
        self.__glosnosc = 10
        self.__wlaczony = False
    
    def wlacz(self):
        self.__wlaczony = True
        
    def wylacz(self):
        self.__wlaczony = False
        
    def zmien_kanal(self, numer):
        if self.__wlaczony:
            self.__kanal = int(numer)

    def glosniej(self):
        if self.__wlaczony and self.__glosnosc < 100:
            self.__glosnosc += 1
            

    def ciszej(self):
        if self.__wlaczony and self.__glosnosc > 0:
            self.__glosnosc -= 1

    def info(self):
        if self.__wlaczony:
            stan = "Włączony"
        else:
            stan = "Wyłączony"
        return f"TV {stan}, kanał: {self.__kanal}, głośność: {self.__glosnosc}."

tv = Telewizor()

tv.zmien_kanal(2)
print(tv.info())

tv.wlacz()
print(tv.info())

tv.zmien_kanal(10)
print(tv.info())

for _ in range(200):
    tv.glosniej()
print(tv.info())



    



        
    
