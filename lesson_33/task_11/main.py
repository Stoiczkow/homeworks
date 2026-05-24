from fastapi import FastAPI
from models import Book

app = FastAPI(
    title="Books API",
)


@app.post("/books")
async def create_book(book: Book):
   
    return book