# environment variable: os.environ.get("NAMEOFVAR")
# setup: export NAMEOFVAR=valueofvar
# => so that anyone on the internet cannot use our api keys/tokens, etc

import requests
from twilio.rest import Client

api_key = "[your_owm_api_key]"
account_sid = "AC55a62df58eef9ea262650a471556747a"
auth_token = "[your_twilio_token]"

MY_LAT = 21.083250
MY_LONG = 80.001099

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(
    "https://api.openweathermap.org/data/2.8/onecall", params=parameters
)
response.raise_for_status()
weather_data = response.json()
next_12_hours = weather_data["hourly"][:12]
# print(next_12_hours)

next_12_hours_codes = [hour["weather"][0]["id"] for hour in next_12_hours]

will_rain = False

for code in next_12_hours_codes:
    if code < 800:
        will_rain = True

if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remeber to bring an umbrella.",
        from_="+17622475889",
        to="+919166950838",
    )
    print(message.status)
