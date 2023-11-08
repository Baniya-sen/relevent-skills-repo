// Imagine you just rescued a dog and you’re deciding on a name. You found a file online with a list of about 150 of the
// most popular dog names! You are curious as to whether or not the names you are considering are on this list. 
// Trie's are great at data lookup, giving time complexity of O(1) in inserting, since all steps in serting are constand,
// also 0(1) for data lookup even as worst case.

// Trie -  Data inserting and Lookup

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

#define MAX_ALPHABET 26
#define MAX_CHAR 20

// Trie data structure, every node has one boolean for if word found, and 26 pointers for every alphabet
typedef struct node
{
	bool is_valid;
	struct node* index[MAX_ALPHABET];
} node;

// Root node
node* root;

// Max length of a word
char word[MAX_CHAR];

// Prototypes
bool check_dogname(char* name);
bool unload_trie(void);
void deallocate(node* ptr);

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		fprintf(stderr, "ERROR: Usage: ./trie_insert_search [Text_File]");
		return 1;
	}

	// Opening text file provided by user
	FILE* t_file;
	errno_t err = fopen_s(&t_file, argv[1], "r");
	if (err != 0)
	{
		// If file is empty or there is error
		fprintf(stderr, "ERROR: Can't read file- %s!", argv[1]);
		return 2;
	}

	root = malloc(sizeof(node));
	if (root == NULL)
	{
		fprintf(stderr, "ERROR: Can't allocate memory!");
		return 3;
	}

	// Set initial values to root node
	root->is_valid = false;
	for (int i = 0; i < MAX_ALPHABET; i++)
	{
		root->index[i] = NULL;
	}

	// Reading 1 word at a time from file
	while (fscanf(t_file, "%s", word) == 1)
	{
		int n = strlen(word);
		node* trav = root;

		for (int i = 0; i < n; i++)
		{
			// Getting hash value based on every letter of word
			unsigned int index_value = tolower(word[i]) - 'a';
			
			// If index in trie is NULL, i.e. has no child trie 
			if (trav->index[index_value] == NULL)
			{
				node* new_trie = malloc(sizeof(node));
				if (new_trie == NULL)
				{
					fprintf(stderr, "ERROR: Can't allocate memory!");
					return 3;
				}
				new_trie->is_valid = false;
				for (int j = 0; j < MAX_ALPHABET; j++)
				{
					new_trie->index[j] = NULL;
				}

				// Index of trie follows new trie
				trav->index[index_value] = new_trie;
			}

			// Preparing pointer for next trie
			trav = trav->index[index_value];
		}

		// If word is added then add true to its boolean variable
		trav->is_valid = true;
	}

	// Get user input to check word
	char name[MAX_CHAR];
	printf("Enter word: ");
	scanf_s("%s", name, (unsigned)sizeof(name));

	if (check_dogname(name))
	{
		printf("Found %s!\n", name);
	}
	else
	{
		fprintf(stderr, "Not Found!\n");
	}

	if (!unload_trie())
	{
		fprintf(stderr, "ERROR: Can't unload memory!\n");
	}

	return 0;
}

bool check_dogname(char* name)
{
	int c;
	node* trav = root;

	// Travere through word's every letter and search trie for word
	while ((c = tolower(*name++)))
	{
		c = c - 'a';
		
		if (trav->index[c] == NULL)
		{
			return false;
		}

		trav = trav->index[c];
	}

	// If we reach end of letters in word and its boolean is true, then word is complete and found
	return trav->is_valid == true ? true : false;
}

// Free memory
bool unload_trie(void)
{
	node* delete = root;
	deallocate(root);
	return true;
}

void deallocate(node *ptr)
{
	for (int i = 0; i < MAX_ALPHABET; i++)
	{
		if (ptr->index[i] != NULL)
		{
			// Recursively call deallocate to free every trie
			deallocate(ptr->index[i]);
		}
	}

	free(ptr);
}