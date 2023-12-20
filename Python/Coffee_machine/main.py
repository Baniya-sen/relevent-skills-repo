from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instances of all imported class
drink_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def main():
    # Main coffee-machine loop
    while True:
        # Take user order until 'off' is input
        order = input(f"\nNamaste. What will you have today? [{drink_menu.get_items()}]: ").lower()

        if order == "off":
            break
        elif order == "report":
            coffee_maker.report()
            money_machine.report()

        # If user input is valid, and resources are sufficient, and coins are enough, then make coffee
        else:
            item = drink_menu.find_drink(order)
            if item and coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)


if __name__ == "__main__":
    main()
