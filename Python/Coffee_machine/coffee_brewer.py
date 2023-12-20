# Initial money, machine started with
money = 0.0


def main():
    # Main coffee prompt loop
    while True:
        print("What would you like? [", end="")
        for menu_item in MENU:  # Prints coffee menu to user
            print(menu_item + ',', end="")
        print("]: ", end="")

        user_prompt = input().lower()
        if user_prompt == 'off':
            break
        elif user_prompt in MENU.keys():
            # Check resources before taking coins from user
            if not check_resource(user_prompt):
                break
            # If resources are enough for menu item then get coins
            check_coins(user_prompt)
        elif user_prompt == 'report':
            # Reports resources left in machine
            (lambda: print('\n'.join([f"[{m_item}: {price}]" for m_item, price in resources.items()])))()
            print(f"[money: ${money}]", end='\n\n')
        else:
            print("Wrong choice.. Try again!", end='\n\n')


def check_resource(menu_choice):
    """Returns True if resources required for a order are sufficient, else False"""
    for item in MENU[menu_choice]["ingredients"]:
        if MENU[menu_choice]["ingredients"][item] > resources[item]:
            print(f"Not enough {item} left in machine, you peasant!")
            return False
    return True


def check_coins(menu_choice):
    """Input coins from user and passes the total to transaction()"""
    print("Enter cents you peasant: ")
    while True:
        try:
            quarters = 0.25 * int(input("Quarters: "))
            dimes = 0.10 * int(input("Dimes: "))
            nickels = 0.05 * int(input("Nickels: "))
            pennies = 0.01 * int(input("Pennies: "))
            break
        except ValueError:
            pass

    if not transactions(quarters + dimes + nickels + pennies, menu_choice):
        print("Transaction canceled!", end='\n\n')


def transactions(amount, choice):
    """Calculates change, if any, reduce ingredients count from resources, adds money to global variable"""
    cost = MENU[choice]["cost"]
    if amount < cost:
        print("Provide sufficient funds! You truly are peasant. Money refunded :(")
        return False
    elif amount > cost:
        change = round(amount - cost, 2)
        print(f"\nHere is your change, sir! ${change:.2f}")

    # If ingredients used by order in resources, then reduce them by order ingredients count
    for key in MENU[choice]["ingredients"]:
        resources[key] -= MENU[choice]["ingredients"][key]
    global money
    money += cost

    print("And.. Here is your coffee..🫖, Enjoy!", end='\n\n')
    return True


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

main()
