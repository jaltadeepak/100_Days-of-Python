STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.start_pos()

    def start_pos(self):
        self.penup()
        self.hideturtle()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move(self, dir):
        if dir == "up":
            self.forward(MOVE_DISTANCE)
        elif dir == "down":
            self.backward(MOVE_DISTANCE)

    def finishline(self):
        if self.ycor() >= 270:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

    