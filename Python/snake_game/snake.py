from turtle import Turtle
import time

# Constants
TURTLE_INITIAL_POSITION = [(0, 0), (-10, 0), (-20, 0)]
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
TURTLE_INITIAL_LENGTH = 3
TURTLE_DISTANCE = 10


class CreateSnake:
    """Initializes an instance of Turtle class"""
    def __init__(self, snake_shape, snake_color, snake_size):
        self.new_kachua = Turtle(snake_shape)
        self.new_kachua.color(snake_color)
        self.new_kachua.shapesize(stretch_wid=snake_size, stretch_len=snake_size)
        self.new_kachua.penup()


class Snakes:
    """Control snake creation and its behaviour"""
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.snake_head = self.all_turtles[0]

    def create_snake_block(self, turtle_position):
        """Creates a single snake block"""
        main_kachua = CreateSnake(snake_shape="square", snake_color="white", snake_size=0.5)
        main_kachua.new_kachua.setposition(turtle_position)
        self.all_turtles.append(main_kachua.new_kachua)

    def create_snake(self):
        """Creates 3-initial snake-block, position each snake-block just adjacent to previous one"""
        for position in TURTLE_INITIAL_POSITION:
            self.create_snake_block(position)

    def move(self):
        """Moves the snake forward"""
        for kachua_index in range(len(self.all_turtles) - 1, 0, -1):
            previous_position = self.all_turtles[kachua_index - 1].position()
            self.all_turtles[kachua_index].setposition(previous_position)

        # Move the head of snake and now tail will follow
        self.snake_head.forward(TURTLE_DISTANCE)

    def extend_snake(self):
        """Extent snake with a block everytime it collide with a food item"""
        self.create_snake_block(self.all_turtles[-1].position())

    def up(self):
        """Moves snake upward"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
            self.move()

    def down(self):
        """Moves snake downward"""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
            self.move()

    def left(self):
        """Moves snake left-side"""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
            self.move()

    def right(self):
        """Moves snake right-side"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
            self.move()
