'''
Rzutowanie typów: Utwórz zmienną liczba_str = "5.8" . Przekonwertuj ją najpierw na
float , a następnie na int i wyświetl wyniki obu konwersji. Co zauważyłeś podczas
konwersji float na int ?
'''

liczba_str = "5.8"

# Konwersja na float
liczba_float = float(liczba_str)
print("Po konwersji na float:", liczba_float)

# Konwersja na int
liczba_int = int(liczba_float)
print("Po konwersji na int:", liczba_int)

# Podczas konwersji float -> int część dziesiętna zostaje obcięta (nie zaokrąglona!).
# Czyli 5.8 staje się 5.

