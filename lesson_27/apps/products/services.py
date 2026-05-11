import time

from django.core.cache import cache


EXPENSIVE_CACHE_KEY = 'products:expensive_calculation'
EXPENSIVE_CACHE_TTL = 30  # sekundy - krotko dla wygodnego testowania


def get_expensive_calculation():
    """Symulacja drogiej operacji (np. agregacja, wywolanie zewnetrznego API).

    Wynik cachowany jest pod kluczem EXPENSIVE_CACHE_KEY przez
    EXPENSIVE_CACHE_TTL sekund. Pole 'source' pozwala odroznic skad
    przyszla wartosc.
    """
    cached = cache.get(EXPENSIVE_CACHE_KEY)
    if cached is not None:
        return {**cached, 'source': 'cache'}

    time.sleep(3)
    payload = {
        'answer': 42,
        'note': 'wynik kosztownych obliczen',
    }
    cache.set(EXPENSIVE_CACHE_KEY, payload, timeout=EXPENSIVE_CACHE_TTL)
    return {**payload, 'source': 'computed'}
