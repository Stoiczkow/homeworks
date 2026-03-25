1. 
Dopasuj pojęcia: Połącz w pary metodę HTTP z jej głównym przeznaczeniem.
    GET
    POST
    DELETE
    PUT
    A. Usunięcie danych
    B. Pobranie danych
    C. Zastąpienie danych w całości
    D. Utworzenie nowych danych

2. 
Własnymi słowami: Wyjaśnij, jaka jest różnica między Klientem a Serwerem w
architekturze Klient-Serwer. Podaj po jednym przykładzie każdego z nich.

3. 
Model żądania: Utwórz w Pythonie słownik, który będzie reprezentował żądanie GET w
celu pobrania listy wszystkich artykułów z adresu /api/articles . W nagłówkach dodaj
klucz Host z wartością my-blog.com .

4. 
Pytanie teoretyczne: Kiedy otwierasz stronę google.com w przeglądarce, jaką
metodę HTTP najprawdopodobniej wysyła Twoja przeglądarka, aby wyświetlić stronę
główną?

5. 
Pytanie teoretyczne: Do której warstwy modelu TCP/IP należy protokół IP,
odpowiedzialny za znalezienie drogi do komputera docelowego?

6. 
Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .
Konstruktor __init__ powinien przyjmować method , target oraz opcjonalnie
headers (słownik) i body (string).
Dodaj metodę display() , która będzie drukować sformatowane żądanie na konsoli w
czytelnej formie, np.:
--- HTTP Request ---
Method: GET
Target: /index.html
Headers:
Host: example.com
User-Agent: PythonClient/1.0
Body:
(empty)
--------------------
Przetestuj klasę, tworząc obiekt dla żądania POST z przykładowymi danymi.

7.
Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
argument adres URL w formie stringa (np.
https://api.example.com:8080/users/search?active=true ) i zwraca słownik
zawierający jego części: protocol , domain , port i path .
Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() .


8.
Symulacja Klient-Serwer: Stwórz prostą symulację interakcji Klient-Serwer przy użyciu
klas.
Napisz klasę FakeServer , która w __init__ tworzy "bazę danych" w postaci
słownika, np. self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2,
"name": "Anna"}]} .
Klasa FakeServer powinna mieć metodę handle_request(request: dict) , która
analizuje żądanie (reprezentowane przez słownik).
Jeśli metoda to GET a cel to /users , powinna zwrócić słownik-odpowiedź z
kodem 200 i listą użytkowników w ciele.
Jeśli metoda to POST a cel to /users , powinna dodać nowego użytkownika z
ciała żądania do self.db i zwrócić odpowiedź z kodem 201 (Created).
Dla każdego innego żądania, zwróć odpowiedź z kodem 404 (Not Found).
Napisz klasę FakeClient z metodą send(server, request) , która "wysyła" żądanie
do obiektu serwera i drukuje otrzymaną odpowiedź.
Przetestuj scenariusze: pobranie wszystkich użytkowników, dodanie nowego
użytkownika i próbę dostępu do nieistniejącego zasobu.


9.
PUT vs PATCH: Wyobraź sobie, że na serwerze pod adresem /users/1 znajduje się
następujący zasób w formacie JSON: {"name": "Katarzyna", "email":
"k.nowak@example.com", "city": "Warszawa"} .
Opisz, jak wyglądałoby ciało żądania PUT , aby zmienić tylko imię na "Kasia".
Opisz, jak wyglądałoby ciało żądania PATCH , aby zmienić tylko imię na "Kasia".
Wyjaśnij w komentarzu w kodzie, dlaczego te żądania się różnią i która metoda jest
bardziej "oszczędna" pod względem przesyłanych danych.


10.

Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
nagłówki: Host i User-Agent .
Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
Host").
Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
wyjątków.