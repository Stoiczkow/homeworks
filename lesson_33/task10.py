from fastapi import FastAPI, Header, HTTPException, Depends, status

app = FastAPI(
    title="API Key Example",
    description="Przykład użycia ",
    version="1.0.0"
)

API_KEY = "secret123"


async def verify_api_key(x_api_key: str = Header(...)):
  

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )


@app.get(
    "/public",
    tags=["Public"]
)
async def public_endpoint():


    return {"message": "Public endpoint"}


@app.get(
    "/books",
    dependencies=[Depends(verify_api_key)],
    tags=["Protected"]
)
async def get_books():


    return {"books": ["Wiedźmin", "Harry Potter"]}


@app.post(
    "/books",
    dependencies=[Depends(verify_api_key)],
    tags=["Protected"]
)
async def add_book():


    return {"message": "Book added"}


@app.delete(
    "/books/{id}",
    dependencies=[Depends(verify_api_key)],
    tags=["Protected"]
)
async def delete_book(id: int):


    return {"message": f"Book {id} deleted"}