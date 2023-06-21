from turtle import Turtle

class Paddle:
    def __init__(self):
        self.left_paddle()
        self.right_paddle()
        
    def left_paddle(self):
        self.lefpad = Turtle("square")
        
        self.lefpad.hideturtle()
        self.lefpad.color("white")
        self.lefpad.penup()
        self.lefpad.shapesize(5, 0.5)
        self.lefpad.speed("fastest")

        self.lefpad.goto(-380, 0)
        self.lefpad.showturtle()
    
    def right_paddle(self):
        self.rigpad = Turtle("square")
        
        self.rigpad.hideturtle()
        self.rigpad.color("white")
        self.rigpad.penup()
        self.rigpad.shapesize(5, 0.5)
        self.rigpad.speed("fastest")

        self.rigpad.goto(380, 0)
        self.rigpad.showturtle()

    def movelefpad(self, dir):
        if dir == "W" and self.lefpad.ycor() <= 140:
            self.lefpad.goto(self.lefpad.xcor(), self.lefpad.ycor() + 20)
                
        if dir == "S" and self.lefpad.ycor() >= -130:
            self.lefpad.goto(self.lefpad.xcor(), self.lefpad.ycor() - 20)
    
    def moverigpad(self, dir):
        if dir == "Up" and self.rigpad.ycor() <= 140:
            self.rigpad.goto(self.rigpad.xcor(), self.rigpad.ycor() + 20)
                
        if dir == "Down" and self.rigpad.ycor() >= -130:
            self.rigpad.goto(self.rigpad.xcor(), self.rigpad.ycor() - 20)

                