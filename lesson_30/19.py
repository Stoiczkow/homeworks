#  Zadanie 19 – AI: Równoległa analiza sentymentu (symulacja)
# Stwórz listę 20 przykładowych zdań (opinii o produkcie). Napisz funkcję
# analizuj_sentyment(zdanie), która symuluje zapytanie do API AI przez
# time.sleep(random.uniform(0.5, 2.0)) i zwraca losowo "Pozytywny", "Negatywny" lub
# "Neutralny". Użyj puli wątków (concurrent.futures.ThreadPoolExecutor), aby przeanalizować
# wszystkie zdania i zebrać wyniki. Zmierz czas wykonania.

from faker import Faker
import time
from random import uniform, choice
import concurrent.futures

start_time = time.time()

fake = Faker()
CHOICE_OPTIONS = ["Pozytywny", "Negatywny", "Neutralny"]

WORKERS = 4

sentences = []
results = []



for _ in range(20):
    sentences.append(fake.sentence())


def analizuj_sentyment(zdanie):
    time.sleep(uniform(0.5, 2.0))
    return choice(CHOICE_OPTIONS)

with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
    sentence_to_choice = {executor.submit(analizuj_sentyment, zdanie): zdanie for zdanie in sentences}
    for current_choice in concurrent.futures.as_completed(sentence_to_choice):
        zdanie = sentence_to_choice[current_choice]
        try:
            data = current_choice.result()
        except Exception as exc:
            print(f"{zdanie} wyrzuciło wyjątek: {exc}")
        else:
            print(f"Zdanie {zdanie} zostało ocenione jako {data}")
            results.append(data)

end_time = time.time() - start_time

print(f"Wyniki dostarczono przy udziale {WORKERS} workerów w czasie {end_time}")
print(results)