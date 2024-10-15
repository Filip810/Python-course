import time
from turtle import  Screen
from scoreboard import ScoreBoard
from turtles import Turtles
from turtlehero import TurtleHero

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

turtles = Turtles()
john = TurtleHero()
scoreboard = ScoreBoard()

screen.listen()

screen.onkeypress(key="w", fun=john.move_up)


game_is_on = True
while game_is_on:
    turtles.add_turtle()
    turtles.move_all_turtles()


    #detect collision with other turtles
    for turtle in turtles.turtles:
        if abs(turtle.xcor() - john.xcor()) <20 and abs(turtle.ycor()- john.ycor()) < 20:
            scoreboard.end_game()
            game_is_on = False

    #detect next level
    if john.ycor() > 300:
        john.goto(x = 0, y = -280)
        scoreboard.update_scoreboard()
        turtles.increase_lvl()

    #detect end game

    if scoreboard.score == 10:
        game_is_on = False

    turtles.delete_turtle()

    screen.update()
    time.sleep(0.1)


screen.exitonclick()