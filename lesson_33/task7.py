from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr

app = FastAPI()


class User(BaseModel):
    email: EmailStr


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    return {
        "message": "User created",
        "email": user.email
    }