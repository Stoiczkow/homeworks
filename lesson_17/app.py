from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello World"

@app.get('/about')
def about():
    return "To jest strona o nas"

@app.get('/user/<username>')
def show_profile(username):
    return f"Witaj {username}"

@app.get('/post/<int:post_id>')
def show_post(post_id):
    return f"Wyświetlasz post o id {post_id}"

@app.get('/index')
def index():
    user_from_db = ['Paweł', 'Krzysztof', 'Anna']
    return render_template('index.html',
                            title = "Strona główna",
                            users = user_from_db,
                            author = "PiotrW")

@app.get('/profile/<username>')
def show_profile_another(username):
    return render_template('user.html',
                            title = 'Profil',
                            my_user_name = username)

if __name__ == '__main__':
    app.run(debug=True)