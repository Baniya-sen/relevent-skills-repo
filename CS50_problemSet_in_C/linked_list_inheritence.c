// A person’s blood type is determined by two alleles (i.e., different forms of a gene).
// The three possible alleles are A, B, and O, of which each person has two (possibly the same, possibly different).
// Each of a child’s parents randomly passes one of their two blood type alleles to their child.
// The possible blood type combinations, then, are: OO, OA, OB, AO, AA, AB, BO, BA, and BB. For example,
// if one parent has blood type AO and the other parent has blood type BB, then the child’s possible blood types would be
// AB and OB, depending on which allele is received from each parent.Similarly, if one parent has blood type AO and the other OB,
// then the child’s possible blood types would be AO, OB, AB, and OO.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Struct for person with 2 allels and 2 parents
typedef struct person
{
	char allels[2];
	struct person *parents[2];
} person;

// Genration to print allels
const int GENERATIONS = 3;
const int INDENT = 4;

person *create_parents(int generations);
void print_family(person* person, int generation);
char rand_allels(void);
void free_family(person* person);

int main(void)
{
	// Seeding the initial value
	srand(time(0));

	// Pointer to gen Z
	person* person = create_parents(GENERATIONS);

	// Print family tree
	print_family(person, 0);

	// Free family of burden
	free_family(person);
}

person *create_parents(int generations)
{
	// Allocate memory for current person
	person* new_person = malloc(sizeof(person));

	// If generation > 1, recursively create parents
	if (generations > 1)
	{
		person* parent0 = create_parents(generations - 1);
		person* parent1 = create_parents(generations - 1);

		// Child pointer points to parent
		new_person->parents[0] = parent0;
		new_person->parents[1] = parent1;

		// Randomly allocate child allels from parents
		new_person->allels[0] = new_person->parents[0]->allels[rand() % 2];
		new_person->allels[1] = new_person->parents[1]->allels[rand() % 2];
	}
	
	else
	{
		// If only one generation, set random allels, and parents to null
		new_person->parents[0] = NULL;
		new_person->parents[1] = NULL;

		new_person->allels[0] = rand_allels();
		new_person->allels[1] = rand_allels();
	}

	return new_person;
}

void print_family(person* person, int generation)
{
	if (person == NULL)
	{
		return;
	}

	for (int i = 0; i < generation * INDENT; i++)
	{
		printf(" ");
	}

	if (generation == 0)
	{
		printf("Child (Generation %i): blood type %c%c\n", generation, person->allels[0], person->allels[1]);
	}
	else if (generation == 1)
	{
		printf("Parent (Genration %i): blood type %c%c\n", generation, person->allels[0], person->allels[1]);
	}
	else
	{
		for (int i = 0; i < generation - 2; i++)
		{
			printf("Great-");
		}
		printf("Grandparent (Generation %i): blood type %c%c\n", generation, person->allels[0], person->allels[1]);
	}

	print_family(person->parents[0], generation + 1);
	print_family(person->parents[1], generation + 1);
}

// Free allocated memory for persons recursively
void free_family(person* person)
{
	if (person == NULL)
	{
		free(person);
	}

	if (person != NULL)
	{
		free_family(person->parents[0]);
		free_family(person->parents[1]);
	}

	free(person);
}

// Random allels to only one generation
char rand_allels(void)
{
	int r = rand() % 3;

	if (r == 0)
	{
		return 'A';
	}
	else if (r == 1)
	{
		return 'B';
	}
	else if (r == 2)
	{
		return 'O';
	}

	return 'O';
}
