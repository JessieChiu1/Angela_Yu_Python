from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.left(90)

    def move(self):
        self.forward(20)

    def detect_finish(self):
        if self.ycor() >= 280:
            return True
        return False

    def reset(self):
        self.goto(0, -280)