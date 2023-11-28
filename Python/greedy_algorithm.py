# Implementing Greedy Algorithm, using money change given. When making change, odds are you want to minimize the
# number of coins you�re dispensing for each customer, lest you run out. Fortunately, computer science has given
# cashiers everywhere ways to minimize numbers of coins due: greedy algorithms.

# Output is calculated on Quarters, dimes, nickels, and pennie. where 1 is a dollar that generates 4 coins(quarters).

def main():
    cents = get_change()

    quarters = count_quarters(cents)
    cents -= quarters * 0.25

    dimes = count_dimes(round(cents, 2))
    cents -= dimes * 0.10

    nickels = count_nickels(round(cents, 2))
    cents -= nickels * 0.05

    pennies = count_pennies(round(cents, 2))
    cents -= pennies * 0.01

    coins = quarters + dimes + nickels + pennies
    print(coins)


def get_change():
    """Prompt user for change until it is a number greater than 0"""
    while True:
        try:
            change = float(input("Change owed: "))
            if change > 0:
                break
        except ValueError:
            pass

    return change


def count_quarters(cents):
    if cents >= 0.25:
        return int(cents / 0.25)

    return 0


def count_dimes(cents):
    if cents >= 0.10:
        return int(cents / 0.10)

    return 0


def count_nickels(cents):
    if cents >= 0.05:
        return int(cents / 0.05)

    return 0


def count_pennies(cents):
    if cents >= 0.01:
        return int(cents / 0.01)

    return 0


if __name__ == "__main__":
    main()
