from turtle import Turtle
from paddle import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.xincrement = 15
        self.yincrement = 15
        self.ballspeed = 0.1
        self.incflag = -1

    def create_ball(self):
        self.shape("circle")
        self.hideturtle()
        self.color("white")
        # self.shapesize(0.5, 0.5, 2)
        self.penup()
        self.showturtle()

    def move_ball(self, lefpos, rigpos):
        self.goto(self.xcor() + self.xincrement, self.ycor() + self.yincrement)

        self.wallstrike()

        self.paddlestrike(lefpos, rigpos)

    def wallstrike(self):
        if self.ycor() <= -160 or self.ycor() >= 160:
            self.yincrement *= -1

    def paddlestrike(self, lefpos, rigpos):
        if self.distance(lefpos) < 50 and self.xcor() < -350:
            self.increment(lefpos)
            self.xincrement *= -1
            self.ballspeed *= 0.9

        if self.distance(rigpos) < 50 and self.xcor() > 350:
            self.increment(rigpos)
            self.xincrement *= -1
            self.ballspeed *= 0.9

    def increment(self, pos):
        if self.yincrement < 0:
            self.incflag = -1
        else:
            self.incflag = 1

        if self.distance(pos) < 10:
            self.yincrement = 15 * self.incflag
        elif self.distance(pos) < 30:
            self.yincrement = 17.5 * self.incflag
        else:
            self.yincrement = 20 * self.incflag

        
    def outofbounds(self):

        if self.xcor() > 400:
            paddle = "right"
        elif self.xcor() < -400:
            paddle = "left"

        if self.xcor() > 400 or self.xcor() < -400:
            self.hideturtle()
            self.goto(0, 0)
            self.ballspeed = 0.1
            self.xincrement *= -1
            self.yincrement *= -1
            self.showturtle()    
            return paddle
        return None
    

        


