import time
from turtle import Turtle
from random import randint, uniform

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car_manager():
    def __init__(self):
        self.cars = []
        # for color in COLORS:
        #    self.generate_cars(color)

    def generate_cars(self):
        num_of_cars = randint(1, 3)
        for x in range(1, num_of_cars):
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(COLORS[randint(0, len(COLORS)-1)])
            new_car.goto(260, randint(-250, 250))
            new_car.seth(180)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)


