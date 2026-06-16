"""
Stwórz dependency verify_api_key sprawdzające header X-API-Key.
Użyj go w 3 różnych endpoints.
"""

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "secret-key-123":
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return x_api_key


@app.get("/secure1")
async def secure_endpoint_1(api_key: str = Depends(verify_api_key)):
    return {"endpoint": "secure1", "api_key": api_key}


@app.get("/secure2")
async def secure_endpoint_2(api_key: str = Depends(verify_api_key)):
    return {"endpoint": "secure2", "api_key": api_key}


@app.post("/secure3")
async def secure_endpoint_3(api_key: str = Depends(verify_api_key)):
    return {"endpoint": "secure3", "api_key": api_key}
