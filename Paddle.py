from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_coordinates):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_coordinates)

    def moveup(self):
        new_y_pos = self.ycor() + 20
        self.goto(self.xcor(), new_y_pos)

    def movedown(self):
        new_y_pos = self.ycor() - 20
        self.goto(self.xcor(), new_y_pos)
