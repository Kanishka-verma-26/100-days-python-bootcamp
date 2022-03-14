import turtle
from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("turtle")


colors = ["red","blue","yellow","purple","cyan","orange","black","pink","gray","darkblue"]
direction = [0,90,180,270]
turtle.speed(3)
tim.width(8)

for i in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))            # setheading sets the orientation of the turtle to the angle