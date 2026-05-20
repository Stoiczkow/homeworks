from aiohttp import web
from sqlalchemy import Integer, String, select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DB_URL = "sqlite+aiosqlite:///./zadanie_17.db"


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
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with factory() as session:
        async with session.begin():
            session.add_all([
                Product(name=f"Produkt {i}", price=i * 100) for i in range(1, 36)
            ])
    app["db_engine"] = engine
    app["db_session_factory"] = factory


async def close_db(app: web.Application) -> None:
    await app["db_engine"].dispose()


async def list_products(request: web.Request) -> web.Response:
    try:
        page = max(1, int(request.query.get("page", "1")))
        limit = max(1, min(100, int(request.query.get("limit", "10"))))
    except ValueError:
        raise web.HTTPBadRequest(text="page i limit muszą być liczbami")
    offset = (page - 1) * limit

    async with request.app["db_session_factory"]() as session:
        stmt = select(Product).order_by(Product.id).offset(offset).limit(limit)
        result = await session.execute(stmt)
        products = result.scalars().all()
    return web.json_response({
        "page": page,
        "limit": limit,
        "items": [p.to_dict() for p in products],
    })


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get("/products", list_products)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), host="127.0.0.1", port=8080)