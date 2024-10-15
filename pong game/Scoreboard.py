from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position_x):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=position_x, y=250)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.score}", align="center", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def end_game(self, player1):
        end_screen = Turtle()
        end_screen.penup()
        end_screen.hideturtle()
        end_screen.color("white")
        end_screen.write(arg=f"game over player {player1} won", align="center", font=('Arial', 20, 'normal'))