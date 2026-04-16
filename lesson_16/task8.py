# Symulacja Klient-Serwer: Stwórz prostą symulację interakcji Klient-Serwer przy użyciu klas.
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
# Napisz klasę FakeClient z metodą send(server, request) , która "wysyła" żądanie do obiektu serwera i drukuje otrzymaną odpowiedź.
# Przetestuj scenariusze: pobranie wszystkich użytkowników, dodanie nowego
# użytkownika i próbę dostępu do nieistniejącego zasobu.

class FakeServer:
    def __init__(self):
        self.db = {
            "users": [
                {"id": 1, "name": "Jan"},
                {"id": 2, "name": "Anna"}
            ]
        }

    def handle_request(self, request):
        if request["method"] == "GET" and request["target"] == "/users":
            return {
                "status": 200,
                "body": self.db["users"]
            }
        
        if request["method"] == "POST" and request["target"] == "/users":
            self.db["users"].append(request["body"])
            return {
                "status": 201,
                "body": request["body"]
            }
        
        return {
            "status": 404,
            "body": "Not Found"
        }
class FakeClient:
    def send(self, server, request):
        response = server.handle_request(request)
        print(response)

server = FakeServer()
client = FakeClient()

request_1 = {
    "method": "GET",
    "target": "/users"
}

request_2 = {
    "method": "POST",
    "target": "/users"
}

request_3 = {
    "method": "GET",
    "target": "/fake"
}

client.send(server, request_1)
client.send(server, request_2)
client.send(server, request_1)
client.send(server, request_3)