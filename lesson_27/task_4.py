'''
Zabawa z niskopoziomowym API w shellu
Uruchom Django shell za pomocą komendy python manage.py shell. Zaimportuj from
django.core.cache import cache. Użyj cache.set('my_key', 'hello world', 30) aby ustawić
wartość, a następnie cache.get('my_key') aby ją odczytać. Poczekaj 30 sekund i spróbuj
odczytać ją ponownie. Co się stało?
'''

# Ustawiłem wartość w pamięci podręcznej na 30 sekund.
# Po upływie tego czasu Django automatycznie ją usunęło, więc cache.get('my_key') zwróciło None.