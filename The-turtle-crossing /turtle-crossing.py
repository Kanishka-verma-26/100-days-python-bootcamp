from turtle import Turtle,Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=800,height=650)
screen.title("Turtle Crossing")
screen.tracer(0)        # turning off the animation


player = Player()
level = Scoreboard()
car_manager = CarManager()


# moving player
screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    # creating cars
    car_manager.create_car()
    car_manager.move_forward()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            level.end_game()
            game_is_on = False

    # detect successfull crossing
    if player.ycor() == 300:
        level.update_level()
        player.go_to_start()
        car_manager.level_up()






screen.exitonclick()