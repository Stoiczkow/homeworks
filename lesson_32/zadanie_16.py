from aiohttp import web
from sqlalchemy import Integer, select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DB_URL = "sqlite+aiosqlite:///./zadanie_16.db"


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(Integer)

    def to_dict(self) -> dict:
        return {"id": self.id, "balance": self.balance}


async def init_db(app: web.Application) -> None:
    engine = create_async_engine(DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with factory() as session:
        async with session.begin():
            session.add_all([Account(id=1, balance=1000), Account(id=2, balance=500)])
    app["db_engine"] = engine
    app["db_session_factory"] = factory


async def close_db(app: web.Application) -> None:
    await app["db_engine"].dispose()


async def transfer(request: web.Request) -> web.Response:
    try:
        data = await request.json()
        from_id = int(data["from_id"])
        to_id = int(data["to_id"])
        amount = int(data["amount"])
    except (KeyError, ValueError, TypeError):
        raise web.HTTPBadRequest(text="Oczekiwano JSON: from_id, to_id, amount")
    if amount <= 0:
        raise web.HTTPBadRequest(text="Kwota musi być dodatnia")
    if from_id == to_id:
        raise web.HTTPBadRequest(text="Konta źródłowe i docelowe muszą się różnić")

    async with request.app["db_session_factory"]() as session:
        async with session.begin():
            result = await session.execute(
                select(Account).where(Account.id.in_([from_id, to_id]))
            )
            accounts = {a.id: a for a in result.scalars().all()}
            if from_id not in accounts or to_id not in accounts:
                raise web.HTTPNotFound(text="Konto nie istnieje")
            src, dst = accounts[from_id], accounts[to_id]
            if src.balance < amount:
                raise web.HTTPBadRequest(text="Brak wystarczających środków")
            src.balance -= amount
            dst.balance += amount
            response = {"from": src.to_dict(), "to": dst.to_dict()}
    return web.json_response(response)


async def list_accounts(request: web.Request) -> web.Response:
    async with request.app["db_session_factory"]() as session:
        result = await session.execute(select(Account))
        accounts = result.scalars().all()
    return web.json_response([a.to_dict() for a in accounts])


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get("/accounts", list_accounts)
    app.router.add_post("/transfer", transfer)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), host="127.0.0.1", port=8080)