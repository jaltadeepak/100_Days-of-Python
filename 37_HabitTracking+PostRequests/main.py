import requests
from datetime import datetime

USERNAME = "jaltadeepak"
TOKEN = "[your token here]"
GRAPH_ID = "graph1"

pixela_endpoint = r"https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# commented out because account already created
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# commented out because graph already created
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_config = {
    "date": today.strftime(r"%Y%m%d"),
    "quantity": input("How many kms did you run today? "),
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

date_to_update = "20230820"

pixel_values = {
    "quantity": "1.4"
}

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"

# response = requests.put(url=pixel_update_endpoint, json=pixel_values, headers=headers)
# print(response.text)

# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)