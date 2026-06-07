# === file: main.py ===
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List

from database import get_db, init_db
from models import UserORM, OrderORM
from schemas import UserCreate, UserUpdate, UserResponse, UserWithOrders
from schemas import OrderCreate, OrderResponse

app = FastAPI(title="FastAPI with Database")

# Inicjalizacja bazy danych przy starcie aplikacji
@app.on_event("startup")
async def startup_event():
    print("zaczynam")
    """Tworzy tabele przy starcie aplikacji."""
    await init_db()
    print("Database initialized!")

# CREATE - tworzenie użytkownika
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Tworzy nowego użytkownika w bazie danych.

    Args:
        user: Dane użytkownika (walidowane przez Pydantic)
        db: Sesja bazy danych (wstrzykiwana przez dependency)
    """
    # Sprawdź, czy username już istnieje
    result = await db.execute(
        select(UserORM).where(UserORM.username == user.username)
    )
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Utwórz nowy obiekt ORM z danych Pydantic
    db_user = UserORM(**user.model_dump())

    # Dodaj do sesji i zapisz
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)  # Odśwież, aby pobrać ID i created_at

    return db_user

# READ - pobierz wszystkich użytkowników
@app.get("/users", response_model=List[UserResponse])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Pobiera listę użytkowników z paginacją."""
    result = await db.execute(
        select(UserORM)
        .offset(skip)
        .limit(limit)
        .order_by(UserORM.created_at.desc())
    )
    users = result.scalars().all()
    return users

# READ - pobierz użytkownika po ID
@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Pobiera użytkownika po ID."""
    result = await db.execute(
        select(UserORM).where(UserORM.id == user_id)
    )
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# READ - użytkownik z zamówieniami (eager loading)
@app.get("/users/{user_id}/with-orders", response_model=UserWithOrders)
async def get_user_with_orders(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Pobiera użytkownika z jego zamówieniami.
    selectinload - eager loading relacji (zapobiega N+1 problem).
    """
    result = await db.execute(
        select(UserORM)
        .options(selectinload(UserORM.orders))  # Załaduj też zamówienia
        .where(UserORM.id == user_id)
    )
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# UPDATE - aktualizacja użytkownika
@app.patch("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Częściowa aktualizacja użytkownika."""
    # Pobierz użytkownika
    result = await db.execute(
        select(UserORM).where(UserORM.id == user_id)
    )
    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Aktualizuj tylko podane pola
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)

    await db.commit()
    await db.refresh(db_user)

    return db_user

# DELETE - usunięcie użytkownika
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Usuwa użytkownika z bazy."""
    result = await db.execute(
        select(UserORM).where(UserORM.id == user_id)
    )
    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(db_user)
    await db.commit()

    return None

# CREATE - tworzenie zamówienia
@app.post("/orders", response_model=OrderResponse, status_code=201)
async def create_order(
    order: OrderCreate,
    db: AsyncSession = Depends(get_db)
):
    """Tworzy nowe zamówienie dla użytkownika."""
    # Sprawdź, czy użytkownik istnieje
    result = await db.execute(
        select(UserORM).where(UserORM.id == order.user_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="User not found")

    db_order = OrderORM(**order.model_dump())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)

    return db_order