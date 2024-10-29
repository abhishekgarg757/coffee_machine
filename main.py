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

wallet = 0

# TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# TODO 2.Turn off the Coffee Machine by entering “ off ” to the prompt.
# TODO 3. Print report.
# TODO 4.Check resources sufficient?

def check_resources(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coins():
    print("Please insert coins")
    total = int(input("how many quaters? :")) *0.25
    total += int(input("how many dimes ?:"))*0.1
    total += int(input("how many nickels :"))*0.05
    total += int(input("how many pennies :"))*0.01
    return total

machine_on = True
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        machine_on = False

    elif user_input == "report":
        print(f"Water:{resources["water"]} ml")
        print(f"Milk:{resources["milk"]} ml")
        print(f"Coffee:{resources["coffee"]} gm")
        print(f"Money:${wallet} ")
    else:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            payment = coins()
            if payment < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round((payment-drink["cost"]),2)
                wallet = wallet+drink["cost"]
                print(f"here is your change : {change}")
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                print(f"enjoy you {user_input}")




