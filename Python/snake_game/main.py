from turtle import Screen
from snake import Snakes
from food import Food
from scoreboard import Score
import time

# Constants
SCREEN_SIZE = 600
SCREEN_EDGE = 295


def main():
    """Main game loop"""
    screen, snake, food, score = snake_initializers()
    is_gameOn = True

    while is_gameOn:
        # Updating snake movement every 0.1 second
        time.sleep(0.1)
        snake.move()
        screen.update()

        # Detect collision with food
        if snake.snake_head.distance(food) < 10:
            time.sleep(0.05)
            food.refresh_food()
            score.update_score()
            snake.extend_snake()

        # Detect collision with wall
        snake_x = snake.snake_head.xcor()
        snake_y = snake.snake_head.ycor()
        if snake_x > SCREEN_EDGE or snake_x < -SCREEN_EDGE or snake_y > SCREEN_EDGE or snake_y < -SCREEN_EDGE:
            score.game_over()
            break

        # Detect snake collision with its tail
        for snake_block in snake.all_turtles[1:]:
            if snake.snake_head.distance(snake_block) < 2:
                screen.update()
                score.game_over()
                is_gameOn = False
                break

    # Close window after 2 seconds of game-over
    time.sleep(2)


def snake_initializers():
    """Initializes all objects require to build a snake"""
    screen = Screen()
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()

    snake = Snakes()
    food = Food()
    score = Score()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(screen.bye, "Escape")

    return screen, snake, food, score


if __name__ == "__main__":
    main()
