from turtle import Turtle
from paddle import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.ballspeed = 15
        self.xincrement = self.ballspeed
        self.yincrement = self.ballspeed

    def create_ball(self):
        self.shape("circle")
        self.hideturtle()
        self.color("white")
        # self.shapesize(0.5, 0.5, 2)
        self.penup()
        self.showturtle()

    def move_ball(self, lefpos, rigpos):
        self.goto(self.xcor() + self.xincrement, self.ycor() + self.yincrement)

        if self.ycor() <= -180 or self.ycor() >= 180:
            self.yincrement *= -1

        if self.distance(lefpos) < 50 and self.xcor() < -350:
            self.xincrement *= -1
            self.ballspeed += 2

        if self.distance(rigpos) < 50 and self.xcor() > 350:
            self.xincrement *= -1
            self.ballspeed += 2

    def outofbounds(self):
        if self.xcor() > 400:
            paddle = "right"
        elif self.xcor() < -400:
            paddle = "left"
        if self.xcor() > 400 or self.xcor() < -400:
            self.hideturtle()
            self.ballspeed = 10
            self.goto(0, 0)
            self.xincrement *= -1
            self.yincrement *= -1
            self.showturtle()    
            return paddle
        return None
    

        


