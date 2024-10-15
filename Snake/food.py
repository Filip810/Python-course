from turtle import  Turtle
from random import  randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.25,0.25)
        self.color("red")
        self.speed("fastest")
        self.replace_food()

    def replace_food(self):
        random_x = randint(-280,280)
        random_y = randint(-280,280)
        self.goto(random_x,random_y)
