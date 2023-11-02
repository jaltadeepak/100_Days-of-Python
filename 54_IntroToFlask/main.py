from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return 'Bye!'

if __name__ == "__main__":
    app.run()

# FUNCTIONS can be passed as first-class objects so they can be parameters of other functions
# FUNCTIONS can be NESTED
# FUNCTIONS can be returned as Output of a function

#PYTHON DECORATORS:
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
# @delay_decorator => DECORATOR IS APPLIED TO THE FUNCTION IN THE NEXT LINE, syntactic sugar
# def say_hello():
#     print("Hello")
    