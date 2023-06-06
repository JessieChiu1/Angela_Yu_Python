from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# ==============================
# Screen setup & variable setup
# ==============================
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
game_on = True
# Disable animation initially
screen.tracer(0)

# ============
# Class setup
# ============
player1 = Paddle(xcor= 350, keyup="Up", keydown="Down")
player2 = Paddle(xcor= -350, keyup="w", keydown="s")
ball = Ball()
scoreboard = Scoreboard()

# =====================
# Screen event listener
# =====================
screen.listen()
screen.onkeypress(player1.go_up, player1.keyup)
screen.onkeypress(player1.go_down, player1.keydown)

screen.onkeypress(player2.go_up, player2.keyup)
screen.onkeypress(player2.go_down, player2.keydown)

# =========
# game loop
# =========

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(player1) < 50 or ball.xcor() < -320 and ball.distance(player2) < 50:
        ball.bounce_paddle()

    # Detect out of bound on player1 side
    if ball.xcor() > 380 and ball.distance(player1) >= 50:
        scoreboard.player2_scored()
        ball.reset_ball()

    if ball.xcor() < -380 and ball.distance(player2) >= 50:
        scoreboard.player1_scored()
        ball.reset_ball()

screen.exitonclick()