import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars

cars = Cars()
scoreboard = Scoreboard()
player = Player()
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.listen()

game_is_on = True

def squish():
    for car in cars.all_cars:
        if player.distance(car.position()) < 1:
            game_is_on = False


while game_is_on:
    time.sleep(.1)
    screen.update()
    screen.ontimer(cars.create_car(), 500)




    if player.ycor() >= 280:
        print("you hit it")
        player.start()
        scoreboard.add_score()
