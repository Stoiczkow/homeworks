from flask import Flask

app = Flask(__name__)


@app.get("/add/<int:num1>/<int:num2>")
def add(num1: int, num2: int):
    suma = num1 + num2
    return f"Wynik to: {suma}"


if __name__ == "__main__":
    app.run(debug=True)
