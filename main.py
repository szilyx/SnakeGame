from turtle import Screen
from snake import Snake
from food import Food
import time

MainScreen = Screen()
MainScreen.setup(width=600, height=700)
MainScreen.bgcolor("black")
MainScreen.title("Snake Game by F.Szilard")
MainScreen.tracer(0)

snake = Snake()
food = Food()
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

MainScreen.exitonclick()