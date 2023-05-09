from turtle import Screen
from player import Player
from carmanager import Carmanager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
carmanager = Carmanager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
gen_count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    carmanager.move_cars()
    gen_count += 1
    if gen_count == 6:
        carmanager.generate_cars()
        gen_count = 0

    # when turtle hits car, end game
    for car in carmanager.cars:
        if car.distance(player) < 25:
            game_is_on = False

    # Return Player to start line once reach finish line and level up
    if player.ycor() == 280:
        player.player_restart()
        carmanager.level_up()


screen.exitonclick()
