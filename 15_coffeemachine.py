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
    if resources["water"] >= MENU[typeofCoffee]["ingredients"]["water"] and resources["milk"] >= MENU[typeofCoffee]["ingredients"]["milk"] and resources["coffee"] >= MENU[typeofCoffee]["ingredients"]["coffee"]:
        return "none"
    elif resources["water"] < MENU[typeofCoffee]["ingredients"]["water"]:
        return "water"
    elif resources["milk"] < MENU[typeofCoffee]["ingredients"]["milk"]:
        return "milk"
    elif resources["coffee"] < MENU[typeofCoffee]["ingredients"]["coffee"]:
        return "coffee"


def takeMoney(typeofCoffee):
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
            print(f"Coffee Served. Change returned is ${money_given_back}.")
    else:
        print("Not enough money put in. Refunded.")
    return money_given_back

def makeCoffee(typeofCoffee):
    global resources
    resources["water"] -= MENU[typeofCoffee]["ingredients"]["water"]
    resources["milk"] -= MENU[typeofCoffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[typeofCoffee]["ingredients"]["coffee"]

def checkResources(typeofCoffee):
    item_not_enough = checkIngredients(typeofCoffee)
    if item_not_enough == "none":
        takeMoney(typeofCoffee)
        makeCoffee(typeofCoffee)

    elif item_not_enough in ["water", "milk", "coffee"]:
        print(f"Machine does not have enough {item_not_enough}.")

def printReport():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def useMachine():
    command = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if command  == "off":
        return False
    elif command in ["espresso", "latte", "cappucino"]:
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

