#SIMPLIFY paddle.py to not have different functions for left and right paddles
#SIMPLIFY ball.py by putting code in different new functions

from turtle import Turtle, Screen
import time
from partition import Partition
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 400)
screen.bgcolor("black")
screen.tracer(0)

screen.textinput(title="First to 5 point wins", prompt="Press enter to start")

divide = Partition()
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(lambda: paddle.movelefpad("W"), "w")
screen.onkeypress(lambda: paddle.movelefpad("S"), "s")
screen.onkeypress(lambda: paddle.moverigpad("Up"), "Up")
screen.onkeypress(lambda: paddle.moverigpad("Down"), "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball(paddle.lefpad.position(), paddle.rigpad.position())
    checkreset = ball.outofbounds() 
    if checkreset != None:
        scoreboard.update(checkreset)
    if scoreboard.lefscore == 5 or scoreboard.rigscore == 5:
        game_is_on = False

screen.exitonclick()

