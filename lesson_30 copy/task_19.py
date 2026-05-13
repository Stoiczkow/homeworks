# Zadanie 19 – AI: Równoległa analiza sentymentu (symulacja)
# Stwórz listę 20 przykładowych zdań (opinii o produkcie). Napisz funkcję
# analizuj_sentyment(zdanie), która symuluje zapytanie do API AI przez
# time.sleep(random.uniform(0.5, 2.0)) i zwraca losowo "Pozytywny", "Negatywny" lub
# "Neutralny". Użyj puli wątków (concurrent.futures.ThreadPoolExecutor), aby przeanalizować
# wszystkie zdania i zebrać wyniki. Zmierz czas wykonania.