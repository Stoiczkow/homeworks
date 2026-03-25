"""
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
"""


class FakeServer:
    def __init__(self):
        self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2, "name": "Anna"}]}

    def handle_request(self, request: dict) -> dict:
        method = request.get("method")
        target = request.get("target")

        if method == "GET" and target == "/users":
            return {"status": 200, "body": self.db["users"]}

        if method == "POST" and target == "/users":
            new_user = request.get("body")
            if isinstance(new_user, dict):
                self.db["users"].append(new_user)
                return {"status": 201, "body": new_user}
            return {"status": 400, "body": "Invalid body"}

        return {"status": 404, "body": "Not Found"}


class FakeClient:
    def send(self, server: FakeServer, request: dict):
        print(f"Request: {request}")
        response = server.handle_request(request)
        print(f"Response: {response}\n")


if __name__ == "__main__":
    server = FakeServer()
    client = FakeClient()

    get_users_request = {"method": "GET", "target": "/users"}
    add_user_request = {"method": "POST", "target": "/users", "body": {"id": 3, "name": "Ola"}}
    not_found_request = {"method": "GET", "target": "/unknown"}

    client.send(server, get_users_request)
    client.send(server, add_user_request)
    client.send(server, get_users_request)
    client.send(server, not_found_request)
