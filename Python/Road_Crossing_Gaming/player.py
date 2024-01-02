from turtle import Turtle
import time

# Constants
TURTLE_SIZE = 1


class Player(Turtle):
    def __init__(self):
        """Creates a turtle avatar"""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("orange")
        self.setheading(90)
        self.starting_position()
        self.shapesize(stretch_wid=TURTLE_SIZE, stretch_len=TURTLE_SIZE)

    def starting_position(self):
        """Places turtle on a starting position"""
        time.sleep(0.5)
        self.setposition(x=0, y=-280)

    def move(self):
        """Moves the turtle forward"""
        self.forward(10)
