import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkeypress(lambda: player.move("up"), "Up")
screen.onkeypress(lambda: player.move("down"), "Down")

player = Player()
cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if cars.check_gameover(player.position()) == False:
        cars.generate_car()
        cars.keep_moving()
        if player.finishline() == True:
            score.update()
            cars.update()
    else:
        game_is_on = False
        score.gameover()

screen.exitonclick()
