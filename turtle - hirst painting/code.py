"""
we are going to use a package called 'colorgram.py' ; its a python library that lets you extract colors from images,
(compared to other libraries, the colorgram algorithm's results are more intense)
image should be at same level of code to extract

pip install colorgram.py

"""

import turtle
import random
import colorgram
from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

colors = colorgram.extract("hirst_img.jpeg",30)          # extracting 8 colors from the image
print(colors)

new_colors = []
for i in colors:
    r=i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_colors.append((r,g,b))
print(new_colors)
# op : [(248, 248, 245), (240, 249, 245), (249, 238, 245), (235, 242, 249), (237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]


""" the first color will be for the background; so remove that 
    op : [(240, 249, 245), (249, 238, 245), (235, 242, 249), (237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]
"""

tim.hideturtle()

new_colors = [(240, 249, 245), (249, 238, 245), (235, 242, 249), (237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]
tim.speed("fast")
tim.penup()
tim.setheading(220)
tim.forward(320)
tim.setheading(0)


num_of_dots = 100


for i in range(1,num_of_dots+1):
    tim.dot(20,random.choice(new_colors))
    tim.forward(55)

    if i%10==0:
        tim.setheading(90)
        tim.forward(55)
        tim.setheading(180)
        tim.forward(550)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()



"""
0 - east

90 - north

180 - west

270 - south
"""