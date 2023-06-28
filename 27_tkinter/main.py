# Argument with default values:
# def my_function(a=1, b=2, c=3):
#     func code
# ARGUMENTS which have default values are optional to be included in the function call, arguments that don't have values must have a reqiured argument passed during the function call

# takes up the entire height and width of the window =>
# my_label.pack(expand=True)

# pack => just stacks elements side by side, default is up to down
# place => places widgets at the exact position specified
# my_label.place(x=0, y=0)
# grid => divides program into grids and columns
# my_label.place(column=0, row=0)
# GRID AND PACK are incompitable with each other

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx = 30, pady= 20)

#Label
my_label = Label(text="I am a Label", font = ("Arial", 20, "bold"))
my_label.pack() 

# my_label["text"] = "new text" is same as =>
my_label.config(text = "new text")

def button_clicked():
    
    my_label.config(text = text_entered)

# Button
button = Button(text = "Click Me", command= button_clicked)
button.pack()

# Entry
input = Entry(width = 50)
input.pack()
text_entered = input.get()

window.mainloop()