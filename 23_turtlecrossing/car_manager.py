COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 1
CAR_HEIGHT = 2

from turtle import Turtle
import random

class CarManager:
    def __init__(self) -> None:
        self.level = 1
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (self.level-1)

    def generate_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            self.cars.append(Turtle())
            car = self.cars[-1]
            car.shape("square")
            car.hideturtle()
            car.penup()
            car.shapesize(CAR_WIDTH, CAR_HEIGHT)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-24, 24) * 10)
            car.showturtle()

    def keep_moving(self):
        for car in self.cars:
            car.backward(self.carspeed)
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)
        
    def update(self):
        self.level += 1

    def check_gameover(self, pos):
        for car in self.cars:
             if car.distance(pos) < 20:
                return True
        return False    
        



