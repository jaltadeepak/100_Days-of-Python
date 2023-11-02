from flask import Flask

app = Flask(__name__)

# HTML and URL Parsing

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function
    
def make_emphasis(function):
    def wrapper_function():
        return '<em>'+function()+'</em>'
    return wrapper_function
    
def make_underlined(function):
    def wrapper_function():
        return '<u>'+function()+'</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye'

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)


#ADVANCED DECORATORS w/ ARGS and KWARGS
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated_user(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
        
# @is_authenticated_user
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post")

# new_user = User('Deepak')
# new_user.is_logged_in = True
# create_blog_post(new_user)

