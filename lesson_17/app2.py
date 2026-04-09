from flask import Flask, render_template

app = Flask(__name__)

# Zadanie 1 – Strona "O mnie"
# Stwórz nową ścieżkę /me w swojej aplikacji. Kiedy użytkownik wejdzie na ten adres, funkcja
# powinna zwrócić Twoje imię i nazwisko.

@app.get('/o-mnie')
def o_mnie():
    return "Piotr Walczak"

# Zadanie 2 – Prosty kalkulator
# Utwórz ścieżkę /add/<int:num1>/<int:num2>. Funkcja przypisana do tej ścieżki powinna
# przyjąć dwie liczby jako argumenty, zsumować je i zwrócić wynik w formacie "Wynik to:
# [suma]".

@app.get('/add/<int:num1>/<int:num2>')
def minicalc(num1, num2):
    return f"Wynik to: {num1 + num2}"

# Zadanie 3 – Przekaż listę do szablonu
# W pliku app.py stwórz listę swoich ulubionych filmów. Następnie stwórz nową ścieżkę
# /movies i szablon movies.html. Przekaż listę filmów do szablonu i wyświetl ją jako listę
# nieuporządkowaną (
# ) w HTML.

# Zadanie 4 – Dynamiczny tytuł strony
# Zmodyfikuj zadanie 3. Oprócz listy filmów, przekaż do szablonu movies.html również
# zmienną page_title z wartością "Moje ulubione filmy". Użyj tej zmiennej w znaczniku

my_movies = ["Kosmos", "Dziedzictwo", "Diuna"]

@app.get('/movies')
def movies():
    return render_template('movies.html',
                            my_movies = my_movies,
                            page_title = "Moje ulubione filmy")


if __name__ == '__main__':
    app.run(debug=True)