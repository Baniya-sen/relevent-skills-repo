import turtle
from PIL import Image
import pandas
import time

# Constants
BG_IMAGE = "blank_states_img.gif"  # Background image location
CSV_FILE = "50_states.csv"  # CSV input file location


def main():
    screen, kachua = initializers()
    states_data = pandas.read_csv(CSV_FILE)
    user_score = 0
    total_points = len(states_data)
    record_list = set()

    # Main game loop
    while user_score <= total_points:
        try:
            user_input = screen.textinput(title=f"{user_score}/{total_points} Guess the state",
                                          prompt="Can you guess the state name?").title()
            # If user inputs exit, close window immediately
            if user_input == "Exit":
                break
            # If user input is valid state and not duplicate entry, score 1 point, and print state on map
            elif user_input in states_data["state"].to_list() and user_input not in record_list:
                state_info = states_data.state == user_input
                x_cords = states_data.x[state_info].values[0]
                y_cords = states_data.y[state_info].values[0]
                kachua.goto(x_cords, y_cords)
                kachua.write(user_input, font=("Comic Sans MS", 8, "bold"))
                record_list.add(user_input)
                user_score += 1
                time.sleep(0.6)
            else:
                time.sleep(0.2)
        except AttributeError:
            break

    exit_game(record_list, states_data)


def initializers():
    """Initializes all elements of game"""
    screen = turtle.Screen()
    screen.title("Us.States-Guessing")
    screen.addshape(BG_IMAGE)
    # Get image size to match screen size as image size
    with Image.open(BG_IMAGE) as bg_image:
        image_width, image_height = bg_image.size

    screen.setup(image_width, image_height)
    turtle.shape(BG_IMAGE)
    kachua = turtle.Turtle()
    kachua.penup()
    kachua.hideturtle()

    return screen, kachua


def exit_game(guessed_states, all_states):
    """Creates a csv file that holds all states that are not guessed by user"""
    non_guessed_states = [state for state in all_states["state"] if state not in guessed_states]
    pandas.DataFrame(non_guessed_states).to_csv("non_guessed_states.csv")
    turtle.bye()


if __name__ == "__main__":
    main()
