# Symulacja Klient-Serwer: Stwórz prostą symulację interakcji Klient-Serwer przy użyciu
# klas.
# Napisz klasę FakeServer , która w __init__ tworzy "bazę danych" w postaci
# słownika, np. self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2,
# "name": "Anna"}]} .
# Klasa FakeServer powinna mieć metodę handle_request(request: dict) , która
# analizuje żądanie (reprezentowane przez słownik).
# Jeśli metoda to GET a cel to /users , powinna zwrócić słownik-odpowiedź z
# kodem 200 i listą użytkowników w ciele.
# Jeśli metoda to POST a cel to /users , powinna dodać nowego użytkownika z
# ciała żądania do self.db i zwrócić odpowiedź z kodem 201 (Created).
# Dla każdego innego żądania, zwróć odpowiedź z kodem 404 (Not Found).
# Napisz klasę FakeClient z metodą send(server, request) , która "wysyła" żądanie
# do obiektu serwera i drukuje otrzymaną odpowiedź.
# Przetestuj scenariusze: pobranie wszystkich użytkowników, dodanie nowego
# użytkownika i próbę dostępu do nieistniejącego zasobu

class FakeServer():
    def __init__(self):
        self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2, "name": "Anna"}]}

    def handle_request(self, request: dict):

        endpoint = request.get('endpoint')
        method = request.get('method')
        body: dict | None = request.get('body')

        if endpoint == "/user":
            if method == "GET":
                return (200, self.db)
            if method == "POST":
                self.db.update(body)
                return 201
            else:
                return 405
        else:
            return 404


class FakeClient():
    def __init__(self):
        pass

    def send(self, server: FakeServer, request: dict):
        
        return server.handle_request(request)

# Przykład użycia

fake_server = FakeServer()
browser = FakeClient()

attempt1 = {'endpoint': '/user',
            'method': 'GET',
            'body': None}

attempt2 = {'endpoint': '/product',
            'method': 'GET',
            'body': None}

attempt3 = {'endpoint': '/user',
            'method': 'POST',
            'body': {"id": 3, "name": "Krzysztof"}}

print(f"Pierwsze użycie - pobranie danych: {browser.send(fake_server, attempt1)}")
print(f"Użycie nieistniejącego endpointa: {browser.send(fake_server, attempt2)}")
print(f"Dodanie użytkownika: {browser.send(fake_server, attempt3)}")
print(f"Ponowne pobranie danych: {browser.send(fake_server, attempt1)}")