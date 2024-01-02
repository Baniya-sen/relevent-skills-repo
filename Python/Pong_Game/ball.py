from turtle import Turtle
import time

# Constants
BALL_SIZE = 1


class Ball(Turtle):
    """Creates a ball with desired length"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=BALL_SIZE, stretch_len=BALL_SIZE)
        self.penup()
        self.setposition(0, 0)
        self.x_distance = 10
        self.y_distance = 10
        self.ball_speed = 0.1

    def move_ball(self):
        """Moves the ball in one direction continuously"""
        current_pos = self.pos()
        self.setposition(current_pos[0] + self.x_distance, current_pos[1] + self.y_distance)

    def ball_bounce_y(self):
        """Bounces the ball to the right"""
        self.y_distance *= -1
        self.move_ball()

    def ball_bounce_x(self):
        """Bounces the ball to the left"""
        self.x_distance *= -1
        self.ball_speed *= 0.9
        self.move_ball()

    def ball_reset(self):
        """Resets the ball everytime player misses"""
        self.setposition(0, 0)
        self.ball_speed = 0.1
        time.sleep(1)
        self.ball_bounce_x()
