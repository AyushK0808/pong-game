from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self=Turtle()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1
        

    def move(self):
        new_x= self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)

    def bounce(self):
        self.ymove *= -1

    def paddlebounce(self):
        self.xmove *= -1
        self.move_speed *=0.8
    
    def reset(self):
        self.goto(0,0)
        self.movespeed=0.1
        self.paddlebounce()