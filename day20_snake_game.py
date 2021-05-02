from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen =Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")    


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15 :
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        game_is_on = False
        scoreboard.game_over()

    for segments in snake.segments[1: ]:
        # if segments == snake.head:
        #     pass
        if snake.head.distance(segments) <10:
            game_is_on = False
            scoreboard.game_over()
        
    


























# for numb in range(3):
#     tim = Turtle("square")
#     go = numb*20*-1
#     tim.goto(go)
#     tim.color("white")

    







screen.exitonclick()