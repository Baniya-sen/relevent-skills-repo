# Password Generator
import random
import sys

# Defining chars to include on password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# List of all lists
all_password_list = [letters, symbols, numbers]


def greet():
    print("Welcome to the PyPassword Generator!\n")


# Taking input of how many letters, symbols, and number user want in password
def take_input():
    nr_letters = input("How many letters would you like in your password? ")
    nr_symbols = input(f"How many symbols would you like? ")
    nr_numbers = input(f"How many numbers would you like? ")
    print("")

    if not (nr_letters.isdigit()) or not (nr_symbols.isdigit()) or not (nr_numbers.isdigit()):
        print("ERROR: Enter only whole numbers!")
        sys.exit()

    return int(nr_letters), int(nr_symbols), int(nr_numbers)


# Get password hash
def get_password(letter_len, symbol_len, number_len):
    password_hash = ""

    for i in range(0, (letter_len + symbol_len + number_len)):
        initial_length = len(password_hash)

        while True:
            random_list = random.randint(0, len(all_password_list) - 1)
            random_char = random.randint(0, len(all_password_list[random_list]) - 1)

            if random_list == 0 and letter_len != 0:
                password_hash += letters[random_char]
                letter_len -= 1
            elif random_list == 1 and symbol_len != 0:
                password_hash += symbols[random_char]
                symbol_len -= 1
            elif random_list == 2 and number_len != 0:
                password_hash += numbers[random_char]
                number_len -= 1

            if len(password_hash) == initial_length + 1:
                break

    return password_hash


if __name__ == "__main__":
    greet()
    letter_size, symbol_size, number_size = take_input()

    # Condition to check to make sure it is viable password
    if letter_size > 25 or symbol_size > 25 or number_size > 25:
        print("Enter valid password range! Under 25 for all!")
        sys.exit()

    password = get_password(letter_size, symbol_size, number_size)

    print(password)
