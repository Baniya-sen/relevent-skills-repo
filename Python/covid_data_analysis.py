from csv import DictReader
import requests


def main():
    # Download nyt covid-data from nyt GitHub, and decode in csv format to read
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = DictReader(file)

    # Calculate last 14 days new cases from consecutive data
    new_cases = calculate(reader)

    print("Choose one or more states to check averages.")
    print("Press enter when done.")

    states = []

    # Get user input for states which user want to look data
    while True:
        state = input("State: ").title()
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\n7-day average:")

    # Compare last week data with previous week's
    comparative_averages(new_cases, states)


def calculate(reader):
    new_cases = {}
    file = open("data.txt", 'w')

    # By subtracting previous cases from new cases, we get daily cases data, store only of last 14 days
    for item in reader:
        state = item["state"]
        cases = int(item["cases"])
        if state in new_cases:
            new_cases[state].append(cases - new_cases[state][-1])
            new_cases[state] = new_cases[state][-14:]
        else:
            new_cases[state] = [cases]

    return new_cases


def comparative_averages(new_cases, states):
    """Compare data of last week's to previous week's and get average"""
    for state in states:
        if state in new_cases:
            last_week_cases = sum(new_cases[state][0:7])
            previous_week_cases = sum(new_cases[state][7:14])
            average = last_week_cases - previous_week_cases
            change = "Increase" if average > 0 else "decrease"
            try:
                average_percent = average / previous_week_cases
            except ZeroDivisionError:
                print("No new case data!")

            print(f"{state} has an 7-day average of {average} and {change} of {average_percent:.4f}%.")


main()
