from fastapi import FastAPI, HTTPException, Path
import time, random

from pydantic import BaseModel, EmailStr, computed_field

from app.database import init_db

from app import models
from app.routers.books_db import router as books_router
from app.routers.authors_db import router as authors_router

from app.middlewares import log_requests_and_add_headers
from app.event_hooks import startup_event, shutdown_event

app = FastAPI(
    title="Moja Pierwsza API",
    description="API do zarządzania książkami i produktami",
    version="1.0.0"
)
    
app.middleware("http")(log_requests_and_add_headers)

@app.on_event("startup")
async def on_startup():
    await startup_event(app)


@app.on_event("shutdown")
async def on_shutdown():
    await shutdown_event(app)
    
app.include_router(books_router)
app.include_router(authors_router)


# Zadanie 1 – Pierwsze API
# Stwórz aplikację FastAPI z trzema endpoints:
# (proste)
# GET / - zwraca {"message": "Hello"}
# GET /time - zwraca aktualny czas
# GET /random - zwraca losową liczbę 1-100

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/time")
async def root():
    return time.time()

@app.get("/random")
async def root():
    return random.randint(1,100)

# 2. ✏ Zadanie 2 – Path Parameters
# Utwórz endpoint GET /greet/{name} który zwraca powitanie dla danej osoby.
# Dodaj walidację: imię musi mieć min 2 znaki.
# (proste)

@app.get("/greet/{name}")
async def greet(
    name: str = Path(..., min_length=2)
    ):
    return {"message": f"Hello, {name}!"}

# 3. ✏ Zadanie 3 – Query Parameters
# Stwórz endpoint GET /calculate który przyjmuje query params:
# Zwraca wynik operacji: add, subtract, multiply, divide

@app.get("/calculate")
async def calculate(
    a: int,
    b: int,
    operation: str = "add"
    ):
    """
    Wykonuje podaną operacje matetematyczną, domyślnie dodawanie
    Params:
    a - pierwsza liczba
    b - druga liczba
    operation - rodzaj operacji spośród (dodawanie, odejmowanie, mnożenie, dzielenie)
    
    
    Returns:
        Wynik opracji matematycznej lub wyjątek w sytuacji dzielenia przez 0
    """
    
    result = None
    if operation == "add":
        result = a + b
    if operation == "subtract":
        result = a - b
    if operation == "multiply":
        result = a * b
    if operation == "divide":
        try:
            result = a / b
        except ZeroDivisionError:
            raise HTTPException(detail="Cannot divide by 0")
    return {operation: result}


USERS = {}

class User(BaseModel):
    email: EmailStr


@app.post("/users", response_model=User, status_code=201, tags=["users"])
async def add_user(user: User):
    """
    Dodaje nowego użytkownika z walidacją emaila.

    Request example:
    ```json
    {
        "email": "test@example.com"
    }
    ```

    Response example:
    ```json
    {
        "email": "test@example.com"
    }
    ```
    """

    user_id = max(USERS.keys(), default=0) + 1

    new_user = {
        "id": user_id,
        **user.model_dump()
    }

    USERS[user_id] = new_user
    return new_user