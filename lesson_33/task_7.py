# 7. ✏ Zadanie 7 – Walidacja Email
# Utwórz model User z polem email (EmailStr).
# Endpoint POST /users waliduje poprawność emaila.
# (proste)


from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr

@app.post("/users", response_model=User)
async def create_user(user: User):
    return user