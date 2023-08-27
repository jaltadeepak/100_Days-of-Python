from  twilio.rest import Client
import requests
import smtplib

TWILIO_SID = "[SID]"
TWILIO_TOKEN = "[TOKEN]"
TWILIO_FROM = "[TWILIO_NUMBER]"
TWILIO_TO = "[VERIFIED_NUMBER]"
MY_EMAIL = "deepaksingh131120@gmail.com"
MY_PASSWORD = "[password]"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.client = Client(username=TWILIO_SID, password=TWILIO_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=TWILIO_TO,
        )
        print(message.sid)

    def send_emails(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="deepaksingh131102@gmail.com",
                msg=f"Subject: Flight Club!\n\n{message}"
            )