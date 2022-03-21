import time
import turtle
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# step 1: Setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong")
screen.tracer(0)        # turning off the animation


# step 2: set up the left and right paddle

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


# step 3: Setting up the ball
ball = Ball()


score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # step 4: detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    # step 5: detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320 :          # condition according to the coordinates of paddles
        ball.bounce_x()

    # step : 6 (through this we will

    # detect when R paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    # detect when L paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()