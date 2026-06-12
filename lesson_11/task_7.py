'''
Enkapsulacja w Telewizorze
Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal
(domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne
metody do zarządzania telewizorem:
wlacz() i wylacz()
zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV
jest włączony.
info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy
nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
100. 
'''

class Telewizor:
    def __init__(self):
        self._kanal = 1
        self._glosnosc = 10
        self.__wlaczony = False

    def wlacz(self):
        self.__wlaczony = True

    def wylacz(self):
        self.__wlaczony = False

    def zmien_kanal(self, numer):
        if self.__wlaczony:
            self._kanal = numer
        else:
            print("Telewizor jest wyłączony!")

    def glosniej(self):
        if self.__wlaczony and self._glosnosc < 100:
            self._glosnosc += 1

    def ciszej(self):
        if self.__wlaczony and self._glosnosc > 0:
            self._glosnosc -= 1

    def info(self):
        stan = "Włączony" if self.__wlaczony else "Wyłączony"
        print(f"{stan}, kanał: {self._kanal}, głośność: {self._glosnosc}")


tv = Telewizor()
tv.info()
tv.zmien_kanal(5)
tv.wlacz()
tv.zmien_kanal(5)
tv.glosniej()
tv.info()
