# 8. Symulacja Klient-Serwer: Stwórz prostą symulację interakcji Klient-Serwer przy użyciu
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

class FakeServer:
    def __init__(self):
        self.db = {
            "users": [{"id": 1, "name": "Jan"},
                      {"id": 2, "name": "Anna"}]
        }
        
    def handle_request(self, request: dict):
        if request["target"] == "/users":
            if request["method"] == "GET":
                return {
                    "code": 200,
                    "body": self.db["users"]
                }
            elif request["method"] == "POST": 
                self.db["users"].append(request["body"])
                return {                
                    "code": 201,
                    "status": "Created",
                }        
        return {                
            "code": 404,
            "status": "Not Found",
        }

class FakeClient:
    def send(self, server, request):
        response = server.handle_request(request)
        
        print("=== Response from server ===")
        print(f"Code: {response.get("code")}")
        
        if "status" in response:
            print(f"Status: {response.get("status")}")
            
        if "body" in response:
            print("Body:")
            print(response.get("body"))
        
server = FakeServer()
client = FakeClient()

request_1 = {
    "method": "GET",
    "target": "/users"
}
request_2 = {
    "method": "POST",
    "target": "/users",
    "body": {"id": 3, "name": "Hania"}
}
request_3 = {
    "method": "GET",
    "target": "/posts"
}

client.send(server, request_1)
client.send(server, request_2)
client.send(server, request_3)
                                    
            