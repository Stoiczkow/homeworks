from fastapi import FastAPI
from routers.books import router as books_router
from routers.authors import router as authors_router

app = FastAPI(
    title="Library API",
    description="API książek i autorów",
    version="1.0.0"
)

app.include_router(books_router)
app.include_router(authors_router)