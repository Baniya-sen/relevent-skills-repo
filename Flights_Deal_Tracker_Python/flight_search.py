import json.decoder
import os
from pprint import pprint

import requests


class FlightSearch:
    def __init__(self):
        """Searches flights with given destination iata-code with Tequila Flight Search API"""
        self.tequila_header = {"apikey": os.getenv("TEQUILA_KIWI_API_KEY")}
        self.tequila_location_url = "https://api.tequila.kiwi.com/locations/query"
        self.tequila_search_url = "https://api.tequila.kiwi.com/v2/search"

    def get_location_codes(self, city_name):
        """Get IATA code for a given city"""
        tequila_location_query = {"term": city_name}
        response = requests.get(
            url=self.tequila_location_url,
            headers=self.tequila_header,
            params=tequila_location_query
        )
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def get_flight_data(self, fly_from, fly_to, date_from, date_to, curr, cheap_or_not, max_stopovers=2):
        """Get flights data for a particular destination with specified date"""
        stopovers = 0

        # If there is no flight data from API, change stopovers to get in-direct flight
        while stopovers <= max_stopovers:
            tequila_search_query = {
                "fly_from": fly_from,
                "fly_to": fly_to,
                "date_from": date_from,
                "date_to": date_to,
                "curr": curr,
                "one_per_date": 1 if cheap_or_not else 0,
                "max_stopovers": stopovers,

            }
            print(f"Getting flights details for IATA code '{fly_to}'...", end=" ")
            response = requests.get(
                url=self.tequila_search_url,
                headers=self.tequila_header,
                params=tequila_search_query
            )
            response.raise_for_status()

            # If no 'data' key in response, then something went wrong with API
            try:
                if response.json()["data"]:
                    print("Done!")
                    return response.json()["data"]
            except (IndexError, KeyError, json.decoder.JSONDecodeError):
                print(f"ERROR: Something went wrong with Kiwi API!")
                return None

            # If no flight, increment stopover, and try in-direct flight
            stopovers += 1
            print(f"\nNo direct flight to '{fly_to}', trying flights with {stopovers} stop-over!")

        # If still no flight then exit
        print("No flights found within the specified stopovers.")
        return None
