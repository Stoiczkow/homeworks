from flask import Flask, render_template

app = Flask(__name__)


@app.get('/me')
def me():
    return 'Malicki Jacek'


@app.get('/add/<int:num1>/<int:num2>')
def adding(num1, num2):
    return f'Wynik to {num1 + num2}'


@app.get('/films')
def films():
    films = ["HP1", "HP2", "War2"]
    return render_template('films.html', title='moje ulubione filmy', films=films)


if __name__ == '__main__':
    app.run(debug=True)
