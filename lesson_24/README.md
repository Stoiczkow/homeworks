# Lesson 24

Tu wrzuć rozwiązanie zadania.


Zadanie 7 – Przekierowanie po zalogowaniu (challenge)
Zmodyfikuj LoginView tak, aby po zalogowaniu użytkownik był przekierowywany na stronę,
z której przyszedł. (Wskazówka: Django robi to domyślnie, jeśli w adresie URL logowania
jest parametr next, np. /login/?next=/profile/. Sprawdź, jak to działa w praktyce, próbując
wejść na chronioną stronę jako niezalogowany użytkownik). Twoim zadaniem jest opisanie
tego mechanizmu.

## Odpowiedź:

Mechanizm sprawia, że po wejściu na chroniony widok, w URL zapisuje się strona z której przyszliśmy,
czyli właśnie np. ?next=/profile/ - i po udanym logowaniu, jesteśmy tam przekierowywani.