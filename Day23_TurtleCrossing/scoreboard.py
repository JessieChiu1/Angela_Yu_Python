from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}", font=('Arial', 12, 'bold'))
        self.speed = 0.1

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=('Arial', 12, 'bold'))
        self.speed_up()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=('Arial', 12, 'bold'))

    def speed_up(self):
        self.speed *= 0.95
