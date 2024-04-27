from turtle import Turtle

FONT = ('Ariel', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.make_the_scoreboard()

    def make_the_scoreboard(self):
        self.goto(-280, 250)
        self.write(f"Current Score : {self.score}", font=FONT)



    def increase_score(self):
        self.score += 1

    def add_score(self):
        self.clear()
        self.increase_score()
        self.make_the_scoreboard()
