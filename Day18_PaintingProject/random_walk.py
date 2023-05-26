from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.pendown()
timmy.width(10)
screen.colormode(255)
timmy.speed("fastest")

for x in range(200):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    timmy.pencolor(r,g,b)
    direction = random.randint(1,4)
    timmy.left(direction * 90)
    timmy.forward(25)
