from turtle import Turtle
import random


class Food(Turtle):
    """Initializes a random dot on screen as food for snake"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("orange")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.4, stretch_len=0.4)
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-270, 270)
        self.setposition(random_x, random_y)
