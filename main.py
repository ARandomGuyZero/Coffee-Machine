"""
Coffee Machine

Author: Alan
Date: August 3rd 2024

This script simulates a coffee machine.
The user selects the coffee drink, pays with coins and the machine will update the list of resources for the next time
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

# Loop for coffee machine that works as long is_on equals True
while is_on:
    menu_items = menu.get_items()
    prompt = input(f"What would you like? {menu_items}:\n")

    # If prompted secret option off, it shuts down the coffee machine
    if prompt == "off":
        is_on = False
    # If prompted secret option report, it reports resources and current profit
    elif prompt == "report":
        coffee_maker.report()
        money_machine.report()
    # Else, will try to make the coffee as long as it has enough resources and the payment can be done
    else:
        try:
            drink = menu.find_drink(prompt)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        except AttributeError:
            pass
