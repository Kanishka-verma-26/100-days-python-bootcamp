# 1) creating a square using turtle and returning on click

from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
for i in range(4):
    timmy.forward(100)
    timmy.right(90)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()