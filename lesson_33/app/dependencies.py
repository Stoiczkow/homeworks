from fastapi import Header, HTTPException, status

API_KEY = "key123"


async def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
        
async def pagination_params(
    skip: int = 0,
    limit: int = 2
):
    if limit > 100:
        limit = 100
    return {"skip": skip, "limit": limit}