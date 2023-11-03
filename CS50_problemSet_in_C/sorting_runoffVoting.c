// We already know about plurality elections, which follow a very simple algorithm for determining the winner of an election:
// Every voter gets one vote, and the candidate with the most votes wins.
// But the plurality vote does have some disadvantages.What happens, for instance, in an election with three candidates,
// there is tie?
// There’s another kind of voting system known as a ranked-choice voting system. In a ranked-choice system,
// voters can vote for more than one candidate. Instead of just voting for their top choice,
// they can rank the candidates in order of preference- 1st, 2nd, 3rd or so on. 
// If no candidate has more than 50% of the vote, then an “instant runoff” occurs.
// The candidate who received the fewest number of votes is eliminated from the election,
// and anyone who originally chose that candidate as their first preference now has their second preference considered.
// Why do it this way? Effectively, this simulates what would have happened if the least popular candidate had not
// been in the election to begin with.

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_CANDIDATES 9
#define MAX_VOTERS 100

// Array to hold winner position index as preferences from input
int preferences[MAX_VOTERS][MAX_CANDIDATES];

typedef struct
{
	char name[50];
	int votes;
	bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

int voter_count;
int candidate_count;

bool name_check(int voter, int candidate, char* name);
void tabulate();
bool print_winner();
int find_min();
bool is_tie(int min);
void eliminate(int min);

int main(int argc, char* argv[])
{
	if (argc < 2)
	{
		printf("Usage: ./sorting_runoffVoting [CANDIDATES NAMES..]\n");
		return 1;
	}

	candidate_count = argc - 1;
	if (candidate_count > MAX_CANDIDATES)
	{
		printf("Only %i are allowed\n", MAX_CANDIDATES);
		return 2;
	}

	printf("Enter no. of voters: ");
	scanf_s("%d", &voter_count);
	if (candidate_count < 1 || candidate_count > 100)
	{
		printf("Only 1 to 100 voters allowed per poll!\n");
		return 3;
	}

	// Setting name from command line to candidate array
	for (int i = 0; i < candidate_count; i++)
	{
		int name_length = strlen(argv[i + 1]);
		strcpy(candidates[i].name, argv[i + 1]);
		candidates[i].votes = 0;
		candidates[i].eliminated = false;
	}

	printf("\nEnter you preferences: \n");

	// Loop to take input preference from user until all voters vote for desired candidates
	for (int i = 0; i < voter_count; i++)
	{
		for (int j = 0; j < candidate_count; j++)
		{
			char name[50];
			printf("Rank %i: ", j + 1);
			fscanf(stdin, "%s", name);

			if (!name_check(i, j, name))
			{
				printf("There is no %s in candidates!\n", name);
				return 5;
			}

		}
		printf("\n");
	}

	// True until we get a winner
	while (true)
	{
		// Tabulates the votes for each candidate
		tabulate();

		// If there is a winner, break
		if (print_winner())
		{
			break;
		}

		// If there is not winner, find minimum vote a candidate has
		int min = find_min();

		// If if there is a tie in all candidates
		if (is_tie(min))
		{
			for (int i = 0; i < candidate_count; i++)
			{
				if (!candidates[i].eliminated)
				{
					candidates[i].name[0] = toupper(candidates[i].name[0]);
					printf("Winners - %s\n", candidates[i].name);
				}
			}
			break;
		}

		// Eliminate candidates who has minimum votes
		eliminate(min);

		// If no winner, then reset votes and tabulate again within remaining candidates
		int i = 0;
		while (i < candidate_count)
		{
			candidates[i].votes = 0;
		}

	}

	return 0;
}

// Check if a user input name is candidate name or not
bool name_check(int voter, int candidate, char* name)
{
	int i = 0, count = 0;
	bool isValid = false;
	
	while (i < candidate_count)
	{
		char* nameB_ptr = candidates[i].name;
		int name_length = strlen(candidates[i].name);
		
		// Loop through candidates names each letter for case insensitivity
		while (*name && *nameB_ptr && (tolower(*name) == tolower(*nameB_ptr)))
		{
			*name++;
			*nameB_ptr++;
			count++;
		}
		i++;

		// Name is correct, return true
		if (count == name_length)
		{
			preferences[voter][candidate] = i - 1;
			return true;
		}
	}

	return false;
}

// Gives 1 vote for candidates who has been given as first preference os a votes,
// if eliminated, give vote to second preference
void tabulate()
{
	for (int i = 0; i < voter_count; i++)
	{
		int j = 0;
		while (candidates[preferences[i][j]].eliminated)
		{
			j++;
		}
		candidates[preferences[i][j]].votes++;
	}
}

// If a candidate has more than 50% votes, declare winner
bool print_winner()
{
	int majority_votes = (voter_count / 2) + 1;

	for (int i = 0; i < candidate_count; i++)
	{
		if (!candidates[i].eliminated && candidates[i].votes >= majority_votes)
		{
			candidates[i].name[0] = toupper(candidates[i].name[0]);
			printf("Winner is - %s!\n", candidates[i].name);
			return true;
		}
	}

	return false;
}

// Find minimum votes a candidate got in all candidates
int find_min()
{
	int minimum_votes = voter_count;
	for (int i = 0; i < candidate_count; i++)
	{
		if (!candidates[i].eliminated && candidates[i].votes < minimum_votes)
		{
			minimum_votes = candidates[i].votes;
		}
	}
	return minimum_votes;
}

// If tie in all candidates, return true
bool is_tie(int min)
{
	int i = 0;
	while (i < candidate_count)
	{
		if (candidates[i].votes != min && !candidates[i].eliminated)
		{
			return false;
		}
		i++;
	}
	return true;
}

// Eliminate all candidates who have minimum vote or equal to it
void eliminate(int min)
{
	int i = 0;
	while (i < candidate_count)
	{
		if (candidates[i].votes == min && !candidates[i].eliminated)
		{
			candidates[i].eliminated = true;
		}
		i++;
	}
}