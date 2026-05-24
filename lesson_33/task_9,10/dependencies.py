from fastapi import Header, HTTPException, status


async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "secret-key-123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    return x_api_key