# Lesson 24 notes

## Zadanie 7

Django domyślnie obsługuje przekierowanie po zalogowaniu przez parametr `next`.
Jeżeli niezalogowany użytkownik próbuje wejść na widok zabezpieczony `@login_required`,
Django przekieruje go na:

`/login/?next=/chroniona-strona/`

Po poprawnym zalogowaniu `LoginView` odczytuje ten parametr i przekierowuje użytkownika
na pierwotnie żądany adres. Przykład w tej lekcji:

`/profile/` -> `/login/?next=/profile/` -> po zalogowaniu -> `/profile/`
