from flask import Flask

app = Flask(__name__)


@app.get("/me")
def me():
    return "Jan Kowalski"


if __name__ == "__main__":
    app.run(debug=True)
