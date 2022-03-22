import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("India States Game")
image = "us_map.gif"
screen.addshape(image)                  # adding the image as screen shape

turtle.shape(image)                     # setting up the image shape


""" getting Co-ordinates of each state and storing them in csv"""

# def get_mouse_click_coords(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coords)
#
# turtle.mainloop()                               # its an alternative to screen.exitonclick(); it helps in keeping our screen open even though our code has finished running.




""" input popup """
correct_states = []
dataframe = pandas.read_csv("50_states.csv")
while len(correct_states) < 5:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                    prompt="What's the another state's name?").title()

    if answer_state in (dataframe.state.to_list()) :
        if answer_state not in correct_states:
            correct_states.append(answer_state)
            data = dataframe[dataframe.state == answer_state]
            t=Turtle()                                          # creating new object of turtle else screen will play all the roles
            t.hideturtle()
            t.penup()
            x = data.x
            y = data.y
            t.goto(int(x),int(y))
            t.write(answer_state)
    elif answer_state == 'Exit':
        missed_states = [state for state in dataframe.state.to_list() if state not in correct_states]

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("States_to_learn.csv")
        break


print(answer_state)





