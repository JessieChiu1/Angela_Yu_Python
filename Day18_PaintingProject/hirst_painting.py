import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("image.jpg", 10)

dot = Turtle()
screen = Screen()

dot.width(5)
screen.colormode(255)
dot.speed("fastest")

start = dot.pos()

for l in range(1,10):
    for w in range(1,10):
        dot.color(random.choice(colors).rgb)
        dot.begin_fill()
        dot.circle(10)
        dot.end_fill()
        dot.penup()
        dot.forward(50)
    dot.setx(0)
    dot.sety(l * 50)
