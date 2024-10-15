import time
from turtle import Screen
from ball import Ball
from keyboardmenager import KeyboardManager
from Scoreboard import Scoreboard
from racket import Racket



screen = Screen()
screen.setup(width=800,height=600)
screen.tracer(0)
screen.title("PongGame")
screen.bgcolor("Black")

left_racket = Racket(position_x=-370)
right_racket = Racket(position_x= 370)

ball = Ball()

scoreboard_left = Scoreboard(-100)
scoreboard_right = Scoreboard(100)

screen.listen()


keys_pressed = KeyboardManager(screen)


screen.onkeypress(keys_pressed.press_w, "w")
screen.onkeyrelease(keys_pressed.release_w, "w")

screen.onkeypress(keys_pressed.press_s, "s")
screen.onkeyrelease(keys_pressed.release_s, "s")

screen.onkeypress(keys_pressed.press_up, "Up")
screen.onkeyrelease(keys_pressed.release_up, "Up")

screen.onkeypress(keys_pressed.press_down, "Down")
screen.onkeyrelease(keys_pressed.release_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    ball.move()

    #Detect colision with racket
    ball.is_there_collision(right_racket)
    ball.is_there_collision(left_racket)

    #Detect collision with wall
    ball.collision_with_wall()

    #increase scoreboard
    if ball.xcor() > 420:
        ball.goto(0,0)
        right_racket.goto(right_racket.xcor(),0)
        left_racket.goto(left_racket.xcor(), 0)
        ball.setheading(0)
        scoreboard_left.increase_score()
        time.sleep(1)
    if ball.xcor() < -420:
        ball.goto(0,0)
        right_racket.goto(right_racket.xcor(),0)
        left_racket.goto(left_racket.xcor(), 0)
        ball.setheading(180)
        scoreboard_right.increase_score()
        time.sleep(1)

    #End game

    if scoreboard_left.score == 5:
        scoreboard_left.end_game("Left")
        game_is_on = False
    elif scoreboard_right.score == 5:
        scoreboard_right.end_game("right")
        game_is_on = False



    if left_racket.ycor() <240:
        if keys_pressed.keys_pressed["w"]:
            left_racket.go_up()
    if left_racket.ycor() > -240:
        if keys_pressed.keys_pressed["s"]:
            left_racket.go_down()
    if right_racket.ycor() < 240:
        if keys_pressed.keys_pressed["Up"]:
            right_racket.go_up()
    if right_racket.ycor() > -240:
        if keys_pressed.keys_pressed["Down"]:
            right_racket.go_down()

screen.exitonclick()