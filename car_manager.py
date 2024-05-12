from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.new_car()
    
    def new_car(self):
        index = random.randint(0, len(COLORS)-1)
        car = Turtle(shape = 'square')
        car.penup()
        car.color(COLORS[index])
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(280, random.randint(-280, 280))
        self.car_list.append(car)

    def move(self):
        for x in range(0, len(self.car_list)):
            new_x = self.car_list[x].xcor() - STARTING_MOVE_DISTANCE
            self.car_list[x].goto(new_x, self.car_list[x].ycor())

