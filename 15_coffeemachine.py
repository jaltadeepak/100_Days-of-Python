# windows + period key to open emoji keyboard on windows

# TODO: Make changes so that when ingredients are insufficient, it prints all the insufficient items and not just the first one like it is doing right now

coffee_logo = "☕"

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

def checkIngredients(typeofCoffee):
    """returns the ingredient that is not enough or none if all are enough"""
    if resources["water"] >= MENU[typeofCoffee]["ingredients"]["water"] and resources["milk"] >= MENU[typeofCoffee]["ingredients"]["milk"] and resources["coffee"] >= MENU[typeofCoffee]["ingredients"]["coffee"]:
        return "none"
    elif resources["water"] < MENU[typeofCoffee]["ingredients"]["water"]:
        return "water"
    elif resources["milk"] < MENU[typeofCoffee]["ingredients"]["milk"]:
        return "milk"
    elif resources["coffee"] < MENU[typeofCoffee]["ingredients"]["coffee"]:
        return "coffee"


def takeMoney(typeofCoffee):
    """takes user money and calculates amount to return and returns True if money is enough and False if money put in is not enough"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    
    money_put_in = round(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01, 2)
    money_given_back = round(money_put_in - MENU [typeofCoffee]["cost"], 2)
    # print(money_given_back)
    if money_given_back >= 0:
        global resources
        resources["money"] += MENU[typeofCoffee]["cost"]
        print(f"Coffee Served{coffee_logo}. Change returned is ${money_given_back}.")
        return True
    else:
        print("Not enough money put in. Refunded.")
        return False

def makeCoffee(typeofCoffee):
    """makes changes in the resources dictionary after the coffee is made"""
    global resources
    resources["water"] -= MENU[typeofCoffee]["ingredients"]["water"]
    resources["milk"] -= MENU[typeofCoffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[typeofCoffee]["ingredients"]["coffee"]

def checkResources(typeofCoffee):
    """checks if Resources dictionary has enough ingredients and makes coffee(makeCoffee function) if it does"""
    item_not_enough = checkIngredients(typeofCoffee)
    if item_not_enough == "none":
        enough_money = takeMoney(typeofCoffee)
        if enough_money == True:
            makeCoffee(typeofCoffee)

    elif item_not_enough in ["water", "milk", "coffee"]:
        print(f"Machine does not have enough {item_not_enough}.")

def printReport():
    """prints the amount of resources left"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def useMachine():
    """runs the machine functionality"""
    command = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if command  == "off":
        return False
    elif command in ["espresso", "latte", "cappuccino"]:
        checkResources(command)
    elif command == "report":
        printReport()

    return True

machine_working = True
resources["money"] = 0
while machine_working == True:
    MENU["espresso"]["ingredients"]["milk"] = 0
    # print(MENU)
    machine_working  = useMachine()

print("\nMachine is turned off.")

