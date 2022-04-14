from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.rscore = 0
        self.lscore = 0
        self.update_score()

    def update_score(self):
        self.goto(-100,200)
        self.write(self.lscore, align = 'Center', font = ('Courier', 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align='Center', font=('Courier', 80, "normal"))

    def update_right(self):
        self.clear()
        self.rscore += 1
        self.update_score()



    def update_left(self):
        self.clear()
        self.lscore += 1
        self.update_score()

