from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()





game_is_on = True




while game_is_on:
    screen.update()







screen.exitonclick()