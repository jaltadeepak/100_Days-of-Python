import getpass
import os

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)

word = getpass.getpass("Enter the word: ")
print("\nThe word has been entered.\n")

word_length = len(word)

orig_word = list(word)

guessed_word = []

for i in range(word_length):
    guessed_word.append("_")

current_word = ""

for i in range(word_length):
    current_word += guessed_word[i]

print(f"The word to guess is {current_word}\n")
cont = input("Press ENTER to continue...")

hangman = 0

while not (orig_word == guessed_word):
    os.system('cls')

    print(logo)

    guess = input("Guess a letter: ")

    flag = 0 

    for i in range(word_length):
        if orig_word[i] == guess:
            guessed_word[i] = guess
            flag += 1
        else:
            continue

    if flag==0:
        hangman+=1
        print("\nIncorrect.\n")
    else:
        print("\nCorrect.\n")

    current_word = ""

    for i in range(word_length):
        current_word += guessed_word[i]

    print(f"The word to guess is {current_word}")

    print(stages[6-hangman])

    print(f"Lives Left: {6-hangman}\n")

    if hangman==6:
        print("Game Over, Bhago Yahan Se.")
        break

    cont = input("Press ENTER to continue...")

if orig_word == guessed_word:
    print("Game Won!!")