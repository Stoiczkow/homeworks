import asyncio
from datetime import datetime
from json import JSONDecodeError

from aiohttp import web
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from models import Product, Account

# 2. (Proste) Aiohttp - Strona powitalna: Stwórz prosty serwer aiohttp , który na ścieżce
# / zwróci odpowiedź web.Response z tekstem <h1>Witaj na mojej stronie!</h1> i
# poprawnym content_type='text/html' 

async def handle_home(request: web.Request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>", content_type='text/html'
        )
    
# 3. (Proste) Aiohttp - Dynamiczne powitanie: Rozbuduj serwer z zadania 2. Dodaj
# handler na ścieżce /witaj/{imie} . Handler ma odczytać imie z request.match_info i
# zwrócić tekst "Witaj, {imie}!"

# 8. (Proste) Aiohttp - Obsługa błędu: W handlerze z zadania 3 ( /witaj/{imie} ), dodaj
# sprawdzenie. Jeśli imie to "admin", podnieś wyjątek raise
# web.HTTPForbidden(text="Dostęp dla admina zabroniony")

async def handle_hello(request: web.Request):
    name = request.match_info.get("name")
    if name == 'admin':
        raise web.HTTPForbidden(text="Dostęp dla admina zabroniony")
    return web.Response(
        text=f"<h1>Witaj na mojej stronie, {name}!</h1>", content_type='text/html'
        )

# 4. (Proste) Aiohttp - Proste API JSON: Stwórz handler na ścieżce /api/status , który
# metodą GET zwróci odpowiedź JSON: {"status": "OK", "server_time": "..."} (użyj
# datetime.now() do czasu i web.json_response )

async def handle_status(request: web.Request):
    return web.json_response({
        "status": "OK", 
         "server_time": datetime.now().isoformat()
         })

# 5. (Proste) Aiohttp - Odczyt query params: Stwórz handler /api/search , który odczyta
# z request.query parametr q . Jeśli parametr istnieje, zwróć JSON {"szukana_fraza":
# "wartosc_q"} . Jeśli nie, zwróć {"błąd": "Brak parametru q"} .

async def handle_search(request: web.Request):
    q_param = request.query.get("q", "")
    if q_param:
        return web.json_response({
            "szukana_fraza": q_param
        })
    else:
        return web.json_response({
            "blad": "Brak parametru q"
        })
        
# 6. ✏ (Proste) Aiohttp - Odczyt JSON (echo): Stwórz handler POST na ścieżce /api/echo .
# Handler ma odczytać dane JSON wysłane w ciele ( await request.json() ) i odesłać je z
# powrotem w odpowiedzi web.json_response 

async def handle_echo(request: web.Request):
    data = await request.json()
    
    return web.json_response(data)
    
# 9. (Challenge) CRUD API - Produkty (POST): Używając aplikacji z przykładu (z gotową
# integracją SQLAlchemy ):
# 1. Dodaj model Product (z zadania 7) do pliku.
# 2. Pamiętaj o dodaniu go do Base.metadata.create_all .
# 3. Stwórz handler POST na /products , który odczyta name i price z JSON, stworzy
# nowy obiekt Product i zapisze go w bazie.
# 4. Handler powinien zwrócić dane nowego produktu (wraz z ID) i status 201.

