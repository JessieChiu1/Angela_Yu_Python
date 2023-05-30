from turtle import Turtle, Screen
import random

game_on = True
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for x in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[x])
    turtle.goto(x=-230, y=y[x])
    all_turtles.append(turtle)

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
                game_on = False
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")
                game_on = False
        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()
