from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="User API",
    description="API do zarządzania użytkownikami i walidacji emaili",
    version="1.0.0"
)


class User(BaseModel):
    email: EmailStr


@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    tags=["Users"]
)
async def create_user(user: User):
   
    return {
        "message": "User created",
        "email": user.email
    }


@app.get(
    "/",
    tags=["Root"]
)
async def root():
 

    return {"message": "Hello"}