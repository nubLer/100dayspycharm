from turtle import Turtle
import random


COLORS = ["red", "blue", "green", "yellow", "purple"]
MOVEMENT = 20


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_car()
        self.cars_move_to_wall()

    def cars_move_to_wall(self):
        for car in self.all_cars:
            if car.xcor() <= -280:
                car.clear()
            else:
                self.move_car()

    def create_car(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.penup()
        new_car.goto(self.location_car)
        self.cars_move_to_wall()
        self.all_cars.append(new_car)

    @property
    def location_car(self):
        x = 280
        random_y = random.randint(-280, 280)
        return x, random_y

    def move_car(self):
        for car in self.all_cars:
            new_x = car.xcor() - MOVEMENT
            car.goto(new_x, car.ycor())
