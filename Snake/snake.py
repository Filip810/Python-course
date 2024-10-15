from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        for i in range(0, 3):
            body = Turtle(shape="square")
            body.penup()
            body.shapesize(0.5, 0.5)
            body.color("white")
            body.speed("normal")
            body.setposition(-i * 10, 0)
            self.snake.append(body)
        self.head = self.snake[0]

    def move_forward(self):

        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)


        self.snake[0].forward(10)

    def move_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def move_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def move_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def move_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)


    def food_has_been_eatten(self):
        seg = Turtle(shape="square")
        seg.penup()
        seg.shapesize(0.5, 0.5)
        seg.color("white")
        seg.speed("slowest")
        seg.setposition(self.snake[-1].xcor() - 10,self.snake[-1].ycor()-10)
        self.snake.append(seg)



