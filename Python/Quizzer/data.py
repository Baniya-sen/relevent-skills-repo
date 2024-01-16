import requests

params = {
    "amount": 20,
    "type": "boolean",
}

print("Getting questions...", end="\n\n")

# Get questions from opentdb API
response = requests.get(url="https://opentdb.com/api.php?", params=params)
response.raise_for_status()

# Save list of questions in question_data
question_data = response.json()["results"]
