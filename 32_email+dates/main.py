# pythonanywhere free tier

import smtplib
import datetime as dt
import random

my_email = "deepaksingh131120@gmail.com"
my_password = "[put your own password]"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="deepaksingh131102@gmail.com",
#         msg="Subject: Mail with Subject\n\nTwo newlines ensure this is the body of the email.",
#     )

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# datetime has default values of 00:00:00 for hours, minutes and seconds
# date_of_birth = dt.datetime(year=2002, month=11, day=13)


day_of_week = dt.datetime.now().weekday()
if day_of_week == 3:
    with open(file=r"C:\Code\100 Days of Python - Angela Yu\32_email+dates\quotes.txt") as file:
        data = file.read()
        quotes_list = data.split("\n")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="deepaksingh131102@gmail.com",
            msg=f"Subject: Be Positive!\n\n{random.choice(quotes_list)}"
        )

