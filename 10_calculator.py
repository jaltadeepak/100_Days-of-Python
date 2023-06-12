# stringname.title() func. changes whatever the string into a string where every word starts with a capital letter and the rest of the words are small
# ex: dEEPAK => Deepak, dEePaK => Deepak, DEEPAK SINGH => Deepak Singh

# """You can write the docstring(documentation string) here inside three quotes, you can use this to write the documentation of a function"""

import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

oper_dict = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

flag = True

while flag == True:
    print(logo)
    num1 = float(input("What's the first number?: "))

    for key in oper_dict:
        print(key)

    operation_symbol = input("Pick and operation from the lines above: ")
    num2 = float(input("What's the second number?: "))

    calculation_function = oper_dict[operation_symbol]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    while input("Press 'y' to use the answer for another operation, Press 'n' for a new operation... ") == "y":
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the new number?: "))

        calculation_function = oper_dict[operation_symbol]
        new_answer = calculation_function(first_answer, num3)

        print(f"{first_answer} {operation_symbol} {num3} = {new_answer}")

        first_answer = new_answer
    
    os.system('cls')
