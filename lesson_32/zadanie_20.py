from aiohttp import web
from sqlalchemy import ForeignKey, Integer, String, select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    joinedload,
    mapped_column,
    relationship,
)

DB_URL = "sqlite+aiosqlite:///./zadanie_20.db"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "app_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)

    products: Mapped[list["Product"]] = relationship(back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("app_users.id"))

    user: Mapped[User] = relationship(back_populates="products")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "user_id": self.user_id,
            "username": self.user.username if self.user else None,
        }


async def init_db(app: web.Application) -> None:
    engine = create_async_engine(DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with factory() as session:
        async with session.begin():
            anna = User(username="anna")
            piotr = User(username="piotr")
            session.add_all([anna, piotr])
            await session.flush()
            session.add_all([
                Product(name="Klawiatura", price=14999, user_id=anna.id),
                Product(name="Mysz", price=4999, user_id=anna.id),
                Product(name="Monitor", price=99900, user_id=piotr.id),
            ])
    app["db_engine"] = engine
    app["db_session_factory"] = factory


async def close_db(app: web.Application) -> None:
    await app["db_engine"].dispose()


async def get_product(request: web.Request) -> web.Response:
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(text="ID musi być liczbą")

    async with request.app["db_session_factory"]() as session:
        stmt = (
            select(Product)
            .options(joinedload(Product.user))
            .where(Product.id == product_id)
        )
        result = await session.execute(stmt)
        product = result.scalar_one_or_none()
        if product is None:
            raise web.HTTPNotFound(text=f"Brak produktu o id={product_id}")
        return web.json_response(product.to_dict())


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get("/products/{id}", get_product)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), host="127.0.0.1", port=8080)