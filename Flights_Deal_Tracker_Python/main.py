# This code takes destination info from users Google sheet and searches the cheapest flight in a given time range,
# under given Budget for each destination, for all destinations specified in Google sheet.

import datetime

# File classes imports
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

# Constants, change fly_from city as preferred
ORIGIN_CITY_IATA = "DEL"
ORIGIN_CITY_CURRENCY = "INR"


def format_datetime(date_time):
    """Formats date and time string to datetime object"""
    return datetime.datetime.strptime(
        date_time,
        "%Y-%m-%dT%H:%M:%S.%fZ"
    ).strftime("%A, %B %d, %Y - %I:%M%p")


# Class instances
flight_search = FlightSearch()
notification_manager = NotificationManager()
data_manager = DataManager()

# Data verifications
print("Few checksums:")
data_manager.verify_iata_codes()

# Users emails and flight data from Google sheet
users_emails = data_manager.get_users_emails()
sheet_data = data_manager.get_location_data()

# Flights date range from tomorrow to 6 months
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_moths_after = tomorrow + datetime.timedelta(days=6 * 30)

# For every destination IATA code, search flight with specified date range
for destination in sheet_data:
    flight_search_data = flight_search.get_flight_data(
        fly_from=ORIGIN_CITY_IATA,
        fly_to=destination["iataCode"],
        date_from=tomorrow.strftime("%d/%m/%Y"),
        date_to=six_moths_after.strftime("%d/%m/%Y"),
        curr=ORIGIN_CITY_CURRENCY,
        cheap_or_not=True,
    )

    # Parse flight search data and budget for that flight, to get a dict of flight info
    flight_data_instance = FlightData(flight_search_data, destination["lowestPrice"])
    filtered_flights = flight_data_instance.filter_flight()

    # If there is no flight, or budget is low for flight, dict will have information
    try:
        print(filtered_flights["Information"], end="\n\n")

    # Otherwise dict will have flight information
    except KeyError:
        print("Done!")

        # Format date and time of flight
        departure_datetime = format_datetime(filtered_flights["departureDateTime"])
        destination_datetime = format_datetime(filtered_flights["destinationDateTime"])

        # Sends notification sms to user if flight found
        notification_manager.send_sms(
            f"Low price on flights alert! "
            f"From {filtered_flights['cityName']}-{filtered_flights['cityNameCode']} to "
            f"{filtered_flights['destinationName']}-{filtered_flights['destinationNameCode']}, "
            f"Departure on {departure_datetime} "
            f"and Arrival on {destination_datetime}, "
            f"in just \u20B9 {filtered_flights['price']}" +
            (f", flight has one stop-over via "
             f"{filtered_flights["viaCityName"]}-"
             f"{filtered_flights["ViaCityCodeName"]}!"
             if filtered_flights["viaCityName"] is not None else "!")
        )

        # Send email to all users who opted for flight deals
        print("Sending flights deal to users via email...")
        notification_manager.send_email(users_emails)
        print("Emailed all users!")
