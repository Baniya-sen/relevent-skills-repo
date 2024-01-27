import os
import requests
from flight_search import FlightSearch


class DataManager:
    def __init__(self):
        """This class searches google sheet for destinations and parse it to the Flight Search API"""
        self.url_prices = "https://api.sheety.co/3ac3988a9028fbe2e97c67a9dd37243e/flightDeals/prices"
        self.url_users = "https://api.sheety.co/3ac3988a9028fbe2e97c67a9dd37243e/flightDeals/users"
        self.headers = {
            "Authorization": os.getenv("Authorization"),
            "Content-Type": "application/json",
        }

    def verify_iata_codes(self):
        """Verifies if all destination have their respective IAT codes in google sheet"""
        print("Verifying your destinations IATA codes...")

        flight_search_instance = FlightSearch()
        response = requests.get(url=self.url_prices, headers=self.headers)
        response.raise_for_status()

        # If destination doesn't have IATA-code, then call flight search api and get IATA-code
        for destination in response.json()["prices"]:
            if not destination["iataCode"]:
                print(f"Updating destinations IATA code for '{destination["city"]}'...", end=" ")

                # Put code in google sheet
                query = {"price": {"iataCode": flight_search_instance.get_location_codes(destination["city"])}}
                response = requests.put(
                    url=f"{self.url_prices}/{destination["id"]}",
                    headers=self.headers,
                    json=query
                )
                response.raise_for_status()
                print("Done!")

    def get_users_emails(self):
        """Get all users emails from Google sheet"""
        print("Getting users emails...", end=" ")

        response = requests.get(url=self.url_users, headers=self.headers)
        response.raise_for_status()
        print("Done!")
        return response.json()["users"]

    def get_location_data(self):
        """Get all destinations data from Google sheet"""
        print("Getting your destinations...", end=" ")

        response = requests.get(url=self.url_prices, headers=self.headers)
        response.raise_for_status()
        print("Done!", end="\n\n")
        return response.json()["prices"]
