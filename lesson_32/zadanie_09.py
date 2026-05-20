from aiohttp import web
from sqlalchemy import Integer, String
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DB_URL = "sqlite+aiosqlite:///./zadanie_09.db"


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "price": self.price}


async def init_db(app: web.Application) -> None:
    engine = create_async_engine(DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    app["db_engine"] = engine
    app["db_session_factory"] = async_sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )


async def close_db(app: web.Application) -> None:
    await app["db_engine"].dispose()


async def create_product(request: web.Request) -> web.Response:
    try:
        data = await request.json()
        name = data["name"]
        price = int(data["price"])
    except (KeyError, ValueError, TypeError):
        raise web.HTTPBadRequest(text="Oczekiwano JSON z 'name' (str) i 'price' (int)")

    session_factory: async_sessionmaker[AsyncSession] = request.app["db_session_factory"]
    async with session_factory() as session:
        async with session.begin():
            product = Product(name=name, price=price)
            session.add(product)
            await session.flush()
            result = product.to_dict()
    return web.json_response(result, status=201)


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_post("/products", create_product)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), host="127.0.0.1", port=8080)