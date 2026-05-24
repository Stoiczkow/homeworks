import os
from aiohttp import web
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from models import Base
from handlers import (
    add_product, 
    get_all_products, 
    get_single_product, 
    update_product,
    delete_product
    )

load_dotenv()

DB_URL = os.getenv(
    "DB_URL", "postgresql+asyncpg://postgres:postgres@localhost/aio_test_db"
)


async def init_db(app: web.Application):
    """Sygnał on_startup: tworzy silnik i sessionmaker."""
    print(f"Inicjalizuję połączenie z bazą danych: {DB_URL}")

    engine = create_async_engine(DB_URL, echo=True)

    async_session_factory = async_sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    # # 3. (Opcjonalnie) Stworzenie tabel przy starcie (tylko dla deweloperki!)
    async with engine.begin() as conn:
        # Używamy run_sync do uruchomienia synchronicznej metody create_all
        await conn.run_sync(Base.metadata.create_all)

    # 4. Przechowujemy fabrykę sesji w obiekcie aplikacji
    app["db_session_factory"] = async_session_factory
    print("Połączenie z bazą danych gotowe.")


async def close_db(app: web.Application):
    """Sygnał on_cleanup: zamyka silnik."""
    # SQLAlchemy 2.0+ zaleca użycie `engine.dispose()` w kontekście async
    # W tym prostym przypadku, `web.run_app` często zarządza tym
    # pośrednio, ale jawne czyszczenie jest bezpieczniejsze.
    print("Zamykam pulę połączeń z bazą danych.")
    # Jeśli przechowywaliśmy engine w app:
    # if 'db_engine' in app:
    #     await app['db_engine'].dispose()
    pass


# --- Tworzenie Aplikacji ---


def create_app():
    app = web.Application()

    app.router.add_post("/products", add_product)
    app.router.add_get("/products", get_all_products)
    app.router.add_get("/products/{id}", get_single_product)
    app.router.add_put("/products/{id}", update_product)
    app.router.add_patch("/products/{id}", update_product)
    app.router.add_delete("/products/{id}", delete_product)

    app.on_startup.append(init_db)

    return app


if __name__ == "__main__":
    app = create_app()
    print(f"--- Start serwera na http://127.0.0.1:8080 ---")
    print(f"--- Upewnij się, że baza danych na {DB_URL} działa i jest utworzona. ---")
    web.run_app(app, port=8080)