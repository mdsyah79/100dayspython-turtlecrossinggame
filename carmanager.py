import random
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Carmanager:
    def __init__(self):
        self.cars = []

    def generate_cars(self):
        chance_number = randint(1, 6)
        if chance_number == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(270, randint(-250, 250))
            new_car.seth(180)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
