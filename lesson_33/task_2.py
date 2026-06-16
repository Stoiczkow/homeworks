"""
Utwórz endpoint GET /greet/{name} który zwraca powitanie dla danej osoby.
Dodaj walidację: imię musi mieć min 2 znaki.
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/greet/{name}")
def greet(name: str):
    if len(name) < 2:
        raise HTTPException(status_code=400, detail="Imię musi mieć co najmniej 2 znaki")
    return {"message": f"Witaj, {name}!"}
