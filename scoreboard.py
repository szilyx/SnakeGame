from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as HScore:
            self.highscore = int(HScore.read())
        self.goto(0, 280)
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()
        self.speed("fastest")
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", move=False, align='center', font=('Arial', 24, 'normal'))
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as HScore:
                HScore.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()