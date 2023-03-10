from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # 2 #

snake = Snake()

food = Food()

score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()  # 2 #
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.curr_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset()
        #  score.game_over() # this method was replaced with reset
        #  game_is_on = False # this method was replaced with reset
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score.reset_score()


screen.exitonclick()
