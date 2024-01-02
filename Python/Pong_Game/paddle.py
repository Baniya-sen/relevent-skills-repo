from turtle import Turtle

# Constants
PADDLE_SHAPE, PADDLE_COLOR = "square", "white"
PADDLE_WIDTH, PADDLE_HEIGHT = 3, 1
PADDLE_DISTANCE = 20
SCREEN_HEIGHT = 600  # Screen height should be same from main.py


class Paddle(Turtle):
    """Creates a paddle with desired width and height"""
    def __init__(self, position_x, position_y):
        super().__init__()
        self.penup()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.x_position = position_x
        self.y_position = position_y
        self.setposition(x=self.x_position, y=self.y_position)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)

    def move_up(self):
        """Moves the paddle up"""
        current_position_y = self.ycor()
        # Move only 43% of screen to prevent paddle going beyond screen height
        if current_position_y < int(SCREEN_HEIGHT * 43 / 100):
            self.setposition(x=self.x_position, y=current_position_y + PADDLE_DISTANCE)

    def move_down(self):
        """Moves the paddle down"""
        current_position_y = self.ycor()
        if current_position_y > -(int(SCREEN_HEIGHT * 43 / 100)):
            self.setposition(x=self.x_position, y=current_position_y - PADDLE_DISTANCE)

    def reset_paddle(self):
        self.setposition(x=self.x_position, y=self.y_position)
