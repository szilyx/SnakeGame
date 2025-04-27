from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

MainScreen = Screen()
MainScreen.setup(width=600, height=700)
MainScreen.bgcolor("black")
MainScreen.title("Snake Game by F.Szilard")
MainScreen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
MainScreen.update()
MainScreen.listen()
MainScreen.onkey(snake.up, "Up")
MainScreen.onkey(snake.down, "Down")
MainScreen.onkey(snake.left, "Left")
MainScreen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    MainScreen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        game_is_on = False
        scoreboard.game_over_screen()
        break
    for seg in snake.segments:
        if seg == snake.head:
            pass
        else:
            if snake.head.distance(seg) < 10:
                game_is_on = False
                scoreboard.game_over_screen()
                break
MainScreen.exitonclick()