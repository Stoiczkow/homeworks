from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL,
    echo=True, # True tylko dla local
    future=True
)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False, # Obiekty działają po commit
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

async def get_db():
    """
    Dependency injection dla sesji bazy danych.
    Automatycznie zamyka sesję po zakończeniu requestu.
    """
    async with AsyncSessionLocal() as session:

        try:
            yield session
        finally:
            await session.close()
            
# Funkcja do utworzenia tabel (wywoływana przy starcie)
async def init_db():
    """Tworzy wszystkie tabele zdefiniowane w Base.metadata."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)