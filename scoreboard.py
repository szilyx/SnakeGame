from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()
        self.speed("fastest")
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over_screen(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over! Your score was: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))