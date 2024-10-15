from turtle import Turtle

class TurtleHero (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0,y=-280)
        self.setheading(90)


    def move_up(self):
        self.forward(10)