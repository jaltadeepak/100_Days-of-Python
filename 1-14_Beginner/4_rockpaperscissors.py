# import random
# rand_number = random.randint(a,b) ...where a and b are included
# rand_number2 = random.random ...gen a floating point number between 0 and 1, not including 1 

# list1 = [a, b, c]
# list1[-1] would access c, i.e., from the back of the list
# .append() function to add an item to list
# .extend() to add multiple items, i.e., a list to a list

# choice() function returns random element from a list, string, tuple, etc

# txt.split() will split a string called txt into a list divided by whitespaces(default)
# txt.split(", ") would split it on th basis of a substring that matches ", "

# len(myList) calculates number of elements in list

# nested lists are lists containing multiple lists

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = [rock, paper, scissors]

import random

comp_num = random.randint(0,2)


user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if (user_num<0 or user_num>2):
    print("Choice out of bounds")
else:
    print(choices[user_num])

    print("Computer chose:")
    print(choices[comp_num])


    if (user_num>comp_num and not(user_num == 2 and comp_num==0)):
        print("You win")
    elif (comp_num>user_num and not(comp_num == 2 and user_num==0)):
        print("You lose")
    elif (user_num == 0 and comp_num==2):
        print("You win")
    elif (comp_num == 0 and user_num==2):
        print("You lose")
    elif (comp_num==user_num):
        print("Draw")