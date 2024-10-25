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

# TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
user_input = input("What would you like? (espresso/latte/cappuccino): ")

def func1():
    """it is defining off and report"""
    if user_input == "off":
        return False
    elif user_input == "report":
        print(resources)
    return user_input

def func2():
    if user_input == "latte" or user_input == "cappuccino":
        if MENU[user_input]["ingredients"]["water"] <= resources["water"]  and MENU[user_input]["ingredients"]["milk"] <= resources["milk"]and MENU[user_input]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            return False
            #print(f"{MENU[x]["ingredients"]["water"]},{MENU[x]["ingredients"]["milk"]},{MENU[x]["ingredients"]["coffee"]}")
    elif MENU[user_input]["ingredients"]["water"] <= resources["water"] and MENU[user_input]["ingredients"]["coffee"] <= resources["coffee"]:
        return True
    else:
        print("no")

func2()




# TODO 2.Turn off the Coffee Machine by entering “ off ” to the prompt.


# TODO 3. Print report.

# TODO 4.Check resources sufficient?