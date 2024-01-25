import pandas
import requests
import datetime
import os

NUTRITIONIX_ENDPOINT = os.environ.get("NUTRITIONIX_ENDPOINT")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.environ.get("NUTRITIONIX_APP_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")


def personal_details():
    personal_info = {}
    try:
        personal_file = pandas.read_csv("personal_data.csv")
        # for data in personal_file:
        personal_info["gender"] = personal_file["gender"].iloc[0]
        personal_info["weight"] = personal_file["weight"].iloc[0]
        personal_info["height"] = personal_file["height"].iloc[0]
        personal_info["age"] = personal_file["age"].loc[0]

    except FileNotFoundError:
        personal_info["gender"] = input("What's your gender? [Male/Female]: ").lower()
        while True:
            try:
                personal_info["weight"] = float(input("Weight in Kg: "))
                personal_info["height"] = int(input("Height in cm: "))
                personal_info["age"] = int(input("Your age: "))
                break
            except ValueError:
                print("Enter valid input(s): ")
                pass
        pandas.DataFrame([personal_info]).to_csv("personal_data.csv", index=False)

    return personal_info


def exercise_details():
    user_info = personal_details()

    nutritionix_headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY,
        "Content-Type": "application/json",
    }
    nutritionix_data = {
        "query": input("What exercise did you performed? Duration?: "),
        "gender": user_info["gender"],
        "weight_kg": user_info["weight"],
        "height_cm": user_info["height"],
        "age": user_info["age"],
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
