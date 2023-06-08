import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Car

# ==============================
# Screen setup & variable setup
# ==============================
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=650)
screen.title("Turtle Crossing")
game_on = True
cars = []
counter = 0

# ===========
# Class setup
# ===========
player = Player()
scoreboard = Scoreboard()

# ==============
# Event listener
# ==============
screen.listen()
screen.onkeypress(player.move, "Up")

# =============
# Gameplay Loop
# =============
while game_on:
    time.sleep(scoreboard.speed)
    screen.update()
    counter += 1

    # Create new cars every 6 gameplay loop
    if counter%6 == 0:
        car = Car()
        cars.append(car)

    # Move cars
    for car in cars:
        car.move()
        if car.xcor() < -350:
            cars.remove(car)
            car.hideturtle()
            car.clear()

    # Detect turtle crossing
    if player.detect_finish():
        player.reset()
        scoreboard.next_level()

    # Detect collision
    for car in cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
