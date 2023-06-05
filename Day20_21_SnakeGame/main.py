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
    snakes.move()
    # tick and manually update the screen after the new snake list is configured
    screen.update()
    time.sleep(0.1)

    #Detect collision with food
    if snakes.list[0].distance(food) < 15:
        food.refresh()
        scoreboard.scored()


screen.exitonclick()
