from flask import Flask, render_template

app = Flask(__name__)

#task1
@app.get('/me/<name>/<surname>')
def me(name:str, surname:str):
    return f'name: {name} surname: {surname}'

#task2
@app.get('/add/<int:num1>/<int:num2>')
def add(num1:int, num2:int):
    result = num1 + num2
    return f'wynik to: {str(result)}'


#task3 i task 4
 

@app.get('/movies')
def movies():

    movie_list = ["Harry Potter",
                "Diuna",
                "Hrabia Monte Christo",
                "Piraci z Karaibow",
                "Ojciec Chrzestny"
                ]
    
    return render_template('movies.html',page_title="Moje ulubione filmy", movies=movie_list)



if __name__ == '__main__':
    app.run(debug=True)