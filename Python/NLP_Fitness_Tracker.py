import requests
import datetime
import os

NUTRITIONIX_ENDPOINT = os.environ.get("NUTRITIONIX_ENDPOINT")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.environ.get("NUTRITIONIX_APP_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")


def exercise_details():
    nutritionix_headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY,
        "Content-Type": "application/json",
    }

    nutritionix_data = {
        "query": input("What exercise did you performed? Duration?: "),
        "gender": "male",
        "weight_kg": 84,
        "height_cm": 172,
        "age": 25,
    }

    response = requests.post(NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=nutritionix_data)
    response.raise_for_status()
    return response.json()


def update_google_sheet():
    nutritionix_nlp_result = exercise_details()

    sheety_headers = {
        "Authorization": os.environ.get("SHEETY_TOKEN"),
        "Content-Type": "application/json",
    }
    sheety_data = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%I:%M:%S %p"),
            "exercise": nutritionix_nlp_result["exercises"][0]["name"].title(),
            "duration": nutritionix_nlp_result["exercises"][0]["duration_min"],
            "calories": nutritionix_nlp_result["exercises"][0]["nf_calories"],
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=sheety_data)
    response.raise_for_status()


update_google_sheet()
