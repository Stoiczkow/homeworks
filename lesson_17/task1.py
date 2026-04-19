from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile/<name>')
def profile_name(name):
    return render_template('profile.html', username=name)

if __name__ == "__main__":
    app.run(debug=True)

