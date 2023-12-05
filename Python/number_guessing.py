import random


def main():
    print(logo, end="\n\n")
    print("Ram Ram bhai sareya ne.. Number game mai swaagat hai!", end='\n\n')
    print("Lets play a number guessing game. I am thinking of a number between 0 and 100...")
    choice = random.randint(0, 101)

    # Ask user for difficulty level, easy = 10 attempts, hard = 5
    difficulty = input('Are you up for "Hard" level or wanna take it "Easy". Enter choice: ').lower()
    attempts = 5
    if difficulty == "easy":
        attempts = 10
    elif difficulty != "hard":
        print("Wrong choice.. Gonna go HARD on you!")

    # Run loop until attempts are exhausted
    for i in range(attempts, -1, -1):
        if i == 0:
            print("\nTimes up! You lose. The number was", choice)
            break
        while True:  # We make sure input is a integer
            try:
                print(f"\nYou have {i} attempts left.")
                guess = int(input("Guess the Number: "))
                break
            except ValueError:
                pass
        if guess == choice:
            print(f"\nThat's correct! The number was {choice}.")
            break
        else:
            validate(guess, choice)
            pass


def validate(user_guess, number):
    """Tells the user how much their number is farther or closer to guessed number"""
    if user_guess > number:
        diff = user_guess - number
        if diff > 50:
            print("Too high!")
        elif diff > 25:
            print("Very high!")
        elif diff > 10:
            print("Bit high!")
        elif diff > 5:
            print("Slightly high!")
        else:
            print("Maybe a 1 or 2 places high!")
    else:
        diff = number - user_guess
        if diff > 50:
            print("Too low!")
        elif diff > 25:
            print("Very low!")
        elif diff > 10:
            print("Bit low!")
        elif diff > 5:
            print("Slightly low!")
        else:
            print("Maybe a 1 or 2 places low!")


logo = """
     __                 _                   ___                     _             
  /\ \ \_   _ _ __ ___ | |__   ___ _ __    / _ \_   _  ___  ___ ___(_)_ __   __ _ 
 /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|  / /_\/ | | |/ _ \/ __/ __| | '_ \ / _` |
/ /\  /| |_| | | | | | | |_) |  __/ |    / /_\\| |_| |  __/\__ \__ \ | | | | (_| |
\_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    \____/ \__,_|\___||___/___/_|_| |_|\__, |
                                                                            |___/ 
"""

main()
