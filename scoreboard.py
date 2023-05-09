from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __int__(self):
        super().__int__()
        self.current_level = 1
        self.color("white")
        self.penup()
        self.goto(x=-250, y=250)
        self.write(f"Level: {self.current_level}", move=False, align="center", font=FONT)
