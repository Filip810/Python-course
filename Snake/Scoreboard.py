from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.setposition(x=0,y=270)
        self.refresh_score()

    def add_point(self):
        self.score += 1
        self.clear()
        self.refresh_score()
    def refresh_score(self):
        self.write(f"Score:{self.score}", move=False, align="center", font=('Arial', 20, 'normal'))

    def lose(self):
        self.setposition(0,0)
        self.write(f"You Lost :(", move=False, align="center", font=('Arial', 20, 'normal'))

