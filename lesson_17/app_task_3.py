from flask import Flask, render_template

app = Flask(__name__)

favorite_movies = [
    "Interstellar",
    "Inception",
    "The Matrix",
    "Dune",
]


@app.get("/movies")
def movies():
    return render_template("movies.html", movies=favorite_movies)


if __name__ == "__main__":
    app.run(debug=True)
