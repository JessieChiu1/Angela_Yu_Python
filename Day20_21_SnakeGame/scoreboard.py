from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.find_high_score()
        self.write_score()

    def scored(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 12, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.set_high_score()
        self.score = 0
        self.write_score()

    def find_high_score(self):
        with open("data.txt") as file:
            content = file.read()
            self.high_score = int(content)

    def set_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.score}")