from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1

    def write_level(self):
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write_level()

    def game_over(self):
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)

