class FakeServer:
    def __init__(self):
        self.db = {
            "users": [
                {"id": 1, "name": "Jan"},
                {"id": 2, "name": "Anna"}
            ]
        }

    def handle_request(self, request: dict) -> dict:
        method = request.get("method", "").upper()
        target = request.get("target", "")
        body   = request.get("body", {})

        if method == "GET" and target == "/users":
            return {
                "status": 200,
                "status_text": "OK",
                "body": self.db["users"]
            }

        if method == "POST" and target == "/users":
            new_id   = max(u["id"] for u in self.db["users"]) + 1
            new_user = {"id": new_id, **body}
            self.db["users"].append(new_user)
            return {
                "status": 201,
                "status_text": "Created",
                "body": new_user
            }

        return {
            "status": 404,
            "status_text": "Not Found",
            "body": {"error": f"Resource '{target}' not found"}
        }


class FakeClient:
    def send(self, server: FakeServer, request: dict) -> dict:
        method = request.get("method", "?").upper()
        target = request.get("target", "?")

        print(f">>> {method} {target}")
        if request.get("body"):
            print(f"    Body: {request['body']}")

        response = server.handle_request(request)

        print(f"<<< {response['status']} {response['status_text']}")
        print(f"    Body: {response['body']}")
        print()

        return response

server = FakeServer()
client = FakeClient()


print("[ Scenariusz 1: GET /users ]")
client.send(server, {"method": "GET", "target": "/users"})

print("[ Scenariusz 2: POST /users ]")
client.send(server, {
    "method": "POST",
    "target": "/users",
    "body": {"name": "Piotr"}
})

print("[ Scenariusz 3: GET /users (po dodaniu) ]")
client.send(server, {"method": "GET", "target": "/users"})

print("[ Scenariusz 4: GET /products (404) ]")
client.send(server, {"method": "GET", "target": "/products"})
