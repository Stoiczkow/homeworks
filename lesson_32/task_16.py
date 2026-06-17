from aiohttp import web
from sqlalchemy import Integer, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)


DB_URL = "sqlite+aiosqlite:///lesson32_transfer.db"


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "balance": self.balance,
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

    # Tworzymy testowe konta tylko wtedy, gdy tabela jest pusta
    async with session_factory() as session:
        result = await session.execute(select(Account))
        accounts = result.scalars().all()

        if not accounts:
            async with session.begin():
                session.add_all([
                    Account(balance=1000),
                    Account(balance=500),
                ])

    print("Baza danych gotowa.")


async def close_db(app: web.Application):
    print("Zamykam połączenie z bazą danych...")
    engine = app["db_engine"]
    await engine.dispose()


async def get_accounts(request: web.Request):
    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        result = await session.execute(select(Account))
        accounts = result.scalars().all()

    return web.json_response([account.to_dict() for account in accounts])


async def transfer(request: web.Request):
    try:
        data = await request.json()
        from_id = int(data["from_id"])
        to_id = int(data["to_id"])
        amount = int(data["amount"])
    except Exception:
        raise web.HTTPBadRequest(
            text="Oczekiwano JSON: from_id, to_id, amount"
        )

    if amount <= 0:
        raise web.HTTPBadRequest(text="Kwota przelewu musi być większa od 0")

    if from_id == to_id:
        raise web.HTTPBadRequest(text="Nie można zrobić przelewu na to samo konto")

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            result_from = await session.execute(
                select(Account).where(Account.id == from_id)
            )
            from_account = result_from.scalar_one_or_none()

            result_to = await session.execute(
                select(Account).where(Account.id == to_id)
            )
            to_account = result_to.scalar_one_or_none()

            if from_account is None:
                raise web.HTTPNotFound(text="Konto źródłowe nie istnieje")

            if to_account is None:
                raise web.HTTPNotFound(text="Konto docelowe nie istnieje")

            if from_account.balance < amount:
                raise web.HTTPBadRequest(text="Brak wystarczających środków")

            from_account.balance -= amount
            to_account.balance += amount

            await session.flush()

            response_data = {
                "message": "Przelew wykonany",
                "from_account": from_account.to_dict(),
                "to_account": to_account.to_dict(),
            }

    return web.json_response(response_data)


def create_app():
    app = web.Application()

    app.router.add_get("/accounts", get_accounts)
    app.router.add_post("/transfer", transfer)

    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host="127.0.0.1", port=8080)