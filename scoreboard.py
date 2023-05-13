from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.update_scoreboard()

    def level_up(self):
        self.current_level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-200, y=250)
        self.clear()
        self.write(f"Level: {self.current_level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

