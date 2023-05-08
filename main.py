from turtle import Screen
from player import Player
from car_manager import Car_manager
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = Car_manager()
car_manager.generate_cars()

screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
gen_count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.move_cars()
    gen_count += 1
    if gen_count == 6:
        car_manager.generate_cars()
        gen_count = 0



screen.exitonclick()
