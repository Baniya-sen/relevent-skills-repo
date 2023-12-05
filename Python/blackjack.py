import os
import random

# Constants
CARD_VALUES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def deck_shuffle():
    """Return a random card value"""
    card = random.choice(CARD_VALUES)
    if card == 'Ace':
        return 11
    elif card in ['Jack', 'King', 'Queen']:
        return 10
    else:
        return int(card)


def calculate(card):
    """Calculates and checks cards"""
    total = sum(card)

    # If player deck has Ace and 10, ultimate win, 0 means BlackJack
    if total == 21 and len(card) == 2:
        return 0
    # If player has Ace and score is > 21, then ace can be equals to 1
    elif 11 in card and total > 21:
        card.remove(11)
        card.append(1)
        total = sum(card)

    return total


def end_compare(user_scores, dealer_scores, user_card, dealer_card):
    """Compares players and dealers card to conclude"""

    if user_scores == dealer_scores:
        print("\nIt's a Draw!")
    elif user_scores == 0 or 21 < dealer_score > user_scores:
        print("\nYOU WON.. BlackJack!")
    elif dealer_scores == 0 or user_scores > 21:
        print("\nYou Lose! NoJack.")
    else:
        print("You Lose!")

    print(f"Player's hand- {user_card}, dealer's hand {dealer_card}", end="\n\n")


# Main game loop
while True:
    # If yes then play, any key to exit
    if 'y' != input("Do you wanna play a game of black jack? Yes to play, any key to exit: ").lower() != "yes":
        break
    clear()

    # User's and Dealers Initial 2 cards distribution, and dealers hidden cards
    user_show_card = [deck_shuffle(), deck_shuffle()]
    dealer_show_card = [deck_shuffle(), deck_shuffle()]
    dealer_hidden_card = [dealer_show_card[0]] + ['_' for _ in dealer_show_card[1:]]

    # Calculate scores, and check Blackjack
    user_score = calculate(user_show_card)
    dealer_score = calculate(dealer_show_card)
    if user_score == 0 or dealer_score == 0:
        end_compare(user_score, dealer_score, user_show_card, dealer_show_card)
        continue

    # If nobody got blackjack, print scores to user
    print(f"\nCards player has- {user_show_card} | player score- {user_score}")
    print(f"-Dealer's cards {dealer_hidden_card}")

    # Second loop to prompt user to drew one more card or end the game
    while True:
        drew_option = input('What\'s next ["Drew" to get another card, "stop" to stop]: ').lower()
        if drew_option == "stop":
            break
        elif drew_option != "drew":
            print("Wrong choice... Try again!")
            continue

        # If not stop, Drew one more card to user
        user_show_card.append(deck_shuffle())
        user_score = calculate(user_show_card)
        print(f"Cards player has- {user_show_card}, player score- {user_score}")
        print(f"-Dealer's cards {dealer_hidden_card}")

        # If user score is higher than 21, end the drew
        if user_score > 21:
            break

    # After user chooses its computers turn to get new card
    print("\nNow it's dealers turn to get cards..")
    while dealer_score < 17:
        dealer_show_card.append(deck_shuffle())
        dealer_score = calculate(dealer_show_card)

    # Compare last time to check, end game
    end_compare(user_score, dealer_score, user_show_card, dealer_show_card)
