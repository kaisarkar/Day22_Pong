from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        # Upper boundary is 250 to account for paddle height
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        # Lower boundary is -250 to account for paddle height
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)
