class FakeServer:
    def __init__(self):
        self.db = {
            "users": [
                {"id": 1, "name": "Jan"},
                {"id": 2, "name": "Anna"},
            ]
        }

    def handle_request(self, request: dict) -> dict:
        method = request.get("method")
        target = request.get("target")

        if method == "GET" and target == "/users":
            return {
                "status": 200,
                "body": self.db["users"]
            }

        if method == "POST" and target == "/users":
            nowy_uzytkownik = request.get("body", {})
            nowy_uzytkownik["id"] = len(self.db["users"]) + 1
            self.db["users"].append(nowy_uzytkownik)
            return {
                "status": 201,
                "body": nowy_uzytkownik
            }

        return {
            "status": 404,
            "body": "Not Found"
        }


class FakeClient:
    def send(self, server: FakeServer, request: dict):
        response = server.handle_request(request)
        print(f"Status: {response['status']}")
        print(f"Body: {response['body']}")
        print()


server = FakeServer()
client = FakeClient()

print("--- GET /users ---")
client.send(server, {"method": "GET", "target": "/users"})

print("--- POST /users ---")
client.send(server, {
    "method": "POST",
    "target": "/users",
    "body": {"name": "Piotr"}
})

print("--- GET /users (po dodaniu) ---")
client.send(server, {"method": "GET", "target": "/users"})

print("--- GET /nieistniejacy ---")
client.send(server, {"method": "GET", "target": "/nieistniejacy"})
