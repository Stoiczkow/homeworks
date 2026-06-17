from aiohttp import web
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy import String, Integer, select

DB_URL = "sqlite+aiosqlite:///lesson32.db"


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }


async def init_db(app: web.Application):
    print("Inicjalizuję bazę danych...")

    engine = create_async_engine(DB_URL, echo=True)

    session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    app["db_engine"] = engine
    app["db_session_factory"] = session_factory

    print("Baza danych gotowa.")


async def close_db(app: web.Application):
    print("Zamykam połączenie z bazą danych...")

    engine = app["db_engine"]
    await engine.dispose()


async def create_product(request: web.Request):
    try:
        data = await request.json()
        name = data["name"]
        price = data["price"]
    except Exception:
        raise web.HTTPBadRequest(text="Oczekiwano JSON z polami 'name' i 'price'")

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            new_product = Product(name=name, price=price)
            session.add(new_product)

            await session.flush()

            product_data = new_product.to_dict()

    return web.json_response(product_data, status=201)

async def get_products(request: web.Request):
    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        stmt = select(Product)
        result = await session.execute(stmt)
        products = result.scalars().all()

        products_data = [product.to_dict() for product in products]

    return web.json_response(products_data)



async def get_product(request: web.Request):
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(text="ID produktu musi być liczbą")

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        stmt = select(Product).where(Product.id == product_id)
        result = await session.execute(stmt)
        product = result.scalar_one_or_none()

        if product is None:
            raise web.HTTPNotFound(text="Produkt nie istnieje")

        return web.json_response(product.to_dict())
    
async def update_product(request: web.Request):
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(text="ID produktu musi być liczbą")

    try:
        data = await request.json()
    except Exception:
        raise web.HTTPBadRequest(text="Oczekiwano poprawnego JSON-a")

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            stmt = select(Product).where(Product.id == product_id)
            result = await session.execute(stmt)
            product = result.scalar_one_or_none()

            if product is None:
                raise web.HTTPNotFound(text="Produkt nie istnieje")

            if "name" in data:
                product.name = data["name"]

            if "price" in data:
                product.price = data["price"]

            await session.flush()

            product_data = product.to_dict()

    return web.json_response(product_data)

async def delete_product(request: web.Request):
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(text="ID produktu musi być liczbą")

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            stmt = select(Product).where(Product.id == product_id)
            result = await session.execute(stmt)
            product = result.scalar_one_or_none()

            if product is None:
                raise web.HTTPNotFound(text="Produkt nie istnieje")

            await session.delete(product)

    return web.Response(status=204)

def create_app():
    app = web.Application()

    app.router.add_post("/products", create_product)
    app.router.add_get("/products", get_products)
    app.router.add_get("/products/{id}", get_product)
    app.router.add_patch("/products/{id}", update_product)
    app.router.add_delete("/products/{id}", delete_product)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host="127.0.0.1", port=8080)