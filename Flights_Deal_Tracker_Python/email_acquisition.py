import os
import requests
import time


def get_info(prompt):
    """Prompts user for an input"""
    while True:
        info = input(prompt)
        if info:
            break
        else:
            print("Enter information!")
    return info


def store_info(name, surname, email):
    """Stores the user data in Google sheet"""
    sheety_url = "https://api.sheety.co/3ac3988a9028fbe2e97c67a9dd37243e/flightDeals/users"
    sheety_headers = {
            "Authorization": os.getenv("Authorization"),
            "Content-Type": "application/json",
        }
    sheety_data = {
        "user": {
            "firstName": name,
            "lastName": surname,
            "email": email
        }
    }
    response = requests.post(url=sheety_url, headers=sheety_headers, json=sheety_data)
    response.raise_for_status()


print("Welcome to Baniya Flight's Club!")
time.sleep(1.4)
print("We'll find the best flight deals and email you.")
time.sleep(1.6)

user_name = get_info("What's your first name? ").title()
user_surname = get_info("What's your last name? ").title()

while True:
    user_email = get_info("What's your email? ")
    confirm_email = get_info("Confirm email: ")
    if user_email == confirm_email:
        break
    else:
        print("Email didn't matched! Try again.")

print("Saving info...", end=" ")
store_info(user_name, user_surname, user_email)
print("Done!")
