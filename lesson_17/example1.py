from flask import Flask, render_template

#obiekt naszej aplikacji
# parametr name - nazwa pliku - tutaj jest miejsce gdzie uruchamiamy aplikacje webową
app = Flask(__name__)

# co ma sie stac jak wejdziemy pod konkrety nadress
@app.route("/") # sciezka zasobu # routing do danej strony 
### route mówimy że wchodzimy tylko metodą GET / zmiast route moze być GET
def hellow_world(): # nazwa funkcji zwaraca tylko hello world
    return "Hello world"
@app.get("/about")            # mozemy uzyc get, post , path,delete
def about():
    return "To jest strona o nas"

@app.get("/user/<username>") # tenparametr username musi byc w strzlakowych nawsiasach - przekzywanie rzeczy do funkcji
def show_profile(username):  # to co tu wposzemy user bedzie musial wpsiac
    return f"witaj {username}"
@app.get("/post/<int:post_id>")
def show_post(post_id):
    return f"Wyświetlasz post ID {post_id}"

@app.get("/index")
def index():
    users_form_db = ["Pawel", "Roza", "Pola"]
    return render_template("index.html", 
                           title="Index", 
                           author = "paweł",
                           users=users_form_db) 
#podajemy jako plik ma szukac index.html , zworc mi mindex html

@app.get("/profile/<username>")
def show_my_profile(username):
    return render_template("user.html",
                           title ="Profil",
                           my_user_name=username)
#po lewej podajemy nazwy dostepne whtml

if __name__ == "__main__": # jeśli uruchamiamy ten plik to oboekt aplikacji run
    app.run(debug=True) # będzie pokazywać dodatkowe informacje w trakcie działania apki

    # zmienną w html wstrzykujemy przez nawiasy 2 kalmrowe {{}}