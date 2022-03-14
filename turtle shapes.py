from turtle import Turtle,Screen
tim = Turtle()
tim.shape("turtle")

colors = ["red","blue","yellow","purple","cyan","orange","black","pink","gray","darkblue"]

def draw_shapes(sides):
    if sides <=10:
        angle = 360 / sides
        for j in range(sides):
            tim.color(colors[sides-3])
            tim.forward(100)
            tim.right(angle)

        draw_shapes(sides+1)
    else:
        return

draw_shapes(3)
