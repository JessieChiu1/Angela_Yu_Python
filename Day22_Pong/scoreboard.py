from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.write_score()

    def player1_scored(self):
        self.player1_score += 1
        self.write_score()

    def player2_scored(self):
        self.player2_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.player2_score} : {self.player1_score}", align="center", font=('Arial', 20, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=('Arial', 20, 'bold'))