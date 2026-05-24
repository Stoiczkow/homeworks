from aiohttp import web

# To jest "handler" zapytania. Musi to być korutyna (oznaczona async def).
# Otrzymuje obiekt `request` jako argument.
async def handle_hello(request):
    """
    Handler, który obsługuje zapytania GET na ścieżce '/'.
    """
    # Dostęp do parametrów zapytania (np. /?name=Anna)
    # Używamy .get() aby bezpiecznie pobrać wartość lub domyślną.
    name = request.query.get("name", "Świecie")
    
    # Zwracamy odpowiedź. web.Response jest domyślnie tekstowe (text/plain).
    # Możemy ustawić content_type na 'text/html' jeśli chcemy.
    return web.Response(text=f"Witaj, {name}!", content_type='text/html')

# Tworzymy instancję aplikacji
app = web.Application()

# Dodajemy "trasę" (route), która mapuje metodę HTTP (GET) i ścieżkę (/)
# na nasz handler (handle_hello)

app.router.add_get("/", handle_hello)
# Uruchamiamy serwer
if __name__ == "__main__":
    print("Uruchamiam serwer na [http://127.0.0.1:8080]"
    "(http://127.0.0.1:8080)")
        
# web.run_app() automatycznie tworzy i zarządza pętlą zdarzeń asyncio
web.run_app(app, host="127.0.0.1", port=8080)