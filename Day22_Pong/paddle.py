from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, keyup, keydown):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=xcor, y=0)
        self.keyup = keyup
        self.keydown = keydown
        self.speed_multiplier = 1.1

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

