# 8. ✏ Zadanie 8 – Dokumentacja
# Dla dowolnego API dodaj:
# - Tytuł i opis aplikacji
# - Tagi do endpoints
# - Docstringi z przykładami
# Sprawdź /docs.
# (proste)

from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Users API",
    description="Proste API do zarządzania użytkownikami"
)


class User(BaseModel):
    name: str
    email: EmailStr


@app.get("/", tags=["Home"])
async def home():
    """
    Endpoint główny.

    Zwraca wiadomość powitalną.

    Example:
    {
        "message": "Welcome to Users API"
    }
    """

    return {"message": "Welcome to Users API"}


@app.post(
    "/users",
    tags=["Users"],
    response_model=User,
    status_code=status.HTTP_201_CREATED
)
async def create_user(user: User):
    """
    Tworzy nowego użytkownika.

    Waliduje:
    - name jako string
    - email jako poprawny adres email

    Example request:
    {
        "name": "Marek",
        "email": "marek@gmail.com"
    }
    """

    return user