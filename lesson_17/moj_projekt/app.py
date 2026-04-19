from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = ['Adam', 'Ewa', 'Karol']
    return render_template('index.html', title='Strona Główna', users=users)

@app.route('/user/<name>')
def user_page(name):
    return render_template('user.html', username=name)

# Zadanie 1 – Strona "O mnie"
# Stwórz nową ścieżkę /me w swojej aplikacji. Kiedy użytkownik wejdzie na ten adres, funkcja powinna zwrócić Twoje imię i nazwisko.

@app.route('/me')
def about_me():
    return "Daniel Chomiak"

# Zadanie 2 – Prosty kalkulator
# Utwórz ścieżkę /add/<int:num1>/<int:num2>. Funkcja przypisana do tej ścieżki powinna nprzyjąć dwie liczby jako argumenty, zsumować je i zwrócić wynik w formacie "Wynik to: [suma]".

@app.route('/add/<int:num1>/<int:num2>')
def suma(num1, num2):
    result = num1 + num2
    return f"Wynik to: {result}"

# Zadanie 3 – Przekaż listę do szablonu
# W pliku app.py stwórz listę swoich ulubionych filmów. Następnie stwórz nową ścieżkę /movies i szablon movies.html. Przekaż listę filmów do szablonu i wyświetl ją jako listę nieuporządkowaną (
# ) w HTML.
# Zadanie 4 – Dynamiczny tytuł strony
# Zmodyfikuj zadanie 3. Oprócz listy filmów, przekaż do szablonu movies.html również zmienną page_title z wartością "Moje ulubione filmy". Użyj tej zmiennej w znaczniku
@app.route('/movies')
def fav_movie():
    movies = ["Akira", "Paprika", "Spider-man: Poprzez Uniwersum"]
    page_title = "Moje ulubione filmy"
    return render_template('movies.html', page_title=page_title, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
