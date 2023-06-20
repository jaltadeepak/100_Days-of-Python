# import colorgram

# colors = colorgram.extract("img.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

import turtle as t
import random

t.colormode(255)


timmy = t.Turtle()
timmy.hideturtle()           #make the turtle invisible
timmy.penup()                #don't draw when turtle moves
timmy.goto(-200, -200)       #move the turtle to a location
timmy.showturtle()           #make the turtle visible
timmy.pendown()

timmy.speed("fast")
timmy.hideturtle()

for _ in range(10):
    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)

screen = t.Screen()
screen.exitonclick()