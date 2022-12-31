from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        ball=Turtle()
        ball.shape('circle')
        ball.color('white')
        ball.penup()
        self.xmove=10
        self.ymove=10
        

    def move(self):
        new_x= self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)

    def bounce(self):
        self.ymove *= -1
        