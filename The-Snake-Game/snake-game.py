from turtle import Turtle, Screen
import time
import turtle
import random

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    """ Step 1: Create snake """

    def create_snake(self):
        for i in range(3):
            # self.add_segment(i)
            segment_i = Turtle("square")
            segment_i.color("white")
            segment_i.penup()
            segment_i.goto(-20 * i, 0)
            self.segments.append(segment_i)

    def add_segment(self, position):
        segment_i = Turtle("square")
        segment_i.color("white")
        segment_i.penup()
        segment_i.goto(position)
        self.segments.append(segment_i)

    def reset(self):
        for seg in self.segments:  # as the game ends we are suppose to start again with a new snake so we are sending the previous snake at position (1000,1000) far away from our screen
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to snake
        self.add_segment(self.segments[-1].position())  # passing the position of the last segment

    """ Step 2: Move snake """

    def move(self):

        """ Turn turtle animation on/off and set delay for update drawings. If n is given, only each n-th regular screen update
        is really performed. (Can be used to accelerate the drawing of complex graphics.) When called without arguments, returns
         the currently stored value of n. Second argument sets delay value (see delay()).

          syntax : turtle.tracer(n=None, delay=None)

          when we turn off the tracer then we need to '.update()' method for the screen updation.
          Perform a TurtleScreen update. To be used when tracer is turned off.
          """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DIST)

    """ Step 3: Control Snake"""

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


""" Step 4: Detect Collission with Food """


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,
                       stretch_wid=0.5)  # bydefault a turtle is of size 20x20 pixels, we are chnging it to 10x10 pixels
        self.color("blue")
        self.speed("fastest")
        self.refresh_coords()

    def refresh_coords(self):
        random_x = random.randint(-280, 280)  # as our screen is of size 300x300 coordinates
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


""" Step 5: Create a score board and keeping record of high score """

""" we can write inside our screen using 'write' method.

Write text - the string representation of arg - at the current turtle position according to align 
(“left”, “center” or “right”) and with the given font. If move is true, the pen is moved to the bottom-right 
corner of the text. By default, move is False.

syntax : turtle.write(arg, move=False, align='left', font='Arial', 8, 'normal')

    arg – object to be written to the TurtleScreen

    move – True/False

    align – one of the strings “left”, “center” or right”

    font – a triple (fontname, fontsize, fonttype)


** turtle.clear()

Delete the turtle’s drawings from the screen. Do not move turtle. State and position of the turtle as well as drawings 
of other turtles are not affected.

"""


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:              # reading from the file to get the high score
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.highscore}", align='center',
                   font=('Courier', 22, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Oops!! GAME OVER", align='center', font=('Courier', 25, 'normal'))


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

""" Step 3 : Control snake """

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

""" Step 2 : Move the snake """
game_is_on = True

turtle.tracer(0)  # turning off the tracer;  this gives the snake a smooth effect while moving
turtle.speed("slow")
turtle.hideturtle()
while game_is_on:
    screen.update()  # as tracer is off hence we need to update our screen at every step
    time.sleep(0.15)

    snake.move()

    """ Step 4,5 : Detect collision with food and score board """

    """ we will detect the collision of food and snake using 'distance' method which Return the distance from the turtle
     to (x,y), the given vector, or the given other turtle, in turtle step units. 

     syntax : turtle.distance(x, y=None)
     x : a number or a pair/vector of numbers or a turtle instance
     y : a number if x is a number, else None
     """
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh_coords()

    """ Step 6: Detect collision with Wall """
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    """ Step 7: Detect collision with Tail """
    # if head collides with any segment of the tail:
    # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()