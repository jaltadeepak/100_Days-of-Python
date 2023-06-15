# python does NOT have BLOCK SCOPE like c and c++, i.e., for/if/identations etc do not have their separate local scope, only functions do

# enemies = 1
# def increase_enemies():
#     global enemies
#     enemies += 1
# you have to declare the global entity with the global keyword inside functions to MODIFY(not to access, that is possible without the keyword) them locally
# although it is advised to avoid modifying global scopes locally

# convention is to use fully uppercase words as variable, etc names for values that won't change, i.e, are constants thourhgout the program
# URL = "https://www.abc.com"
# PI = 3.14159

import random
import os

# link for ASCII art generator: http://patorjk.com/software/taag/#p=display&f=Standard&t=Type%20Something%20
logo = """                                                                             
 _____                      _____ _          _____ _____ _____ _____ _____ _____ 
|   __|_ _ ___ ___ ___     |_   _| |_ ___   |   | |  |  |     | __  |   __| __  |
|  |  | | | -_|_ -|_ -|      | | |   | -_|  | | | |  |  | | | | __ -|   __|    -|
|_____|___|___|___|___|      |_| |_|_|___|  |_|___|_____|_|_|_|_____|_____|__|__| (by jaltadeepak)
                                                                                  
"""

# print(logo)

EASY_TURNS = 10
DIFF_TURNS = 5

def welcome():
    os.system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def setDifficulty():
    difficulty = input("Select the difficulty level => Type 'easy' or 'difficult': ")

    if difficulty == "easy":
        return EASY_TURNS
    else:
        return DIFF_TURNS
    
def checkGuess(guess, number, numguess):
    if guess == number:
            print(f"\nCorrect guess. The number was {guess}, YOU WIN!!")
            return 0
    else:
        if guess > number:
            print("\t=>Too high.")
        elif guess < number:
            print("\t=>Too low.")
        return numguess-1

def playgame():
    
    welcome()

    noofguesses = setDifficulty()

    thenumber = random.randint(1, 100)

    while noofguesses > 0:
        print(f"\nThe number of guesses left: {noofguesses}")
        userguess = int(input("Enter your guess: "))
        
        noofguesses = checkGuess(userguess, thenumber, noofguesses)

    if userguess != thenumber:
        print(f"\nYou have zero chances left, YOU LOSE. The correct guess was {thenumber}.")

    

to_continue = input("Do you want to play the Number Guessing Game? Press 'y' for yes and 'n' for no... ")

while to_continue == "y":
    playgame()
    to_continue = input("\nDo you want to play the Number Guessing Game? Press 'y' for yes and 'n' for no... ")

print("\nThanks for playing.\n")
