from turtle import Turtle
import random

color = ["brown", "red", "blue", "green", "black"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(color))
        self.setheading(180)
        self.goto(x=300, y=random.randint(-250, 250))

    def move(self):
        self.forward(10)


