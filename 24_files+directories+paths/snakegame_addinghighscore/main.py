# INHERITANCE:
# class toinherit:
#     functions
# class inherits:
#     def __init__(self) -> None:
#         super().__init__()

# SLICING:
# list = [a, b, c, d, e, f]
# list[2:5:1] = [c, d, e, f]
# list[2:5:2] = [c, e]
# list[::-1] => to reverse the list

# STEPS FOR THE GAME:
# 1. Create a snake body
# 2. Move the snake
# 3. Create snake food 
# 4. Detect collision with food 
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

# Try to add a reset button so that the game continues

from turtle  import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# game_exit = False
# while game_exit == False:


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(lambda: snake.turn("Up"), "Up")
screen.onkey(lambda: snake.turn("Down"), "Down")
screen.onkey(lambda: snake.turn("Right"), "Right")
screen.onkey(lambda: snake.turn("Left"), "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update()
        snake.update()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        scoreboard.reset()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
                snake.reset()
                scoreboard.reset()
        
screen.exitonclick()
