# 3. ✏ (Proste) Aiohttp - Dynamiczne powitanie: Rozbuduj serwer z zadania 2. Dodaj
# handler na ścieżce /witaj/{imie} . Handler ma odczytać imie z request.match_info i
# zwrócić tekst "Witaj, {imie}!".



from aiohttp import web

async def home(request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
    )

async def handle_hello(request):
   
    name = request.match_info["name"]
    return web.Response(text=f"Witaj, {name}!", content_type='text/html')

app = web.Application()

app.router.add_get("/", home)
app.router.add_get("/hello/{name}", handle_hello)

if __name__ == "__main__":
    print("Uruchamiam serwer na [http://127.0.0.1:8080] (http://127.0.0.1:8080)")
    web.run_app(app, host="127.0.0.1", port=8080)