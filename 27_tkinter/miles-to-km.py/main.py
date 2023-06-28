from tkinter import *

window = Tk()
window.title("miles to km converter")
window.minsize(width = 200, height = 50)
window.config(padx=20, pady=20)

def calculate():
    input_miles = float(input.get())
    output_miles = input_miles * 1.609
    output.config(text = f"{round(output_miles, 2)}")

input = Entry(width = 10)
input.grid(column=1, row=0)

mile_label = Label(text = "Miles")
mile_label.grid(column=2, row=0)

is_equal_to_label = Label(text = "is equal to")
is_equal_to_label.grid(column = 0, row = 1)

output = Label(text = "0")
output.grid(column = 1, row = 1)

km_label = Label(text = "Km")
km_label.grid(column=2, row = 1)

calculate_button = Button(text = "Calculate", command = calculate)
calculate_button.grid(column = 1, row = 2)

window.mainloop()