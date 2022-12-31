from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time


screen=Screen()
screen.bgcolor('black')
screen.setup(800,600)

screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
screen.exitonclick()

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'W')
screen.onkey(l_paddle.go_down,'S')


flag=True
while flag:
    screen.update()
    time.sleep(0.1)