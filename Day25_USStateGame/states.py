from turtle import Turtle


class State(Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        self.name = state_name
        self.x = x
        self.y = y
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(x, y)

    def reveal_state(self):
        self.write(f"{self.name}", align="center", font=("Arial", 8, "bold"))