from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE_POS = (-280, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POS)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.current_level}", font=FONT, align="left")

    def add_score(self):
        self.current_level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)
