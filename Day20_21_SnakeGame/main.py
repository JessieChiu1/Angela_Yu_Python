from turtle import Turtle, Screen
import random

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake")

# Snake setup
ycor = [0, 0, 0]
xcor = [0, -20, -40]
snakes = []

for i in range(0, 3):
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.goto(x=xcor[i], y=ycor[i])
    snakes.append(snake)

print(snakes)
screen.exitonclick()