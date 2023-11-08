// Theoretically, on input of size n, an algorithm with a running time of n is “asymptotically equivalent,”
// in terms of O, to an algorithm with a running time of 2n. Indeed, when describing the running time of an algorithm,
// we typically focus on the dominant (i.e., most impactful) term.
// This program designed to spell-check a file after loading a dictionary of words from disk into memory.
// That dictionary, meanwhile, is implemented in a file called dictionary.c.
// The prototypes for the functions therein, meanwhile, are defined not in dictionary.c itself but in dictionary.h instead. 

// Using Linked-list based Hash Table

// Usage: run compile.bat from terminal, then execute "./speller Dictionaries\large Text\LaLaLand.text"

#include <stdio.h>
#include <ctype.h>
#include <Windows.h>

#include "hash_table.h"

// Defining dictionary if user doesnt provide any
#define DICTIONARY "Dictionaries/large"

// Time performance of functions
double calculate(LARGE_INTEGER b, LARGE_INTEGER a, LARGE_INTEGER frequency);

int main(int argc, char* argv[])
{
	if (argc < 2 || argc > 3)
	{
		fprintf(stderr, "ERROR: Usage: ./speller [DICTIONARY NAME] [TEXT NAME]");
		return 1;
	}

	// Structures for timing data using Windows API
	LARGE_INTEGER before, after;
	LARGE_INTEGER frequency;

	// Benchmarks
	double time_load = 0.0, time_check = 0.0, time_size = 0.0, time_unload = 0.0;
	QueryPerformanceFrequency(&frequency);

	// Default dictionary if user does'nt provide any
	char* dictionary = argc == 3 ? argv[1] : DICTIONARY;

	// Load dictionary
	QueryPerformanceCounter(&before);
	bool loaded = load_in(dictionary);
	QueryPerformanceCounter(&after);

	if (!loaded)
	{
		fprintf(stderr, "ERROR: Could not load dictionary!");
		return 2;
	}

	// Calculate time to load dictionary
	time_load = calculate(before, after, frequency);

	// Opening text file that user provided
	char* text_file = argc == 3 ? argv[2] : argv[1];
	FILE* t_file = fopen(text_file, "r");
	if (t_file == NULL)
	{
		fprintf(stderr, "ERROR: Could not open text file %s!", text_file);
		unload_mem();
		return 3;
	}

	// Prepare to report misspellings
	printf("\nMISSPELLED WORDS\n\n");

	int index = 0, misspellings = 0, words = 0;
	char word[MAX_LENGTH + 1];

	// Reading words from text file character by character
	char c;
	while (fread(&c, sizeof(char), 1, t_file))
	{
		// If char is alpha or apostrophe
		if (isalpha(c) || (c == '\'' && index > 0))
		{
			// Add letter to word
			word[index] = c;
			index++;

			// Consume rest of letters if word is greater than max length
			if (index > MAX_LENGTH)
			{
				while (fread(&c, sizeof(char), 1, t_file) && isalpha(c));

				index = 0;
			}
		}

		// If char is digit or alphnumeric, consume all till next word
		else if (isdigit(c))
		{
			while (fread(&c, sizeof(char), 1, t_file) && isalnum(c));

			index = 0;
		}

		//If char is niether alphabet nor alphanumeric, then must have finished reading a word
		else if (index > 0)
		{
			// Terminate current word
			word[index] = '\0';

			// Increate word counter
			words++;

			// Check word's spelling
			QueryPerformanceCounter(&before);
			bool misspelled = !check_word(word);
			QueryPerformanceCounter(&after);

			// Update benchmark
			time_check += calculate(before, after, frequency);

			// Report misspelled word
			if (misspelled)
			{
				printf("%s\n", word);
				misspellings++;
			}

			index = 0;
		}
	}

	// If any error reading a file
	if (ferror(t_file))
	{
		fclose(t_file);
		unload_mem();
		fprintf(stderr, "ERROR reading!\n");
		return 5;
	}

	fclose(t_file);

	// Determine dictionary's size
	QueryPerformanceCounter(&before);
	unsigned int n = get_size();
	QueryPerformanceCounter(&after);

	time_size = calculate(before, after, frequency);

	QueryPerformanceCounter(&before);
	bool unloaded = unload_mem();
	QueryPerformanceCounter(&after);

	// If any error unloading dictionary from memory
	if (!unloaded)
	{
		fprintf(stderr, "ERROR: Can't unload!");
		return 7;
	}

	// Calculate time to unload dictionary
	time_unload = calculate(before, after, frequency);

	// Report benchmarks
	printf("\nWORDS MISSPELLED:     %d\n", misspellings);
	printf("WORDS IN DICTIONARY:  %d\n", n);
	printf("WORDS IN TEXT:        %d\n", words);
	printf("TIME IN load:         %.2f\n", time_load);
	printf("TIME IN check:        %.2f\n", time_check);
	printf("TIME IN size:         %.2f\n", time_size);
	printf("TIME IN unload:       %.2f\n", time_unload);
	printf("TIME IN TOTAL:        %.2f\n\n", time_load + time_check + time_size + time_unload);

	// Success
	return 0;
}

// Returns number of seconds between b and a
double calculate(LARGE_INTEGER b, LARGE_INTEGER a, LARGE_INTEGER frequency) {
	return (double)(a.QuadPart - b.QuadPart) / frequency.QuadPart;
}

