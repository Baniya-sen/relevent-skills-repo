// Wordle, a new “secret word” is chosen and the object is to guess what the secret word is within six tries.
// Fortunately, given that there are more than six five-letter words in the English language,
// one may get some clues along the way.

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define MAX_WORD_LENGTH 9
#define LISTSIZE 1000

// Defining exact scores for position and matching words
#define EXACT 2
#define CLOSE 1
#define WRONG 0

// Using Ascii value 033 as escape sequence
#define GREEN "\033[38;2;255;255;255;1m\033[48;2;106;170;100;1m"
#define YELLOW "\033[38;2;255;255;255;1m\033[48;2;201;180;88;1m"
#define RED "\033[38;2;255;255;255;1m\033[48;2;220;20;60;1m"
#define RESET "\033[0m"

char* get_guess(int wordsize);
int get_score(char *guess, int wordsize, char *choise, int *status);
void print_guess(char *guess, int *status);

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		printf("Usage: ./wordle WORDSIZE\n");
		return 1;
	}

	// Get wordsize
	int temp_wordsize = atoi(argv[1]);
	if (temp_wordsize < 5 || temp_wordsize > 8)
	{
		printf("Wordsize must be 5, 6, 7, or 8\n");
		return 2;
	}

	int wordsize = temp_wordsize;

	FILE* infile = fopen("words.txt", "r");
	if (infile == NULL)
	{
		printf("Can't open file\n");
		return 3;
	}

	// Array to hold all words from file
	char options[LISTSIZE][MAX_WORD_LENGTH];
	char current_word[MAX_WORD_LENGTH];
	int word_count = 0;

	// Check if word readed from file is of size user input
	while (fscanf(infile, "%s", current_word) == 1)
	{
		if (strlen(current_word) == wordsize)
		{
			strcpy(options[word_count], current_word);
			word_count++;
		}
		if (word_count >= LISTSIZE)
		{
			break;
		}
	}

	// If no words read, exit
	if (word_count == 0)
	{
		printf("There is no word in txt file regarding %i length!\n", wordsize);
		return 4;
	}

	// Seeding random word
	srand(time(NULL));

	// Selecting random word
	int random_index = rand() % word_count;
	char* choise = options[random_index];
	int guesses = wordsize + 1;
	bool won = false;

	printf("\n");
	printf(GREEN "Welcome to Wordle!" RESET "\n");
	printf("You have " RED " %i " RESET " tries left to guess the " GREEN " %i " RESET " length word:\n", guesses, wordsize);

	for (int i = 0; i < wordsize; i++)
	{
		// Get users guess
		char* guess = get_guess(wordsize);
		printf("Guess %i: ", i + 1);

		// Array to hold guess word status of Green, Yellow, Red
		int *status = malloc(sizeof(int) * wordsize);
		if (status == NULL)
		{
			printf("Memory allocation failed\n");
			return 5;
		}

		// Initialing array to 0, to wrong initial
		for (int i = 0; i < wordsize; i++)
		{
			status[i] = 0;
		}

		// Get users score of current guess
		int score = get_score(guess, wordsize, choise, status);
		print_guess(guess, status);

		free(status);

		// If user guessed it right
		if (score == EXACT * wordsize)
		{
			won = true;
			break;
		}
	}

	if (won)
	{
		printf(GREEN "You Won" RESET "\n");
	}
	else
	{
		printf(RED "You lose.. The word was %s" RESET "\n", choise);
	}

	return 0;
}

char* get_guess(int wordsize)
{
	static char guess[9] = "";

	// If guess contains previous value because of static, reset it
	if (strlen(guess) != 0)
	{
		memset(guess, 0, sizeof(guess));
	}

	// Take user guess until desired wordsize
	while (strlen(guess) != wordsize)
	{
		bool isValid = true;
		char temp_guess[9] = "";

		printf("Input a %i letter word: ", wordsize);
		fscanf(stdin, "%s", temp_guess);

		int n = strlen(temp_guess);
		for (int i = 0; i < n; i++)
		{
			// Check if all letters are alphabet, if not, take another guess
			if (!isalpha(temp_guess[i]))
			{
				isValid = false;
				break;
			}
		}
		if (isValid)
		{
			strcpy(guess, temp_guess);
		}
	}

	return guess;
}

int get_score(char* guess, int wordsize, char* choise, int* status)
{
	int score = 0;
	// Boolean array to check if current letter has been matched in current cycle
	bool is_matched[8] = { false };

	for (int i = 0; i < wordsize; i++)
	{
		int c = tolower(choise[i]);
		for (int j = 0; j < wordsize; j++)
		{
			int g = tolower(guess[j]);
			// Match ascii value because of same letter in different index
			if (c == g && !is_matched[j])
			{
				score += i == j ? EXACT : CLOSE;
				status[j] = i == j ? EXACT : CLOSE;
				is_matched[j] = true;
				break;
			}
		}
	}

	return score;
}

void print_guess(char* guess, int* status)
{
	// Loop through each char in guess
	while (*guess)
	{
		// Status represent score, so color match with score
		if (*status == EXACT)
		{
			printf(GREEN "%c" RESET, *guess);
		}
		else if (*status == CLOSE)
		{
			printf(YELLOW "%c" RESET, *guess);
		}
		else if (*status == WRONG)
		{
			printf(RED "%c" RESET, *guess);
		}

		*guess++;
		*status++;
	}
	printf("\n");
}
