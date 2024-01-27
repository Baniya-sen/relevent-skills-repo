import datetime


class FlightData:
    """This class is responsible for structuring and sorting the flight data"""
    def __init__(self, flight_search_data, budget):
        self.budget = budget
        self.filtered_flight = {}

        # Sot the all flights data on price and departure-time basis
        self.sorted_flights = sorted(
            flight_search_data,
            key=lambda x: (x["price"], x["local_departure"])
        )

    def filter_flight(self):
        """Get first flight from flight data and store info in a dict"""
        print("Sorting data with budget...", end=" ")

        # If flight is a stopover > 0, get name of city via to reach destination
        try:
            via_city = self.sorted_flights[0]["route"][1]["cityFrom"]
            via_city_code = self.sorted_flights[0]["route"][1]["cityCodeFrom"]
        except IndexError:
            via_city = None
            via_city_code = None

        # If there are flights and first flight price is <= budget, store details, or store error
        self.filtered_flight = (
            {
                "price": self.sorted_flights[0]["price"],
                "cityName": self.sorted_flights[0]["cityFrom"],
                "cityNameCode": self.sorted_flights[0]["cityCodeFrom"],
                "viaCityName": via_city,
                "ViaCityCodeName": via_city_code,
                "destinationName": self.sorted_flights[0]["cityTo"],
                "destinationNameCode": self.sorted_flights[0]["cityCodeTo"],
                "departureDateTime": self.sorted_flights[0]["local_departure"],
                "destinationDateTime": self.sorted_flights[0]["local_arrival"]
            }
            if self.sorted_flights and self.sorted_flights[0]["price"] <= self.budget
            else
            {"Information": "No flights in this budget!"}
            if self.sorted_flights
            else
            {"Information": "No flights available!"}
        )
        return self.filtered_flight

