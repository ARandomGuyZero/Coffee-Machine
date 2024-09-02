"""
Coffee Machine

Author: Alan
Date: August 29th 2024

This script simulates a coffee machine.
The user selects the coffee drink, pays with coins and the machine will update the list of resources for the next time
"""

# List of coffee to make.
# Each list has a list of ingredients and the cost
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

# Stores the profit of the coffee machine
profit = 0

# List of available resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def has_ingredients(coffee_ingredients):
    """
    Checks if the coffee machine has enough ingredients
    :param coffee_ingredients: List of ingredients to make the coffee
    :return: Returns True if the coffee machine has enough ingredients or False if not.
    """

    # Loops per ingredient for the coffee's ingredients
    for ingredient in coffee_ingredients:
        if resources[ingredient] < coffee_ingredients[ingredient]:
            print(f"Sorry, there's not enough {ingredient}")
            return False

    return True

def process_coins():
    """
    Inputs how much coins the user will insert to the machine
    :return: The total of coins
    """
    print("Please insert coins.")
    quarter = int(input("how many quarters?:"))
    dime = int(input("how many dimes?:"))
    nickle = int(input("how many nickles?:"))
    pennie = int(input("how many pennies?:"))

    return (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (pennie * 0.01)

def make_coffee(coffee_ingredients, coffee):
    """
    Makes coffee for the user!
    :param coffee_ingredients: List of ingredients to make the coffee
    :param coffee: Stores the name of the coffee
    :return: Returns a cup of coffee
    """
    for resource in resources:
        resources[resource] -= coffee_ingredients[resource]

    return f"Here is your {coffee} ☕️. Enjoy!"

def is_transaction_successful(coffee):
    """
    Checks if the payment was completed
    :param coffee: Stores the name of the coffee
    :return: Returns True if the payment was completed or False if not
    """
    global profit
    coffee_cost = MENU[coffee]["cost"]
    total_coins = process_coins()

    if total_coins >= coffee_cost:
        profit += coffee_cost
        change = total_coins - coffee_cost
        print(f"Here's your change: ${change}")
        return True
    else:
        print("You don't have enough cash!")
        return False

def report_resources():
    """
    Prints the amount of resources
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def coffee_machine():
    """
    Has the full logic of the code
    """
    is_on = True

    # Simple loop to continue producing coffee
    while is_on:
        prompt = input("What would you like? (espresso/latte/cappuccino):\n")
        # Checks if the prompt is in the menu
        if prompt in MENU:
            coffee_ingredients = MENU[prompt]["ingredients"]
            if has_ingredients(coffee_ingredients):
                if is_transaction_successful(prompt):
                    make_coffee(coffee_ingredients, prompt)
        # If report is prompted, it prints the report of resources
        elif prompt == "report":
            report_resources()
        # If off is prompted, it shuts down the coffee machine
        elif prompt == "off":
            is_on = False
        # Default response
        else:
            print("We don't have that option!")

    print("Shutting down... Goodbye!")

coffee_machine()
