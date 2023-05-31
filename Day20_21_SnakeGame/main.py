import time
from turtle import Screen
from snake import Snake

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
# Snake setup
# ===========
snakes = Snake()
print(snakes)

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

screen.exitonclick()
