from turtle import Turtle
FONT = ("Courier",15,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280,290)
        self.level = 1
        self.write(f"Level : {self.level}",align="right",font = FONT)


    def update_level(self):
        self.level +=1
        self.clear()
        self.goto(-280, 290)
        self.write(f"Level : {self.level}", align="right", font=FONT)


    def end_game(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write("GAME OVER!!!", align="center", font=("Courier",20,"normal"))