from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_RIGHT_SIDE, PADDLE_LEFT_SIDE = 350, 0
SCREEN_EDGE_X, SCREEN_EDGE_Y = 420, 285


def main():
    screen, r_paddle, l_paddle, ball, score = initializers()

    # Main game loop
    while True:
        time.sleep(ball.ball_speed)
        screen.update()
        ball.move_ball()

        # Detects paddle touch, if ball touches paddle or is near paddle and near screen edge
        if (ball.distance(r_paddle) < 26 and ball.xcor() > SCREEN_HEIGHT / 2 or
                ball.distance(l_paddle) < 26 and ball.xcor() < -(SCREEN_HEIGHT / 2)):
            ball.ball_bounce_x()

        # Detects upper and lower wall collision to bounce back
        ball_y_position = ball.ycor()
        if ball_y_position > SCREEN_EDGE_Y or ball_y_position < -SCREEN_EDGE_Y:
            ball.ball_bounce_y()

        # Detects collision with left and right wall, increases score and resets paddle and ball
        ball_x_position = ball.xcor()
        if ball_x_position > SCREEN_EDGE_X:
            score.left_point()
            ball.ball_reset()
            r_paddle.reset_paddle()
            l_paddle.reset_paddle()
        elif ball_x_position < -SCREEN_EDGE_X:
            score.right_point()
            ball.ball_reset()
            r_paddle.reset_paddle()
            l_paddle.reset_paddle()


def initializers():
    """Initializes all elements"""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("PONG Game")
    screen.tracer(0)

    # Initializes paddle with desired width and height
    right_paddle = Paddle(PADDLE_RIGHT_SIDE, PADDLE_LEFT_SIDE)
    left_paddle = Paddle(-PADDLE_RIGHT_SIDE, PADDLE_LEFT_SIDE)
    ball = Ball()
    score = Score()

    # Detects keypress- Up and Down, W and S
    screen.listen()
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")
    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(left_paddle.move_down, "s")

    return screen, right_paddle, left_paddle, ball, score


if __name__ == "__main__":
    main()
