"""
Stwórz endpoint GET /calculate który przyjmuje:
- a: int (wymagany)
- b: int (wymagany)
- operation: str (domyślnie "add")
Zwraca wynik operacji: add, subtract, multiply, divide.
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/calculate")
def calculate(a: int, b: int, operation: str = "add"):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Nie można dzielić przez zero")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Nieznana operacja")

    return {"a": a, "b": b, "operation": operation, "result": result}
