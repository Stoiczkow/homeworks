"""
Walidacja Email
Utwórz model User z polem email (EmailStr).
Endpoint POST /users waliduje poprawność emaila.
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    email: EmailStr

@app.post("/users")
def create_user(user: User):
    return user
