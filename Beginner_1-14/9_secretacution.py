# prog_dict = {key1: value1, key2: value2, }

# prog_dict[key1] will give the value at the given key, i.e, value1

# prog_dict["Loop"] = "new value of loop" will add an item with key = "Loop" into the dictionary, can also be used to edit an existing key item if it already exists.

# empty_dict = {} can be used to create an empty dictionary as well as to wipe an exisiting dictionary

# for key in prog_dict:
#   print(key)
#   print(prog_dict[key])

# Nesting Dictionary in a Dictionary=>
# travel_log = { 
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}, 
#     "Germany": {"cities_visited": ["Munich", "Hamburg", "Stuttgart"], "total_visits": 5}, 
# }

# Nested Dictionary in a List=>
# travel_log = [
#     {
#         "country": "France", 
#         "cities_visited": ["France", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Munich", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# ]
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bid_dict = {}
to_cont = True

def enter_bid():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_dict[name] = bid

def calc_winner(bid_dict):
    max = 0
    for name in bid_dict:
        if bid_dict[name] > max:
            max = bid_dict[name]
            nameofwinner = name
        else:
            continue
    print(f"The winner is {nameofwinner} with the bid of ${bid_dict[nameofwinner]}")

print(logo)

while to_cont == True:
    enter_bid()
    cont = input("Are there any more bidders? Type yes or no... ")
    if cont == "no":
        to_cont = False
    else:
        os.system('cls')

calc_winner(bid_dict)




        

