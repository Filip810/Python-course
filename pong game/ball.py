from turtle import Turtle
from random import randint,choice

positions = [randint(0,45), randint(315,360)]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")


    def move(self):
        self.forward(20)

    def is_there_collision(self,paddle):
         if abs(self.xcor()-paddle.xcor()) <= 21 and abs(self.ycor()-paddle.ycor()) <= 41:
            if self.heading() < 45 or self.heading() > 315:
                self.setheading(randint(135,225))
            else:
                self.setheading(choice(positions))


    def collision_with_wall(self):
        if self.ycor() > 300:
            if 90 < self.heading() < 270:
                current_heading = self.heading()
                self.setheading(current_heading + randint(45,90))
            else:
                current_heading = self.heading()
                self.setheading(current_heading - randint(45,90))
        if self.ycor() < -300:
            if 90 < self.heading() < 270:
                current_heading = self.heading()
                self.setheading(current_heading - randint(45,90))
            else:
                current_heading = self.heading()
                self.setheading(current_heading + randint(45,90))






