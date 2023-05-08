from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.seth(90)
        self.color("green")
        self.penup()
        self.goto(x=0, y=-280)
