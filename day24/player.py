from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.start()
        self.restart()

    def start(self):
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(0, new_y)

    def restart(self):
        if self.ycor() >= 280:
            self.start()




