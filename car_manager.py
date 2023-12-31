from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.move = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.forward(self.move)

    def new_level(self):
        self.move += MOVE_INCREMENT

