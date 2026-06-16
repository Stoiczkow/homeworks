'''
Stwórz aplikację FastAPI z trzema endpoints:
(proste)
GET / - zwraca {"message": "Hello"}
GET /time - zwraca aktualny czas
GET /random - zwraca losową liczbę 1-100
'''

from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

@app.get("/time")
def get_time():
    return {"time": datetime.now().isoformat()}

@app.get("/random")
def get_random():
    return {"number": random.randint(1, 100)}
