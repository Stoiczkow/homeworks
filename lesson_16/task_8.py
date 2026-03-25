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
# użytkownika i próbę dostępu do nieistniejącego zasobu.

class FakeServer:
    def __init__(self):
        self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2, "name": "Anna"}]}
        
    def handle_request(self, request: dict) -> dict:
        method = request.get("method")
        target = request.get("target")
        
        if method == "GET" and target == "/users":
            return {"status_code": 200, "body": self.db["users"]}
        
        elif method == "POST" and target == "/users":
            new_user = request.get("body")
            if new_user:
                new_user["id"] = len(self.db["users"]) + 1
                self.db["users"].append(new_user)
                return {"status_code": 201, "body": new_user}
            else:
                return {"status_code": 400, "body": "Bad Request"}
        
        else:
            return {"status_code": 404, "body": "Not Found"}

class FakeClient:
    def send(self, server: FakeServer, request: dict):
        response = server.handle_request(request)
        print(f"Response: {response}")

# Testowanie scenariuszy
server = FakeServer()
client = FakeClient()
# Pobranie wszystkich użytkowników
get_request = {"method": "GET", "target": "/users"}
client.send(server, get_request)
# Dodanie nowego użytkownika
post_request = {"method": "POST", "target": "/users", "body": {"name": "Katarzyna"}}
client.send(server, post_request)
# Próba dostępu do nieistniejącego zasobu
invalid_request = {"method": "GET", "target": "/invalid"}
client.send(server, invalid_request)