async def add_product(request: web.Request):
    try:
        data = await request.json()
    except JSONDecodeError:
        raise web.HTTPBadRequest(
            text={"error": "Invalid data"}, type="application/json"
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:        

        async with session.begin():
            new_product = Product(name=data["name"], price=data["price"], user_id=data["user_id"])    
            session.add(new_product)    

    return web.json_response(new_product.to_dict(), status=201)

# 10. (Challenge) CRUD API - Produkty (GET Lista): Bazując na zadaniu 9, stwórz handler
# GET na /products , który pobierze wszystkie produkty z bazy danych ( select(Product) )
# i zwróci je jako listę obiektów JSON.

# 17. (Challenge) Aiohttp - Paginacja: (Znacie paginację z Django). Zmodyfikuj handler GET
# /products (zadanie 10). Handler ma przyjmować page (domyślnie 1) i limit (domyślnie 10) z
# request.query. Zmodyfikuj zapytanie SQLAlchemy, aby użyć .offset() i .limit() do zwrócenia
# tylko jednej "strony" wyników

async def get_all_products(request: web.Request):
    page = int(request.query.get("page", 1))
    limit = int(request.query.get("limit", 10))
    
    offset = (page - 1) * limit
    
    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        result = await session.execute(
            select(Product)
            .offset(offset)
            .limit(limit)
            )

        products = result.scalars().all()

    return web.json_response([
        product.to_dict() for product in products
        ])

# 11. (Challenge) CRUD API - Produkty (GET Pojedynczy): Bazując na zadaniu 10, stwórz
# handler GET na /products/{id} . Handler ma pobrać ID z match_info , znaleźć produkt
# w bazie ( select(Product).where(Product.id == product_id) ). Jeśli produkt istnieje,
# zwróć jego dane JSON. Jeśli nie, podnieś wyjątek web.HTTPNotFound() .

# 20. (Challenge) SQLAlchemy Async - JOIN: (Znacie JOIN). Dodaj do modelu Product
# relację ForeignKey do User (twórca produktu). Zmodyfikuj handler GET
# /products/{id} , aby pobierał produkt wraz z nazwą użytkownika, który go stworzył
# (używając select(Product, User).join(User) lub
# options(joinedload(Product.user)) - opcja dla ambitnych)

async def get_product(request: web.Request):
    product_id = int(request.match_info.get("id"))
    
    session_factory = request.app["db_session_factory"]
    
    async with session_factory() as session:
        result = await session.execute(
            select(Product)
            .options(joinedload(Product.user))
            .where(Product.id == product_id)
            )

        product = result.scalar_one_or_none()

        if product is None:
            raise web.HTTPNotFound(text="Product not found")
        
        return web.json_response(product.to_dict())

# 14. (Challenge) CRUD API - Produkty (PUT/PATCH): Bazując na zadaniu 11, stwórz
# handler PUT (lub PATCH ) na /products/{id} . Handler ma:
# 1. Pobrać produkt (i zwrócić 404, jeśli go nie ma).
# 2. Odczytać nowe dane name i/lub price z await request.json() .
# 3. Zaktualizować atrybuty obiektu produktu.
# 4. Zapisać zmiany w bazie (w ramach sesji i transakcji).
# 5. Zwrócić zaktualizowane dane produktu

async def update_product(request: web.Request):
    product_id = int(request.match_info.get("id"))
    
    try:
        data = await request.json()
    except Exception:
        raise web.HTTPBadRequest(text="Invalid JSON")
        
    session_factory = request.app["db_session_factory"]
    
    async with session_factory() as session:
        result = await session.execute(
            select(Product).where(Product.id == product_id)
            )
        
        product = result.scalar_one_or_none()
        
        if product is None:
            raise web.HTTPNotFound(text="Product not found", status=404)
        
        if "name" in data:
            product.name = data["name"]
            
        if "price" in data:
            product.price = data["price"]
            
        await session.commit()
        
    return web.json_response(product.to_dict())            
    

# 15. Challenge) CRUD API - Produkty (DELETE): Bazując na zadaniu 11, stwórz handler
# DELETE na /products/{id} . Handler ma pobrać obiekt, usunąć go ( await
# session.delete(product) ) i zwrócić pustą odpowiedź ze statusem 204 (No Content).

async def delete_product(request: web.Request):
    product_id = request.match_info.get("id")
    
    session_factory = request.app["db_session_factory"]
    
    async with session_factory() as session:
        result = await session.execute(
            select(Product).where(Product.id == int(product_id))
            )

        product = result.scalar_one_or_none()

        if product is None:
            raise web.HTTPNotFound(text="Product not found", status=404)
        
        
        await session.delete(product)
        await session.commit()
        
    return web.json_response(status=204)
    
# 16. (Challenge) SQLAlchemy Async - Transakcja: (Znacie transakcje). Stwórz dwa
# modele: Account (z polem balance: Mapped[int] ) i handler POST /transfer . Handler
# ma przyjąć JSON { "from_id": 1, "to_id": 2, "amount": 100 } . W ramach jednej
# transakcji ( async with session.begin(): ):
# 1. Pobierz oba konta.
# 2. Sprawdź, czy na koncie from_id jest wystarczająco środków.
# 3. Odejmij amount z from_id i dodaj do to_id .
# 4. Jeśli coś pójdzie nie tak (np. brak środków), transakcja powinna zostać automatycznie
# wycofana (dzięki session.begin() i wyjątkowi)

async def transfer(request: web.Request):
    session_factory = request.app["db_session_factory"]
    
    try:
        data = await request.json()
    except Exception:
        raise web.HTTPBadRequest(text="Invalid JSON")
    
    amount = int(data["amount"])
    from_id = int(data["from_id"])
    to_id = int(data["to_id"])
    
    async with session_factory() as session:        
        async with session.begin():
            
            result_1 = await session.execute(
                select(Account).where(Account.id == from_id)
                )
            account_from = result_1.scalar_one_or_none()
            
            result_2 = await session.execute(
                select(Account).where(Account.id == to_id)
                )
            account_to = result_2.scalar_one_or_none()
            
            if account_from is None or account_to is None:
                raise web.HTTPNotFound(text="Account not found")
                
            if account_from.balance < amount:
                raise web.HTTPBadRequest(text="Insufficient funds")
            
            account_from.balance -= amount
            account_to.balance += amount
            
    return web.json_response({
        "status": "transfer completed",
        "from": from_id,
        "to": to_id,
        "amount": amount
    }, status=201)
        
async def get_all_accounts(request: web.Request):
    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        result = await session.execute(select(Account))

        accounts = result.scalars().all()

    products = [account.to_dict() for account in accounts]

    return web.json_response(products)

# 18. (Challenge) Aiohttp - Mock API dla AI: Stwórz handler POST na /api/v1/chat .
# Handler ma:
# 1. Oczekiwać JSON-a: {"prompt": "jakaś treść"} .
# 2. Symulować długie przetwarzanie przez AI: await asyncio.sleep(3) .
# 3. Zwrócić odpowiedź JSON: {"response": f"Otrzymałem twój prompt: '{prompt_text}' i
# przetworzyłem go."}.
# (To ćwiczenie pokazuje, jak serwer aiohttp radzi sobie z długimi zadaniami I/O, nie
# blokując innych zapytań).

async def chat(request: web.Request):    
    try:
        data = await request.json()
        prompt_text = data["prompt"]
    except Exception:
        raise web.HTTPBadRequest(text="Invalid JSON") 
      
    await asyncio.sleep(3)
    
    return web.json_response({
        "response": f"Otrzymałem twój prompt: '{prompt_text}' i przetworzyłem go."
        })