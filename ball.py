from turtle import Turtle

class Ball(Turtle):
    def __init__ (self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1
        self.move()

    def collide(self):
        self.xmove *= -1
        self.ymove *= -1
        self.move()

    def out(self):
        self.xmove *= -1
        self.ymove *= -1
        self.goto(0,0)
        self.move()






