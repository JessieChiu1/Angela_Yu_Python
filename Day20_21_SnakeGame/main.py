import time
from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake")
# Disable animation initially
screen.tracer(0)

# Snake setup
pos = [(-40, 0), (-20, 0), (0, 0)]
snakes = []

for i in range(0, 3):
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.goto(pos[i])
    snakes.append(snake)

# Snake movement
direction = "right"
game_on = True

# Logic is that technically at each tick, the only changes are the tails disappear a new head appear
while game_on:

    # pop the position and snake of the tail in lists
    snake = snakes.pop(0)
    pos.pop(0)
    if direction == "right":
        snake.setx(snakes[-1].xcor() + 20)
    elif direction == "left":
        snake.setx(snakes[-1].xcor() - 20)
    elif direction == "up":
        snake.sety(snakes[-1].ycor() + 20)
    elif direction == "down":
        snake.sety(snakes[-1].ycor() - 20)
    # add the new snake head and position to the lists
    pos.append(tuple(snake.pos()))
    snakes.append(snake)

    # tick and update the screen
    screen.update()
    time.sleep(0.1)


screen.exitonclick()

