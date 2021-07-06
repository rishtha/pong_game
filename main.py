from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height=600)
screen.bgcolor("black")
screen.tracer(0)

lpaddle = Paddle((-350, 0))
rpaddle = Paddle((350, 0))
striker = Ball()
score = Scoreboard()


screen.listen()
#right paddle control
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")

#left paddle control
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(striker.move_speed)

    screen.update()
    striker.move()

    if(striker.ycor() > 280 or striker.ycor() < -280 ):
        striker.bounce_y()


  #detect collision with right paddle
    if striker.distance(rpaddle) < 50 and striker.xcor() > 320 or striker.distance(lpaddle) < 50 and striker.xcor() < -320:
        #print("collided")
        striker.bounce_x()



    #detect right paddle miss
    if striker.xcor() > 380 :
        striker.reset_position()
        score.l_point()



    #detect left paddle miss
    if striker.xcor() < -380 :
        striker.reset_position()
        score.r_point()



screen.exitonclick()