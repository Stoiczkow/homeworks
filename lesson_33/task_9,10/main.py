from fastapi import FastAPI
from routers import books, authors


app = FastAPI(
    title="Books API",
    description="API książek i autorów"
)

app.include_router(books.router)
app.include_router(authors.router)


@app.get("/")
async def root():
    return {"message": "Books API"}