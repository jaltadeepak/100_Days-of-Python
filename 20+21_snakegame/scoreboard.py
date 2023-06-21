from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x = 0, y = 280)
        self.score = 0
        self.write("Score: 0", False, "center", ("Arial", 10, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def gameover(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER. FINAL SCORE: {self.score}", False, ALIGNMENT, FONT)

    # def create_buttons(self):
    #     self.reset = Turtle("square")
    #     self.reset.hideturtle()
    #     self.reset.penup()
    #     self.reset.color("white")
    #     self.reset.goto(-200, -200)
    #     self.reset.write("Reset", False, ALIGNMENT, FONT)
    #     self.reset.shapesize(2, 2)
    #     self.reset.onclick(self.reset_game)
    #     self.reset.showturtle()

    #     self.endgame = Turtle("square")
    #     self.endgame.hideturtle()
    #     self.endgame.penup()
    #     self.endgame.color("white")
    #     self.endgame.goto(200, -200)
    #     self.endgame.write("Close", False, ALIGNMENT, FONT)
    #     self.endgame.shapesize(2, 2)
    #     self.endgame.onclick(self.end_game)
    #     self.endgame.showturtle()

    # def reset_game(self):
    #     return False

    # def end_game(self):
    #     return True

