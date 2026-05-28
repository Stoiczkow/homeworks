import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status, BackgroundTasks

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import BookCreate, BookResponse, BookUpdate, BooksResponse, PaginationParams, BookFilter
from app.models import BookORM, AuthorORM
from app.background_tasks import write_to_log_file, log_book_deleted

router = APIRouter(
    prefix="/books-db",
    tags=["BooksDB"],
)

# Zadanie 18 – Paginacja i Filtrowanie
# Dla GET /books dodaj:
# (challenge)
# Paginację (skip, limit)
# Filtrowanie (category, min_price, max_price)
# Sortowanie (sort_by: "price" lub "title")

# READ - pobierz wszystkie książki
@router.get("/", response_model=BooksResponse)
async def get_books(
    pagination: PaginationParams = Depends(),
    filters: BookFilter = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """
    Pobiera listę książek.
    
    Args:
        db: sesja bazy danych
        pagination: parametry do paginacji
        filters: parametry do filtrowania

    """
    query = select(BookORM).options(joinedload(BookORM.author))
    
    if filters.category:
        query = query.where(BookORM.category == filters.category)
    if filters.min_price is not None:
        query = query.where(BookORM.price >= filters.min_price)
    if filters.max_price is not None:
        query = query.where(BookORM.price <= filters.max_price)
    
    if filters.sort_by == "price":
        query = query.order_by(BookORM.price)
    elif filters.sort_by == "title":
        query = query.order_by(BookORM.title)
    
    result = await db.execute(query.offset(pagination.skip).limit(pagination.limit))
    
    books = result.scalars().unique().all()
    
    return BooksResponse(pagination=pagination, books=books)

@router.post("/", response_model=BookResponse, status_code=201)
async def add_book(
    book: BookCreate,    
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    ):
    background_tasks.add_task(
        write_to_log_file,
        book_title=book.title
    )
    """
    Tworzy nową książkę w bazie danych.
            
    Args:
        book: dane książki w JSON
        background_tasks: zadania działające w tle
        db: sesja bazy danych

    """

    result = await db.execute(
        select(BookORM).where(BookORM.title == book.title)
    )

    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=400,
            detail="Book already exists"
        )
        
    author_result = await db.execute(
        select(AuthorORM).where(AuthorORM.id == book.author_id)
    )
    
    author = author_result.scalar_one_or_none()
    
    if not author:
        raise HTTPException(
            status_code=400,
            detail="Author doesn't exist"
        )
        
    db_book = BookORM(**book.model_dump())
    
    db_book.author = author 
    
    db.add(db_book)
    await db.commit()

    result = await db.execute(
        select(BookORM)
        .options(selectinload(BookORM.author))
        .where(BookORM.id == db_book.id)
    )

    created_book = result.scalar_one_or_none()

    return created_book

# READ - pobierz książkę po ID
@router.get("/{id}", response_model=BookResponse)
async def get_book(
    id: int,
    db:  AsyncSession = Depends(get_db)
    ):
    """
    Pobiera książkę po ID.
        
    Args:
        id: ID książki
        db: sesja bazy danych

    """
    result = await db.execute(
        select(BookORM)
        .options(selectinload(BookORM.author))
        .where(BookORM.id == id)
        )   
    
    db_book = result.scalar_one_or_none()
    
    if not db_book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return db_book


# READ - usun książkę po ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    id: int,    
    background_tasks: BackgroundTasks,
    db:  AsyncSession = Depends(get_db),
    ):
    """
    Usuwa książkę po ID.

    Args:
        id: ID książki
        background_tasks: zadania działające w tle
        db: sesja bazy danych
    """    
    result = await db.execute(
        select(BookORM)
        .where(BookORM.id == id)
        )
    
    db_book = result.scalar_one_or_none()
    
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not Found")
    
    background_tasks.add_task(
        log_book_deleted,
        db_book.title
    )
    await db.delete(db_book)
    await db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# UPDATE - aktualizacja ksiazki
@router.patch("/{id}", response_model=BookResponse)
async def update_book(
    id: int,
    book_update: BookUpdate,
    db: AsyncSession = Depends(get_db)
):
    """
    Częściowa aktualizacja książki
    
    Args:
        id: ID książki
        book_update: słownik z polami do aktualizacji
        db: sesja bazy danych
    """
    
    result = await db.execute(
        select(BookORM)
        .where(BookORM.id == id)
    )
    
    db_book = result.scalar_one_or_none()
    
    if not db_book:
        raise HTTPException(
            status_code=404, detail="Book not Found"
        )
    
    update_data = book_update.model_dump(exclude_unset=True)
    
    if update_data.get("author_id"):
        author_result = await db.execute(
            select(AuthorORM).where(AuthorORM.id == update_data["author_id"])
        )
        
        author = author_result.scalar_one_or_none()
        
        if not author:
            raise HTTPException(
                status_code=400,
                detail="Author doesn't exist"
            )
        
        
    for field, value in update_data.items():
        setattr(db_book, field, value)
    
    await db.commit()
    await db.refresh(db_book)
    
    return db_book
    
    