from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Text: multiple lines of entry
text = Text(height=5, width=30)
#puts curson in text box
text.focus()
text.insert(END, "Text to begin")
# Gets current value in textbox at line 1, character 0. That is why 1.0 is written
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_ = 5, to = 10, width = 5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)
scale = Scale(from_ = 0, to = 100, command = scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    #prints 1 if on, 0 if off
    print(checked_state.get())
checked_state = IntVar() # IntVar is a class
checkbutton = Checkbutton(text = "Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
# variable to hold the value of the current selected radiobutton checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text = "Option1", value = 1, variable = radio_state, command = radio_used)
radiobutton2 = Radiobutton(text = "Option2", value = 2, variable = radio_state, command = radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()