from turtle import Turtle


class Snake:

    def __init__(self):
        self.position = [(-40, 0), (-20, 0), (0, 0)]
        self.list = []
        self.direction = "right"
        for position in self.position:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(position)
            self.list.append(snake)

    def move(self):
        """

        :param pos: set of snake's positions
        :param self.direction: self.direction of arrow
        :return: none
        Logic is that technically at each tick, the only changes are the tails disappear a new head appear
        """
        # pop the position and snake of the tail in lists
        snake = self.list.pop(0)
        self.position.pop(0)
        if self.direction == "right":
            snake.setpos(self.list[-1].xcor() + 20, self.list[-1].ycor())
        elif self.direction == "left":
            snake.setpos(self.list[-1].xcor() - 20, self.list[-1].ycor())
        elif self.direction == "up":
            snake.setpos(self.list[-1].xcor(), self.list[-1].ycor() + 20)
        elif self.direction == "down":
            snake.setpos(self.list[-1].xcor(), self.list[-1].ycor() - 20)
        # add the new snake head and position to the lists
        self.position.append(tuple(snake.pos()))
        self.list.append(snake)

    def set_direction_up(self):
        self.direction = "up"

    def set_direction_down(self):
        self.direction = "down"

    def set_direction_right(self):
        self.direction = "right"

    def set_direction_left(self):
        self.direction = "left"
