from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-250, 220)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def level_increased(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 50)
        self.write(f"Level : {self.level}", align="center", font=("Courier", 10, "normal"))
        self.goto(0, 0)
        self.write("GAME_OVER", align="center", font=FONT)

