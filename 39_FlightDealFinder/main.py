#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
    
flight_search = FlightSearch()

data_manager = DataManager()

notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_CODE = "LON"

for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_destination_code(row['city'])
print(f"Sheet Data:\n{sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_code()

tomorrow = (datetime.now() + timedelta(1)).strftime("%d/%m/%Y")
six_month_from_today = (datetime.now() + timedelta(180)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination['lowestPrice']:
        notification_manager.send_sms(
            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )


