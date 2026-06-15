"""
CRUD API – Produkty (POST)
"""

import asyncio
from aiohttp import web
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)  # cena w groszach

DATABASE_URL = "sqlite+aiosqlite:///./products.db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_product(request):
    session: AsyncSession = SessionLocal()

    data = await request.json()
    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return web.json_response(
            {"error": "Brak wymaganych pól: name, price"},
            status=400
        )

    produkt = Product(name=name, price=price)
    session.add(produkt)
    await session.commit()
    await session.refresh(produkt)

    return web.json_response(
        {
            "id": produkt.id,
            "name": produkt.name,
            "price": produkt.price
        },
        status=201
    )


async def create_app():
    await init_db()

    app = web.Application()
    app.router.add_post("/products", create_product)
    return app


def main():
    web.run_app(create_app(), host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
