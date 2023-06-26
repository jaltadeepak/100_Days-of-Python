# bugs: 1. "card drawn" isn't visible on screen because of the cls statement in print_info, 2. Mutiple print of blackjack art when computer plays
# possible solution: 1. print the last card drawn inside the print_info function somehow

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards_art = [
    '''
    .------.  
    |A     |  
    |  ♠   |  
    |     A|  
    `------'
    ''',
    '''
    .------.  
    |2     |  
    |  ♠   |  
    |     2|  
    `------'
    ''',
    '''
    .------.  
    |3     |  
    |  ♠   |  
    |     3|  
    `------'
    ''',
    '''
    .------.  
    |4     |  
    |  ♠   |  
    |     4|  
    `------'
    ''',
    '''
    .------.  
    |5     |  
    |  ♠   |  
    |     5|  
    `------'
    ''',
    '''
    .------.  
    |6     |  
    |  ♠   |  
    |     6|  
    `------'
    ''',
    '''
    .------.  
    |7     |  
    |  ♠   |  
    |     7|  
    `------'
    ''',
    '''
    .------.  
    |8     |  
    |  ♠   |  
    |     8|  
    `------'
    ''',
    '''
    .------.  
    |9     |  
    |  ♠   |  
    |     9|  
    `------'
    ''',
    '''
    .------.  
    |10    |  
    |  ♠   |  
    |    10|  
    `------'
    ''',
    '''
    .------.  
    |J     |  
    |  ♠   |  
    |     J|  
    `------'
    ''',
    '''
    .------.  
    |Q     |  
    |  ♠   |  
    |     Q|  
    `------'
    ''',
    '''
    .------.  
    |K     |  
    |  ♠   |  
    |     K|  
    `------'
    ''',
]



import random
import os

card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')
    
def add_cards(cards_list):
    return sum(cards_list)

def has_an_ace(cards_list):
    acecheck = False
    if 11 in cards_list:
        acecheck = True
    return acecheck

def check_blackjack(cards_list):
    check_blackjackflag = False
    if 11 in cards_list and 10 in cards_list and len(cards_list) == 2:
        check_blackjackflag = True
    return check_blackjackflag

def print_cards(card_list_index):
    for art in card_list_index:
        print(cards_art[art], end="")

def print_info(user_cards_index, user_sum, computer_cards_index, computer_sum):
    os.system('cls')
    # clear_console()
    print(logo)
    print("Your Cards:")
    print_cards(user_cards_index)
    print(f"Your current score: {user_sum}")
    print("\nComputer's Cards:")
    print_cards(computer_cards_index)
    print(f"Computer's current score: {computer_sum}\n")


print(logo)
    
want_to_play = input("Does the user want to play a game of Blackjack? Type 'y' for yes and 'n' for no: ")

while want_to_play == "y":

    user_cards = []
    computer_cards = []
    user_sum = 0
    computer_sum = 0
    game_over = False
    user_cards_index = []
    computer_cards_index = []

    chosen_card = random.choice(card_list)
    user_cards_index.append(card_list.index(chosen_card))
    user_cards.append(chosen_card)

    chosen_card = random.choice(card_list)
    user_cards_index.append(card_list.index(chosen_card))
    user_cards.append(chosen_card)

    user_sum = add_cards(user_cards)

    if has_an_ace(user_cards) == True and user_sum>21:
        user_cards.remove(11)
        user_cards.append(1)
        user_sum-=10

    
    chosen_card = random.choice(card_list)
    computer_cards_index.append(card_list.index(chosen_card))
    computer_cards.append(chosen_card)

    computer_sum = computer_cards[0]

    print_info(user_cards_index, user_sum, computer_cards_index, computer_sum)

    draw_card = input("Do you wnat to draw another card? Type 'y' for yes and 'n' for no: ")

    while draw_card == "y" and game_over == False:
        chosen_card = random.choice(card_list)
        user_cards_index.append(card_list.index(chosen_card))
        user_cards.append(chosen_card)

        user_sum = add_cards(user_cards)

        print(f"You drew: {user_cards[-1]}")
        print_info(user_cards_index, user_sum, computer_cards_index, computer_sum)

        if check_blackjack(user_cards) == True:
            print("BLACKJACK!! You Win!!")
            game_over = True
        elif user_sum > 21:
            if has_an_ace(user_cards) == False:
                print("You lose.")
                game_over = True
            elif has_an_ace(user_cards) == True:
                user_cards.remove(11)
                user_cards.append(1)
                user_sum-=10
                print_info(user_cards_index, user_sum, computer_cards_index, computer_sum)

        if game_over == False:
            draw_card = input("\nDo you want to draw another card? Type 'y' for yes and 'n' for no: ")

    while computer_sum<17 and game_over == False:
        chosen_card = random.choice(card_list)
        computer_cards_index.append(card_list.index(chosen_card))
        computer_cards.append(chosen_card)
        print(f"Computer drew: {cards_art[computer_cards_index[-1]]}")
        computer_sum  = add_cards(computer_cards)
        
        if check_blackjack(computer_cards) == True:
            print("BLACKJACK!! Computer Win!!")
            game_over = True
        elif computer_sum > 21:
            if has_an_ace(computer_cards) == False:
                print_info(user_cards_index, user_sum, computer_cards_index, computer_sum)
                print("You win.")
                game_over = True
            elif has_an_ace(computer_cards) == True:
                computer_cards.remove(11)
                computer_cards.append(1)
                computer_sum-=10

    if computer_sum<=21 and user_sum<=21:
        print_info(user_cards_index, user_sum, computer_cards_index, computer_sum)
        if computer_sum < user_sum:
            print("You win.")
        elif computer_sum > user_sum:
            print("Computer wins.")
        elif computer_sum == user_sum:
            print("You draw.")

    want_to_play = input("\nDo you want to play a game of Blackjack? Type 'y' for yes and 'n' for no: ")
    os.system('cls')
    print(logo)

print("\n\nThank you for playing.")
