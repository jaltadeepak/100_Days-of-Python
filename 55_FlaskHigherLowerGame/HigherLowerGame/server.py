from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1> <img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp" width=200>'

random_num = random.randint(0, 9)

@app.route('/<int:number>')
def check_guess(number):
    if number == random_num:
        return '<h1 style="color: green">ABSOLUTELY CORRECT!</h1>'
    elif number > random_num:
        return '<h2 style="color: red">Too High...</h2>'
    elif number < random_num:
        return '<h2 style="color: red">Too Low...</h2>'

if __name__ == "__main__":
    app.run(debug=True)