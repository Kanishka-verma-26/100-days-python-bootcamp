import time
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


""" Creating a snake body """
segments = []

for i in range(3):
    segment_i = Turtle("square")
    segment_i.color("white")
    segment_i.penup()
    segment_i.goto(-20 * i, 0)
    segments.append(segment_i)


""" Move the snake """

game_is_on = True

""" Turn turtle animation on/off and set delay for update drawings. If n is given, only each n-th regular screen update 
is really performed. (Can be used to accelerate the drawing of complex graphics.) When called without arguments, returns
 the currently stored value of n. Second argument sets delay value (see delay()).
  
  syntax : turtle.tracer(n=None, delay=None)
  
  when we turn off the tracer then we need to '.update()' method for the screen updation.
  Perform a TurtleScreen update. To be used when tracer is turned off.
  """

turtle.tracer(0)        # turning off the tracer;  this gives the snake a smooth effect while moving
turtle.speed("slow")
while game_is_on:
    screen.update()
    for i in segments:
        i.forward(20)
        screen.update()
        time.sleep(1)



screen.exitonclick()