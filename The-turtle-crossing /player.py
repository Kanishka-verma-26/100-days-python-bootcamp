from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -300)
        self.setheading(90)

    def go_up(self):
        if self.ycor() < FINISH_LINE_Y:
            new_y = self.ycor()+MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(0, -300)