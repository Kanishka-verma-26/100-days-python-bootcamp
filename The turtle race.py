from turtle import Turtle,Screen
import random

screen = Screen()


""" as in this game the screen size plays a vital role; as any turtle who reaches the end of the screen 'WINS'.
so we can set the screen size using setup method such as 'screen.setup(500,400)' i.e. 500px wide and 400px high screen
"""

screen.setup(width=500,height=400)

""" turtle allow us to take 'textinput' which Pop up a dialog window for input of a string. Parameter title is the title
 of the dialog window, prompt is a text mostly describing what information to input. Return the string input. 
 If the dialog is canceled, return None. 
 
 syntax : turtle.textinput(title, prompt)
 """

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

turtle_color = ['red','purple','yellow','black','cyan','green']

y_position = [-70, -40, -10, 20, 50, 80]

all_turtles = []

is_race_on = False

""" to move each turtle to a certain position we will use 'turtle.goto(x, y=None)' where x and y width and height coordinates.
"""

for i in range(0,6):
    new_turtle= Turtle(shape ='turtle')
    new_turtle.color(turtle_color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_position[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        if i.xcor() > 230:          # looking for x-coordinates
            is_race_on = False
            # winning_color = i.color()                   # color() Return the current pencolor and the current fillcolor as a pair of color specification strings or tuples as returned by pencolor() and fillcolor().
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've WON!, the {winning_color} turtle is the winner.")
            else:
                print(f"You've LOST!, the {winning_color} turtle is the winner.")


        rand_dist = random.randint(0,10)
        i.forward(rand_dist)



screen.exitonclick()