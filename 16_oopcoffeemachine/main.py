# Classes:
# name is usually with first letter of every word capitalized to differentiate from functions etc (Pascal Case)
# objectofclass = ClassName()
# print(objectofclass) => prints <module.ClassName object at 0x23423423>

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkCyan")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# # print(table)
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)
# table.align = "l"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while (is_on == True):
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        menuitem = menu.find_drink(choice)
        if menuitem:
            if coffee_maker.is_resource_sufficient(menuitem) == True:
                if money_machine.make_payment(menuitem.cost) == True:
                    coffee_maker.make_coffee(menuitem)

    print("")
        