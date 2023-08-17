import datetime as dt
import smtplib
import pandas
from random import choice
import os

birthday_entry = None

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
curr_month = now.month
curr_day = now.day

data = pandas.read_csv(r"C:\Code\100 Days of Python - Angela Yu\32_email+dates\Birthday Wisher\birthdays.csv")
dict = data.to_dict(orient = 'records')

for entry in dict:
    if entry['month'] == curr_month and entry['day'] == curr_day:
        birthday_entry = entry


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if birthday_entry != None:
    path_to_random_letter = choice(os.listdir(r"C:\Code\100 Days of Python - Angela Yu\32_email+dates\Birthday Wisher\letter_templates"))
    full_path = rf"C:\Code\100 Days of Python - Angela Yu\32_email+dates\Birthday Wisher\letter_templates\{path_to_random_letter}"

    with open(full_path) as letter:
        letter_content = letter.read()
        birthday_letter_content = letter_content.replace("[NAME]", f"{birthday_entry['name']}")

# 4. Send the letter generated in step 3 to that person's email address.
    my_email = "deepaksingh131120@gmail.com"
    my_password = "[put your password here]"
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{birthday_entry['email']}",
                msg=f"Subject: Happy Birthday!\n\n{birthday_letter_content}"
            )




