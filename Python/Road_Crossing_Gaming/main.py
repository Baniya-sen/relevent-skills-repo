from turtle import Screen
from cars import Cars
from player import Player
from scoreboard import Score
import time

# Constants
SCREEN_SIZE = 600


def main():
    screen, cars, player, score = initializers()
    is_game_on = True

    # Main game loop
    while is_game_on:
        # Updates screen every 0.1 second
        time.sleep(0.1)
        screen.update()

        # Creates a car in every loop run
        cars.create_car(score.level)
        cars.move_cars()

        # Detects collision of cars with turtle
        for car in cars.all_cars:
            if player.distance(car) < 15:
                score.game_over()
                is_game_on = False
                break

        # If turtle reaches upper line, reset turtle and increase level
        if player.ycor() > 285:
            player.starting_position()
            cars.level_up()
            score.level_up()

    # Wait a second before closing window
    time.sleep(1)


def initializers():
    """Abstract of all initialized elements"""
    screen = Screen()
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.title("Turtle Crossing")
    screen.bgcolor("black")
    screen.tracer(0)

    cars = Cars()
    player = Player()
    score = Score()

    # Listens for keypress- Up
    screen.listen()
    screen.onkey(player.move, "Up")

    return screen, cars, player, score


if __name__ == "__main__":
    main()
