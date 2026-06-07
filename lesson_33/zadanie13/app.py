from fastapi import FastAPI, HTTPException, status, Depends, BackgroundTasks, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from database import get_db, init_db, AsyncSessionLocal, engine
from models import BookORM, AuthorORM, StatsORM

from datetime import datetime
import uuid
import os
import json
from faker import Faker

from typing import List

from schemas import (
    Book, BookResponse, BookUpdate, BookCreate, BookNoAuthorResponse,
    AuthorCreate, AuthorResponse
    )

app_cache = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Database initialized!")

    global app_cache
    if os.path.exists("cache.json"):
        with open("cache.json", "r", encoding="UTF-8") as file:
            app_cache = json.load(file)
            print("Cache loaded")
    else:
        app_cache = {}
        print("No cache found")

    yield

    # Dodawania czegoś do cache przed zamknięciem
    fake = Faker()
    key = fake.name()
    value = fake.year()
    app_cache.update({key: value})

    with open("cache.json", "w", encoding="UTF-8") as file:
        json.dump(app_cache, file, ensure_ascii=False, indent=4)
        print("Cache saved")

    print("Application is shutting down...")

    await engine.dispose()
    print("Database connections closed!")

app = FastAPI(lifespan=lifespan)

### BACKGROUND TASKS ###

async def write_to_log_file(message: str):
    with open("email.log", "a", encoding="UTF-8") as f:
        timestamp = datetime.now().isoformat()
        f.write(f"{timestamp} - {message}\n")

async def write_to_all_log_file(message: str):
    with open("all-logs.log", "a", encoding="UTF-8") as f:
        f.write(message)

async def update_stats(action_type: str):
    async with AsyncSessionLocal() as db:
        if action_type == "book_delete":
            result = await db.execute(select(StatsORM).where(StatsORM.id == 1))
            stats = result.scalar_one_or_none()

            if stats is None:
                stats = StatsORM(deleted_books_count=1)
                db.add(stats)
            else:
                stats.deleted_books_count += 1
            await db.commit()

### MIDDLEWEAR ###

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    log = f"{datetime.now().isoformat()} - {request.method} - {request.url.path}\n"

    response = await call_next(request)

    response.headers["X-Request-ID"] = str(uuid.uuid4())

    if response.background is None:
        response.background = BackgroundTasks()
    response.background.add_task(write_to_all_log_file, log)
        
    return response

### BOOKS ENDPOINT ###

@app.get("/books", status_code=200)
async def get_books(skip: int = 0,
                    limit: int = Query(default=10, ge=1, le=100),
                    category: str = None,
                    min_price: float = None,
                    max_price: float = None,
                    sort_by: str = None,
                    db: AsyncSession = Depends(get_db)):
    
    query = select(BookORM)

    if category:
        query = query.where(BookORM.category == category)
    if min_price is not None:
        query = query.where(BookORM.price >= min_price)
    if max_price is not None:
        query = query.where(BookORM.price <= max_price)
    if sort_by == "price":
        query = query.order_by(BookORM.price)
    elif sort_by == "title":
        query = query.order_by(BookORM.name)

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)
    books = result.scalars().all()
    
    if not books:
        raise HTTPException(status_code=404,
                            detail="Empty response")

    return books

@app.get("/books/{id}", status_code=200, response_model=Book)
async def get_books(id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(BookORM).where(BookORM.id == id))
    book = result.scalar_one_or_none()
    
    if not book:
        raise HTTPException(status_code=404,
                            detail="Book doesn't exist")

    return book

@app.post("/books", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate,
                        background_tasks: BackgroundTasks,
                        db: AsyncSession = Depends(get_db)
                        ):
    
    try:
        db_book = BookORM(**book.model_dump())
        db.add(db_book)
        await db.commit()
    except IntegrityError:
        raise HTTPException(status_code=400,
                            detail="Couldn't save book in the database")
    
    result = await db.execute(select(BookORM).where(BookORM.id == db_book.id).options(selectinload(BookORM.author)))

    created_book = result.scalar_one()

    background_tasks.add_task(
        write_to_log_file,
        f"Zapisano książkę {created_book.name}!"
        )

    return created_book

@app.delete("/books/{id}", status_code=200)
async def delete_book(id: int, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(BookORM).where(BookORM.id == id))

    book = result.scalar_one_or_none()
    
    if not book:
        raise HTTPException(status_code=404,
                            detail="Book with that ID does not exist")

    await db.delete(book)
    await db.commit()

    background_tasks.add_task(
    update_stats,
    action_type="book_delete"
    )

    return {"info": f"book {id} deleted"}

@app.patch("/books/{id}", status_code=200, response_model=BookUpdate)
async def update_book(id: int, book_update: BookUpdate, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(BookORM).where(BookORM.id == id))
    book = result.scalar_one_or_none()
    
    if not book:
        raise HTTPException(status_code=404,
                            detail="Book with that ID does not exist")
    
    update_data = book_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(book, field, value)

    await db.commit()
    await db.refresh(book)

    return book

### AUTHOR ENDPOINTS ###

@app.get("/authors/{id}/books", status_code=200, response_model=List[BookNoAuthorResponse])
async def get_author_book(id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(BookORM).where(BookORM.author_id == id))
    books = result.scalars().all()
    
    if not books:
        raise HTTPException(status_code=404,
                            detail="No books found")
    return books

@app.post("/authors", response_model=AuthorResponse, status_code=201)
async def create_author(author: AuthorCreate,
                        db: AsyncSession = Depends(get_db)
                        ):
    try:
        db_author = AuthorORM(**author.model_dump())
        db.add(db_author)
        await db.commit()
    except IntegrityError:
        raise HTTPException(status_code=400,
                            detail="Couldn't save author in the database")
    await db.refresh(db_author)
    return db_author