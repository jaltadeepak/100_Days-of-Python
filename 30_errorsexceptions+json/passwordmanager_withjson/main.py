# json.dump(): write
# json.load(): read
# json.update(): update

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

def gen_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_lettters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_lettters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)


def add_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="You can't leave any fields empty.")
    else:
        try:
            with open(r"C:\Code\100 Days of Python - Angela Yu\30_errorsexceptions+json\passwordmanager_withjson\data.json", "r") as f:
                # reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open(r"C:\Code\100 Days of Python - Angela Yu\30_errorsexceptions+json\passwordmanager_withjson\data.json", "w") as f:
                # saving new data
                json.dump(new_data, f, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open(r"C:\Code\100 Days of Python - Angela Yu\30_errorsexceptions+json\passwordmanager_withjson\data.json", "w") as f:
                # saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def search_password():
    website = website_input.get()
    try:
        with open(r"C:\Code\100 Days of Python - Angela Yu\30_errorsexceptions+json\passwordmanager_withjson\data.json") as f:
            data = json.load(f)
    except:
        messagebox.showerror(title="error", message="File not found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="error", message="Entry not found.")
    

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=r"C:\Code\100 Days of Python - Angela Yu\30_errorsexceptions+json\passwordmanager_withjson\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text="Website:")
website_label.grid(row = 1, column = 0)

website_input = Entry(width=32)
website_input.grid(row = 1, column = 1)
website_input.focus()

search_button = Button(text="Search", command=search_password, width=14)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row = 2, column = 0)

email_input = Entry(width=50)
email_input.grid(row = 2, column = 1, columnspan = 2)
email_input.insert(0, "deepaksingh131102@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row = 3, column = 0)

password_input = Entry(width=32)
password_input.grid(row = 3, column = 1)

gen_pass_button = Button(text="Generate Password", command = gen_pass)
gen_pass_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", command = add_data, width = 43)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()