import time
from asyncore import write
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from Scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


john_the_snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()

screen.onkey(key="w", fun=john_the_snake.move_up)
screen.onkey(key="a", fun=john_the_snake.move_left)
screen.onkey(key="d", fun=john_the_snake.move_right)
screen.onkey(key="s", fun=john_the_snake.move_down)

while game_is_on:


    john_the_snake.move_forward()
    screen.update()
    time.sleep(0.1)


    #Detect collision with food
    if john_the_snake.head.distance(food) < 10:
        john_the_snake.food_has_been_eatten()
        food.replace_food()
        scoreboard.add_point()
        scoreboard.refresh_score()


    #Detect collision with wall
    if -280 > john_the_snake.head.position()[0] or john_the_snake.head.position()[0] > 280 or -280 > john_the_snake.head.position()[1] or  john_the_snake.head.position()[1] > 280:
        game_is_on = False
        scoreboard.lose()

    #detect collision with own tail
    for segment in john_the_snake.snake:
        if segment == john_the_snake.head:
            pass
        elif john_the_snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.lose()




screen.exitonclick()