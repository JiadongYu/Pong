from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

import time
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Pong')
starting_coordinate = (350,0)
game_on = True
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))

score = Scoreboard()

ball = Ball()
ball.move()
sleep_time = 0.1


screen.listen()

while game_on:
    time.sleep(sleep_time)
    screen.onkey(right_paddle.moveup, 'Up')
    screen.onkey(right_paddle.movedown,'Down')
    screen.onkey(left_paddle.moveup, 'w')
    screen.onkey(left_paddle.movedown, 's')
    ball.move()
    # Detect collisions with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collisions with right paddle
    if ball.xcor() > 340 and ball.distance(right_paddle)<55 or ball.xcor() < -340 and ball.distance(left_paddle)<55:
        ball.collide()
        sleep_time * 0.95

    # Detect when rp misses
    elif ball.xcor() > 380:
        ball.out()
        score.update_left()

    # Detect when lp misses
    elif ball.xcor() < -380:
        ball.out()
        score.update_right()





    screen.update()


screen.exitonclick()

