from random import choice
from turtle import Turtle,Screen
import colorgram

my_colors = colorgram.extract('image.jpg', 20)
def random_color_gen(turtle):
    random_color = choice(my_colors)
    turtle.pencolor((int(random_color.rgb[0]), int(random_color.rgb[1]), int(random_color.rgb[2])))

screen = Screen()
screen.colormode(255)

john = Turtle()
john.shape("turtle")
john.pencolor("red")
john.speed("fastest")
john.pensize(15)



for i in range (-5,5):
    john.penup()
    john.setposition(-200, i * 50)
    for j in range (1,10):
        random_color_gen(john)
        john.dot(20)
        john.forward(50)






screen.exitonclick()
