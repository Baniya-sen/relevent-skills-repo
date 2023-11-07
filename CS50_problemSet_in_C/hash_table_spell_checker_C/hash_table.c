#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

#include "hash_table.h"

// Struct for linked-list
typedef struct node
{
	char word[MAX_LENGTH + 1];
	struct node* next;
} node;

#define TABLE_SIZE 80000

// Hash Table
node* hash_table[TABLE_SIZE];

// Counter to mark every word that readed in load function
unsigned int words_read = 0;

// Checking word if it is present in dictionary of not, true if present
bool check_word(const char* word)
{
	unsigned int hash_value = hash(word);

	node* trav = hash_table[hash_value];
	while (trav != NULL)
	{
		if (stricmp(trav->word, word) == 0)
		{
			return true;
		}
		trav = trav->next;
	}

	return false;
}

// Multiplicative Hash function
unsigned int hash(const char *word)
{
	// Set initial value to a prime number
	unsigned int hash_value = 5380;

	// Loop through every letter of word
	int c;
	while ((c = tolower(*word++)))
	{
		// Multiply with a prime number and add ascii value of letter
		hash_value = hash_value * 33 + c;
	}

	// Make sure it stays in range of table size
	return hash_value % TABLE_SIZE;
}

// Loading dictionary in hash table
bool load_in(const char* dictionary)
{
	if (dictionary == NULL)
	{
		return false;
	}

	FILE* dict = fopen(dictionary, "r");
	if (dict == NULL)
	{
		return false;
	}

	bool is_loaded = false;
	char word[MAX_LENGTH + 1];

	while (fscanf(dict, "%s", word) == 1)
	{
		is_loaded = true;

		words_read++;

		unsigned int hash_value = hash(word);

		node* new_value = malloc(sizeof(node));
		if (new_value == NULL)
		{
			unload_mem();
			fclose(dict);
			return false;
		}

		strcpy(new_value->word, word);
		new_value->next = hash_table[hash_value];

		// Pre-pending the word in linked list
		hash_table[hash_value] = new_value;
	}
	fclose(dict);

	// return true if even one word is loaded
	return is_loaded;
}

unsigned int get_size(void)
{
	return 0 == words_read ? 0 : words_read;
}

bool unload_mem(void)
{
	unsigned int words_count = 0;

	for (unsigned int i = 0; i < TABLE_SIZE; i++)
	{
		node* delete = hash_table[i];

		// Traversing till end and freeing size by size of every linked list in hash table
		while (delete != NULL)
		{
			node* trav = delete->next;
			free(delete);
			delete = trav;
			words_count++;
		}
	}

	// Of words readed and words free are same, return true
	return words_count == words_read ? true : false;
}