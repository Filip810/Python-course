from turtle import Turtle

class ScoreBoard():
    def __init__(self):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(x=-200,y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.scoreboard.clear()
        self.scoreboard.write(arg= f"level: {self.score}", move=False, font=('Arial', 20, 'normal'))

    def end_game(self):
        self.scoreboard.clear()
        self.scoreboard.goto(x=-100,y=0)
        self.scoreboard.write(arg=f"YOU LOST :(", move=False, font=('Arial', 20, 'normal'))

