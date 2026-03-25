# Własnymi słowami: Wyjaśnij, jaka jest różnica między Klientem a Serwerem w
# architekturze Klient-Serwer. Podaj po jednym przykładzie każdego z nich.

# Odpowiedź

# Klient wysyła żądanie (request) do serwera za pomocą odpowiedniej metody, przekazując nagłówki.
# Dzięki temu serwer otrzymuje instrukcję dot. tego, co chciałby uzyskać klient.
# Klientem może być np. przeglądarka internetowa, żądaniem chęć wejścia na stronę i pobrania jej zawartości
# Klientem może być też np. program w Pythonie z biblioteką requests, który dodaje nowe produkty do sklepu za pomocą metody POST

# Serwer w tym układzie jest komputerem w sieci Internet na którym działa aplikacja webowa, która potrafi rozpoznać intencje użytkownika i jego request
# Dokonuje odpowiedniej akcji -> np. generuje/przekazuje kod HTML do klienta; albo dodaje to co zażądał użytkownik do bazy danych.
# Serwer to np. wykupiony współdzielony dostęp do komputera w jednej z firm hostingowych, na której działa aplikacja napisana we Flask, która generuje stronę dla użytkownika.