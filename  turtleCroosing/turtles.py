from turtle import Turtle
from random import randint,choices


def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    new_color = (r, g, b)

    return new_color



class Turtles():
    def __init__(self):
        self.turtles = []
        self.level = [0.9,0.1]

    def add_turtle(self):
        print(self.level)

        do_we_add = choices(population =[0,1],weights=self.level,k=1)
        print(do_we_add)
        if do_we_add[0] == 1:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("turtle")
            new_turtle.color(random_color())
            new_turtle.setposition(x=-320, y=randint(-250,280))
            self.turtles.append(new_turtle)

    def move_all_turtles(self):
        for turtle in self.turtles:
            turtle.forward(randint(10,30))


    def increase_lvl(self):
        self.level[0] -= 0.1
        self.level[1] += 0.1

    def delete_turtle(self):
        for t in self.turtles:
            if t.xcor() > 250:
                t.clear()
                t.hideturtle()
                self.turtles.remove(t)




