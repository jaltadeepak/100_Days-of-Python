APP_ID = "[your ID]"
APP_TOKEN = "[your token]"

GENDER = "male"
WEIGHT = 60.5
HEIGHT = 175.4
AGE = 21

import requests
import datetime as dt

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "[your sheety endpoint]"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_TOKEN,
    "x-remote-user-id": "0",
}

exercise_params = {
    "query": input("Tell me the exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)

sheety_headers = {
    "Authorization": "Bearer [your token]",
}

today = dt.datetime.now()

date = today.date()
time = today.time()
date_string = date.strftime(f"%d/%m/%Y")
time_string = time.strftime(f"%H:%M:%S")


for exercise in response.json()['exercises']:
    exercise_name = exercise['name'].title()
    duration = round(exercise['duration_min'])
    calories = round(exercise['nf_calories'])
    sheets_params = {
        "workout": {
            "date": date_string,
            "time": time_string,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories
        }
    }
    sheety_response = requests.post(url=SHEET_ENDPOINT, json=sheets_params, headers=sheety_headers)
    sheety_response.raise_for_status()