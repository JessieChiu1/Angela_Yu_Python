from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.pendown()
screen.colormode(255)
timmy.speed("fastest")

for x in range(60):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)
    timmy.circle(100)
    timmy.left(360/60)