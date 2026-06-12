'''
Licznik wywołań: Stwórz domknięcie (closure). Napisz funkcję stworz_licznik() , która
zwraca funkcję. Każde wywołanie zwróconej funkcji powinno zwiększać wewnętrzny licznik i
zwracać jego aktualną wartość.
'''

def stworz_licznik():
    licznik = 0

    def zwieksz():
        nonlocal licznik
        licznik += 1
        return licznik

    return zwieksz

licz = stworz_licznik()
print(licz()) 
print(licz())  
print(licz())  
