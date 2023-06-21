from turtle import Turtle

RESIZE = 0.75
LINESEGMENTS = 20

class Partition(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.create_partition()

    def create_partition(self):
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.pensize(3)
        self.make_the_line()
       

    def make_the_line(self):
        self.goto(0, 200)
        self.setheading(270)
        self.pendown()
        for seg_no in range(LINESEGMENTS):
            self.forward(12.5)
            self.penup()
            self.forward(7.5)
            self.pendown()
            