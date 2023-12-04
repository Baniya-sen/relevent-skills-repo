import os
import random

# Constants
CARD_VALUES = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def deck_shuffle():
    """Return a random card value"""
    return random.choice(CARD_VALUES)


def calculate(card):
    """Calculates and prints who won"""
    total = sum(card)

    if total == 21 and len(card) == 2:
        return 0

    if 11 in card and total > 21:
        card.remove(11)
        card.append(1)
        total = sum(card)

    return total


def end_compare(user_scores, dealer_scores, user_card, dealer_card):
    """If user chooses end, then who has the highest score wins"""

    if user_scores == dealer_scores:
        print("\nIt's a Draw!")
    elif user_scores == 0 or dealer_score > 21 >= user_scores:
        print("\nYOU WON BlackJack!")
    elif dealer_scores == 0 or user_scores > 21:
        print("\nYou Lose! NoJack.")
    else:
        print("You Lose!")

    print(f"Your hand- {user_card}, dealer's hand {dealer_card}", end="\n\n")


# Main game loop
while True:
    # If yes then play, any key to exit
    if 'y' != input("Do you wanna play a game of black jack? Yes to play, any key to exit: ").lower() != "yes":
        break

    clear()

    # User's and Dealers cards
    user_show_card = []
    dealer_show_card = []
    dealer_hidden_card = []

    # Initial 2 cards distribution for both
    for i in range(2):
        user_show_card.append(deck_shuffle())
        dealer_show_card.append(deck_shuffle())

    # Hide dealer's all cards but first in new list
    dealer_hidden_card = dealer_show_card[:]

    for i in range(1, len(dealer_show_card)):
        dealer_hidden_card[i] = '_'

    # Calculate scores
    user_score = calculate(user_show_card)
    dealer_score = calculate(dealer_show_card)

    if user_score == 0 or dealer_score == 0:
        end_compare(user_score, dealer_score, user_show_card, dealer_show_card)
        continue

    # Print scores to user
    print(f"\nHere are your cards- {user_show_card}, your score- {user_score}  ||"
          f"  and here is dealer's cards {dealer_hidden_card}")

    # Second loop to prompt user to drew one more card or end the game
    while True:
        drew_option = input("You wanna conclude game or drew one card('Drew' to drew card, "
                            "any key to see who won): ").lower()

        # If user chooses to end the game and see result
        if drew_option != "drew":
            break

        # If not,
        # Drew one more card to user
        user_show_card.append(deck_shuffle())

        # Calculate users new scores
        user_score = calculate(user_show_card)

        # Show user cards and score
        print(f"\nHere are your cards- {user_show_card}, your score- {user_score}  ||"
              f"  and here is dealer's card {dealer_hidden_card}")

        # If user score is higher than or equals to 0, then there is a win or draw
        if user_score > 21:
            break

    # After user chooses and did not win, then it's computers turn to get new card until it's score is < 17
    print("\nNow it's dealers choice to choose cards..")

    while dealer_score < 18:
        dealer_show_card.append(deck_shuffle())
        dealer_hidden_card.append('_')
        dealer_score = calculate(dealer_show_card)

    print("Dealer has chosen it's cards..")

    # Compare last time to check end game
    end_compare(user_score, dealer_score, user_show_card, dealer_show_card)
