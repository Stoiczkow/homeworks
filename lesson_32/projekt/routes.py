"""
Zadanie 19 – Refaktoryzacja: osobny plik routes.py
Wszystkie trasy rejestrowane przez setup_routes(app).
"""
import asyncio
from datetime import datetime

from aiohttp import web
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from database import AsyncSessionLocal
from models import Account, Product, User


# ── Zadania 2 + 3 + 8 – strony HTML ────────────────────────────────────────
async def index(request: web.Request) -> web.Response:
    return web.Response(text='<h1>Witaj na mojej stronie!</h1>', content_type='text/html')


async def witaj(request: web.Request) -> web.Response:
    imie = request.match_info['imie']
    # Zadanie 8 – zakaz dla admina
    if imie.lower() == 'admin':
        raise web.HTTPForbidden(text='Dostęp dla admina zabroniony')
    return web.Response(text=f'Witaj, {imie}!')


# ── Zadania 4 + 5 + 6 – API JSON ────────────────────────────────────────────
async def api_status(request: web.Request) -> web.Response:
    return web.json_response({
        'status': 'OK',
        'server_time': datetime.now().isoformat(),
    })


async def api_search(request: web.Request) -> web.Response:
    q = request.query.get('q')
    if not q:
        return web.json_response({'błąd': 'Brak parametru q'}, status=400)
    return web.json_response({'szukana_fraza': q})


async def api_echo(request: web.Request) -> web.Response:
    data = await request.json()
    return web.json_response(data)


# ── Zadania 9-11, 14-15, 17 – CRUD Produkty ─────────────────────────────────
async def products_list(request: web.Request) -> web.Response:
    # Zadanie 17 – paginacja
    try:
        page = int(request.query.get('page', 1))
        limit = int(request.query.get('limit', 10))
    except ValueError:
        raise web.HTTPBadRequest(text='page i limit muszą być liczbami całkowitymi')

    offset = (page - 1) * limit
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Product).offset(offset).limit(limit)
        )
        produkty = result.scalars().all()

    return web.json_response([
        {'id': p.id, 'name': p.name, 'price': p.price} for p in produkty
    ])


async def products_create(request: web.Request) -> web.Response:
    data = await request.json()
    name = data.get('name')
    price = data.get('price')
    if not name or price is None:
        raise web.HTTPBadRequest(text='Wymagane pola: name, price')

    async with AsyncSessionLocal() as session:
        produkt = Product(name=name, price=price)
        session.add(produkt)
        await session.commit()
        await session.refresh(produkt)

    return web.json_response(
        {'id': produkt.id, 'name': produkt.name, 'price': produkt.price},
        status=201,
    )


async def _get_product_or_404(session, product_id: int) -> Product:
    result = await session.execute(select(Product).where(Product.id == product_id))
    produkt = result.scalar_one_or_none()
    if produkt is None:
        raise web.HTTPNotFound(text=f'Produkt o ID={product_id} nie istnieje')
    return produkt


async def products_detail(request: web.Request) -> web.Response:
    # Zadanie 20 – JOIN z User
    product_id = int(request.match_info['id'])
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Product).options(joinedload(Product.user)).where(Product.id == product_id)
        )
        produkt = result.scalar_one_or_none()
        if produkt is None:
            raise web.HTTPNotFound(text=f'Produkt o ID={product_id} nie istnieje')

    return web.json_response({
        'id': produkt.id,
        'name': produkt.name,
        'price': produkt.price,
        'creator': produkt.user.name if produkt.user else None,
    })


async def products_update(request: web.Request) -> web.Response:
    product_id = int(request.match_info['id'])
    data = await request.json()

    async with AsyncSessionLocal() as session:
        produkt = await _get_product_or_404(session, product_id)
        if 'name' in data:
            produkt.name = data['name']
        if 'price' in data:
            produkt.price = data['price']
        await session.commit()
        await session.refresh(produkt)

    return web.json_response({'id': produkt.id, 'name': produkt.name, 'price': produkt.price})


async def products_delete(request: web.Request) -> web.Response:
    product_id = int(request.match_info['id'])

    async with AsyncSessionLocal() as session:
        produkt = await _get_product_or_404(session, product_id)
        await session.delete(produkt)
        await session.commit()

    return web.Response(status=204)


# ── Zadanie 16 – Transakcja bankowa ─────────────────────────────────────────
async def transfer(request: web.Request) -> web.Response:
    data = await request.json()
    from_id = data.get('from_id')
    to_id = data.get('to_id')
    amount = data.get('amount')

    if not all([from_id, to_id, amount]):
        raise web.HTTPBadRequest(text='Wymagane pola: from_id, to_id, amount')

    async with AsyncSessionLocal() as session:
        async with session.begin():
            r1 = await session.execute(select(Account).where(Account.id == from_id))
            r2 = await session.execute(select(Account).where(Account.id == to_id))
            konto_from = r1.scalar_one_or_none()
            konto_to = r2.scalar_one_or_none()

            if not konto_from or not konto_to:
                raise web.HTTPNotFound(text='Nie znaleziono jednego z kont')

            if konto_from.balance < amount:
                raise web.HTTPBadRequest(
                    text=f'Niewystarczające środki: saldo={konto_from.balance}, żądanie={amount}'
                )

            konto_from.balance -= amount
            konto_to.balance += amount
            # session.begin() automatycznie commituje lub rollbackuje

    return web.json_response({
        'message': f'Przelew {amount} gr z konta {from_id} na {to_id} zakończony sukcesem'
    })


# ── Zadanie 18 – Mock AI API ─────────────────────────────────────────────────
async def chat(request: web.Request) -> web.Response:
    data = await request.json()
    prompt = data.get('prompt', '')
    await asyncio.sleep(3)  # symulacja długiego przetwarzania przez AI
    return web.json_response({
        'response': f"Otrzymałem twój prompt: '{prompt}' i przetworzyłem go."
    })


# ── Zadanie 19 – rejestracja tras ────────────────────────────────────────────
def setup_routes(app: web.Application) -> None:
    app.router.add_get('/', index)
    app.router.add_get('/witaj/{imie}', witaj)
    app.router.add_get('/api/status', api_status)
    app.router.add_get('/api/search', api_search)
    app.router.add_post('/api/echo', api_echo)
    app.router.add_get('/products', products_list)
    app.router.add_post('/products', products_create)
    app.router.add_get('/products/{id}', products_detail)
    app.router.add_put('/products/{id}', products_update)
    app.router.add_patch('/products/{id}', products_update)
    app.router.add_delete('/products/{id}', products_delete)
    app.router.add_post('/transfer', transfer)
    app.router.add_post('/api/v1/chat', chat)
