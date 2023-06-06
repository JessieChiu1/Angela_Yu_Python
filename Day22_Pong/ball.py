from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_right = True
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_wall(self):
        self.move_y = self.move_y * -1

    def bounce_paddle(self):
        self.move_x = self.move_x * -1
        self.move_speed *= 0.95

    # Added some randomness to the movement of the ball on reset
    def reset_ball(self):
        self.move_right = not self.move_right
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move_y = random.randint(5, 20)
        if self.move_right:
            self.move_x = random.randint(10, 20)
        else:
            self.move_x = random.randint(-20, -10)

