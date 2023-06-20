from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:    
    def __init__(self) -> None:
        self.snake = []
        self.length = 3
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        self.snake = []
        for _ in range(self.length):
            self.add_segment()

    def add_segment(self):
        self.snake.append(None)
        self.snake[-1] = Turtle("square")
        self.snake[-1].color("white")
        self.snake[-1].penup()
        if len(self.snake) > 1:
            last_segment = self.snake[-2]
            new_segment = self.snake[-1]
            
            new_segment.goto(last_segment.position())

    def update(self):
        self.length += 1
        self.add_segment()  
        
    def move(self):
        for i in range(self.length - 1, 0, -1):
            self.snake[i].goto(self.snake[i-1].position())
        self.head.forward(20)

    def turn(self, dir):
        if dir == "Up":
            angle = UP
            curr_angle = DOWN
        elif dir == "Down":
            angle = DOWN
            curr_angle = UP
        elif dir == "Left":
            angle = LEFT
            curr_angle = RIGHT
        elif dir == "Right":
            angle = RIGHT
            curr_angle = LEFT
    
        if self.head.heading() != curr_angle:
            self.head.setheading(angle)
    
