from turtle import Turtle

class Scoreboard:
    def __init__(self) -> None:
        self.lefscore = 0
        self.rigscore = 0
        self.create_lefscore()
        self.create_rigscore()

    def create_lefscore(self):
        self.left = Turtle()
        self.left.hideturtle()
        self.left.color("white")
        self.left.penup()
        self.left.goto(-50, 130)
        self.left.write(self.lefscore, False, "center", ("Arial", 50, "normal"))
    
    def create_rigscore(self):
        self.right = Turtle()
        self.right.hideturtle()
        self.right.color("white")
        self.right.penup()
        self.right.goto(50, 130)
        self.right.write(self.rigscore, False, "center", ("Arial", 50, "normal"))

    def update(self, paddle):
        if paddle == "right":
            self.lefscore += 1
            self.left.clear()
            self.left.write(self.lefscore, False, "center", ("Arial", 50, "normal"))
        elif paddle == "left":
            self.rigscore += 1
            self.right.clear()
            self.right.write(self.rigscore, False, "center", ("Arial", 50, "normal"))
        

    