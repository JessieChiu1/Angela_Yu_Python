import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# ==============================
# Screen setup & variable setup
# ==============================

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake")
game_on = True
extend = False
# Disable animation initially
screen.tracer(0)

# ===========
# Class setup
# ===========
snakes = Snake()
food = Food()
scoreboard = Scoreboard()

# =====================
# Screen event listener
# =====================

screen.listen()
screen.onkey(snakes.set_direction_up, "Up")
screen.onkey(snakes.set_direction_down, "Down")
screen.onkey(snakes.set_direction_right, "Right")
screen.onkey(snakes.set_direction_left, "Left")

# =========
# game loop
# =========

while game_on:
    # tick and manually update the screen after the new snake list is configured
    if extend:
        snakes.extend()
    extend = False
    screen.update()
    time.sleep(0.1)
    snakes.move()

    # Detect collision with food
    if snakes.list[0].distance(food) < 15:
        food.refresh()
        scoreboard.scored()
        time.sleep(0.1)
        extend = True

    # Detect collision with walls
    if snakes.list[0].xcor() > 280 or snakes.list[0].xcor() < -280 or snakes.list[0].ycor() > 280 or snakes.list[0].ycor() < -280:
        game_on = False
        scoreboard.gameOver()

    # Detect collision with body it is supposed to be from list[1:] onward but because we don't know the specific
    # distance calculation [2:] works better
    for body in snakes.list[2:]:
        if snakes.list[0].distance(body) < 10:
            game_on = False
            scoreboard.gameOver()
            print(snakes.position)

screen.exitonclick()
