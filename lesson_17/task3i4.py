#Zadanie 3 – Przekaż listę do szablonu
#W pliku app.py stwórz listę swoich ulubionych filmów. Następnie stwórz nową ścieżkę /movies i szablon movies.html. Przekaż listę filmów do szablonu i wyświetl ją jako listę nieuporządkowaną ( ) w HTML

from flask import Flask, render_template


app = Flask(__name__)

#lewa strona (movies) → nazwa w HTML
#prawa strona (film_list) → dane z Pythona

@app.get("/movies")
def movies():
    film_list = ["Straszny Film", "Gladiator", "Kubuś Puchatek"]
    return render_template("movies.html", movies=film_list, page_title="Moje ulubione filmy - ZD 4") # pagi title dodane w tytule body

if __name__ == "__main__":
    app.run(debug=True)

#  Zadanie 4 – Dynamiczny tytuł strony
# Zmodyfikuj zadanie 3. Oprócz listy filmów, przekaż do szablonu movies.html również zmienną page_title z wartością "Moje ulubione filmy". Użyj tej zmiennej w znaczniku