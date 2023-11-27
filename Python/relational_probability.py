# Simulate a sport tournament relational possibility of winning chance of a team based on previous scores.

import sys
import csv
import random

# Number of tournaments
N = 1000


def main():
    """Ensuring proper usage"""
    if len(sys.argv) != 2:
        print("Usage: python relational_probability.py CSV_FILE_NAME")
        sys.exit(1)

    """List to store all team name and previous scores"""
    teams = []
    with open(sys.argv[1]) as infile:
        reader = csv.DictReader(infile)

        for team in reader:
            team["rating"] = int(team["rating"])
            teams.append(team)

    """Dict to store count of number of win a team get in N tournaments"""
    count = {}
    for i in range(N):
        winner_name = simulate_tournament(teams)
        if winner_name in count:
            count[winner_name] += 1
        else:
            count[winner_name] = 1

    # Printing teams chances sorted
    for team in sorted(count, key=lambda team: count[team], reverse=True):
        print(f"{team}: {count[team] * 100 / N:.1f}% chance of winning!")


# Simulate a dual between 2 teams, return true and false randomly based on previous scores
def simulate_dual(team1, team2):
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


# Simulate a single round
def simulate_round(teams):
    winner = []

    for i in range(0, len(teams), 2):
        if simulate_dual(teams[i], teams[i + 1]):
            winner.append(teams[i])
        else:
            winner.append(teams[i + 1])

    return winner


# Simulate a tournament, until a winner remains
def simulate_tournament(teams):
    while len(teams) != 1:
        teams = simulate_round(teams)

    """Returns the name of the winner team"""
    return teams[0]['team']


if __name__ == "__main__":
    main()
