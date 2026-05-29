"""
Lesson 32 – aiohttp + SQLAlchemy Async
Wymagania: pip install aiohttp aiosqlite sqlalchemy

Uruchomienie: python app.py
Serwer nasłuchuje na http://localhost:8080
"""
from aiohttp import web

from database import engine
from models import Base
from routes import setup_routes


async def on_startup(app: web.Application) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Baza danych zainicjalizowana.")


def create_app() -> web.Application:
    app = web.Application()
    app.on_startup.append(on_startup)
    setup_routes(app)  # Zadanie 19 – trasy w osobnym pliku
    return app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app, host='localhost', port=8080)
