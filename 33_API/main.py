# response code
# 404: doesn't exist
# 200: success
# 1XX: Hold on
# 2XX: Here you go
# 3XX: Go away, no permission
# 4XX: You screwed up, doesn't exist
# 5XX: server screwed up

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 28.535517
MY_LONG = 77.391029

def position_check():
    response = requests.get("http://api.open-notify.org/iss-now.json")

    # raise an exception with the specific response code
    response.raise_for_status()

    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if MY_LONG - 5 <= longitude <= MY_LONG + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        return True
    return False


def night_check():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    if hour_now > sunrise and hour_now < sunset:
        return True
    return False


is_close = position_check()
is_dark = night_check()

my_email = "deepaksingh131120@gmail.com"
my_password = "[put your own password]"

while True:
    time.sleep(60)
    if is_close and is_dark:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="deepaksingh131102@gmail.com",
                msg="Subject: Look Up\n\nThe space station is in your sky.",
            )
