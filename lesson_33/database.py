# === file: database.py ===
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do bazy danych (przykład dla PostgreSQL)
# Format: postgresql+asyncpg://user:password@host:port/database
DATABASE_URL = "postgresql+asyncpg://postgres:prorok25@localhost/fastapi_db"

# Dla SQLite (rozwój lokalny):
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Tworzenie async engine
engine = create_async_engine(
    DATABASE_URL, echo=True, future=True  # Logowanie SQL queries (wyłącz w produkcji)
)

# Session factory - tworzy nowe sesje
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Obiekty działają po commit
    autocommit=False,
    autoflush=False,
)

# Base class dla modeli ORM
Base = declarative_base()


# Dependency injection do sesji bazy danych
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