from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hw():
    return 'Hello, World!'

@app.get('/about')
def about():
    return 'Strona o nas'

@app.get('/user/<name>')
def show_profile(name):
    return f'Witaj {name}'

@app.get('/post/<int:post_id>')
def show_post(post_id):
    return f'Wyswietlasz post o id {post_id}'

@app.get('/index')
def index():
    users_from_db = ['Fil', 'Kaaan', 'Pola']
    return render_template('index.html', title="Strona głowna", users=users_from_db)

if __name__ == '__main__':
    app.run(debug=True)
