from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def movecc():
    timmy.left(10)


def movec():
    timmy.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=movecc)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=movec)
screen.exitonclick()
