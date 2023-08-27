from  twilio.rest import Client

TWILIO_SID = "[SID]"
TWILIO_TOKEN = "[TOKEN]"
TWILIO_FROM = "[TWILIO_NUMBER]"
TWILIO_TO = "[VERIFIED_NUMBER]"

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