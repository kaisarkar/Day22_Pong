import random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


left_paddle = Paddle((-390, 0))
right_paddle = Paddle((380, 0))
ball = Ball()


screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

ball_direction = random.choice([ball.move_top_right, ball.move_bottom_left])

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball_direction()
    # Check for collision with boundary
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()





screen.exitonclick()