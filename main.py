from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# screen.tracer(0) & screen.update()


left_paddle = Paddle((-390, 0))
right_paddle = Paddle((380, 0))
ball = Ball()


screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")




screen.exitonclick()