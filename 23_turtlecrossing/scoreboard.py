FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard():
    def __init__(self) -> None:
        self.level = 1
        self.scorer = Turtle()
        self.score()

    def score(self):
        self.scorer.clear()
        self.scorer.penup()
        self.scorer.hideturtle()
        self.scorer.goto(-280, 250)
        self.scorer.write(f"Level {self.level}", False, "Left", FONT)

    def update(self):
        self.level += 1
        self.score()

    def gameover(self):
        self.over = Turtle()
        self.over.penup()
        self.over.hideturtle()
        self.over.goto(0, 0)
        self.over.write("GAME OVER", False, "Center", FONT)