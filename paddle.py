from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        paddle=Turtle()
        paddle.shape('square')
        paddle.shapesize(stretch_len=1,stretch_wid=5)
        paddle.color('white')
        paddle.penup()
        paddle.goto(350,0)
    
    
    def go_up(self):
        new_y= self.ycor()+20
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y= self.ycor()-20
        self.goto(self.xcor(),new_y)