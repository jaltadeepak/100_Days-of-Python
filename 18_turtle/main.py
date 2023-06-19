# from turtle import * => will import all classes and you can use them directly, bu this is not preferred
# import turtle as t => to shorten the name
 
# DRAW A SQUARE 
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("orangered")
# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)

# DRAW A DASHED LINE
# from turtle import Turtle, Screen
# timmy = Turtle()
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# DRAW A TRIANGLE, SQUARE, PENTAGON, ETC TILL DECAGON
# from turtle import Turtle, Screen
# timmy = Turtle()
# import random
# colours = ["pale violet red", "pink", "gold", "pale green", "deep sky blue", "slate gray", "light steel blue", "yellow", "teal"]
# for i in range(3, 11):
#     timmy.color(random.choice(colours))
#     for _ in range(0, i):
#         timmy.forward(100)
#         timmy.right(360/i)

# DRAW A RANDOM WALK
# from turtle import Turtle, Screen
# timmy = Turtle()
# .setheading() basically moves north, south, west or east according to the angles
# import random
# colours = ["pale violet red", "pink", "gold", "pale green", "deep sky blue", "slate gray", "light steel blue", "yellow", "teal"]
# angles = [0, 90, 180, 270]
# timmy.width(10)
# timmy.speed("fastest")
# for _ in range (100):
#     timmy.forward(20)
#     timmy.color(random.choice(colours))
#     timmy.setheading(random.choice(angles))

# my_tuple = (1, 3, 9)
# tuples are like lists but are immutable, can not be changed once declared, cannot edit or delete

# GENERATE RANDOM RGB COLORS
# import turtle as t
# import random
# timmy = t.Turtle()
# t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r, g, b)
# angles = [0, 90, 180, 270]
# timmy.width(10)
# timmy.speed("fastest")
# for _ in range (100):
#     timmy.forward(20)
#     timmy.color(random_color())
#     timmy.setheading((random.choice(angles)))

# DRAW A SPIROGRAPH
from turtle import Turtle, Screen
import turtle
import random
timmy = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
timmy.speed("fastest")
def draw_spirograph(size_of_graph):
    for i in range(int(360/size_of_graph)):
        timmy.color(random_color())
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size_of_graph)
draw_spirograph(10)

screen = Screen()
screen.exitonclick()