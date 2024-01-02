from turtle import Turtle
import random

# Constants
MOVE_DISTANCE = 5
CAR_WIDTH, CAR_HEIGHT = 0.4, 1
SCREEN_SIZE_HALF = int(600 / 2)  # Change if screen size changes in main.py
SCREEN_HEIGHT_EDGE = 240  # A less than half of screen height to put cars on random y-axis


class Cars:
    def __init__(self):
        """Creates empty containers for all cars"""
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self, user_level):
        """Creates a single car with 1 in 6 possibility that's keeps decreasing as level increases"""
        if 1 == random.randint(1, (7 - user_level)):
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_HEIGHT)
            new_car.setposition(SCREEN_SIZE_HALF, random.randint(-SCREEN_HEIGHT_EDGE, SCREEN_HEIGHT_EDGE))
            new_car.color((random.random(), random.random(), random.random()))
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars on x-axis"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increases cars speed if when game leveled up"""
        self.car_speed += MOVE_DISTANCE
