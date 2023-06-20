from turtle import Turtle, Screen




# TO DRAW A PAINTING
# screen = Screen()
# timmy = Turtle()
# def move_forward():
#     timmy.forward(10)
# def move_backward():
#     timmy.backward(10)
# def turn_counterclock():
#     timmy.setheading(timmy.heading() + 10)
# def turn_clock():
#     timmy.setheading(timmy.heading() - 10)
# def clearscreen():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
# def make_circle():
#     timmy.circle(100, 10)
# screen.listen()
# # we don't use move_forward() because that would call the function right there and then instead of waiting for the key
# screen.onkey(key="w", fun=move_forward) 
# screen.onkey(key="s", fun=move_backward) 
# screen.onkey(key="a", fun=turn_counterclock) 
# screen.onkey(key="d", fun=turn_clock) 
# screen.onkey(key="c", fun=clearscreen) 
# screen.onkey(key="q", fun=make_circle) 

import random
screen = Screen()
screen.bgcolor("lightgreen")

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# create a line
line = Turtle()
line.hideturtle()
line.penup()
line.goto(x=230, y=150)
line.right(90)
line.pendown()
line.forward(300)

# create the turtles and send them to start
turtles = [None] * 6
for i in range(6):
    turtles[i] = Turtle("turtle")
    turtles[i].hideturtle()
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x = -230, y = 125 - i*50)
    turtles[i].showturtle()

def check_bet(pos):
    """checks and prints if the winner is the one user bet on or not"""
    timmy = Turtle()
    timmy.penup()
    timmy.goto(x=-75, y=0)
    timmy.hideturtle()
    if colors[pos] == user_bet:
        print(f"Correct bet, {user_bet} is the winner.")
        timmy.write(f"Correct bet, {user_bet} is the winner.")
    else:
        print(f"Incorrect bet, {colors[pos]} is the winner.")
        timmy.write(f"Incorrect bet, {colors[pos]} is the winner.")

def start_race():
    """makes the race happen"""
    race_over = False
    while race_over == False:
        for i in range(6):
            turtles[i].forward(random.randint(1, 10))
            if turtles[i].position()[0] >= 210:
                race_over = True
                check_bet(i)

start_race()

screen.exitonclick()