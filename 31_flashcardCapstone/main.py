from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    data = pandas.read_csv(r"C:\Code\100 Days of Python - Angela Yu\31_flashcardCapstone\data\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"C:\Code\100 Days of Python - Angela Yu\31_flashcardCapstone\data\french_words.csv")
finally:    
    dict = data.to_dict(orient="records")

current_card = {}

def flip_card():
    global current_card
    english_word = current_card["English"]
    canvas.itemconfig(card_image, image = card_back_image)
    canvas.itemconfig(card_title, text = "English", fill="white")
    canvas.itemconfig(card_word, text = english_word, fill="white")

def gen_frenchword():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(dict)
    french_word = current_card['French']
    canvas.itemconfig(card_image, image = card_front_image)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text = french_word, fill="black")
    flip_timer = window.after(3000, flip_card)

def remove_card():
    global current_card, dict
    dict.remove(current_card)
    df = pandas.DataFrame(dict)
    df.to_csv(r'C:\Code\100 Days of Python - Angela Yu\31_flashcardCapstone\data\words_to_learn.csv', index=False)
    gen_frenchword()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file=r"C:\Code\100 Days of Python - Angela Yu\31_flashcardCapstone\images\card_front.png")
card_back_image = PhotoImage(file=r"C:\Code\100 Days of Python - Angela Yu\31_flashcardCapstone\images\card_back.png")
card_image = canvas.create_image(400, 263)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan=2)

wrong_image = PhotoImage(file=r"C:\Code\100 Days of Python - Angela Yu\31_flashcardCapstone\images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=gen_frenchword)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file=r"C:\Code\100 Days of Python - Angela Yu\31_flashcardCapstone\images\right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

gen_frenchword()

window.mainloop()

