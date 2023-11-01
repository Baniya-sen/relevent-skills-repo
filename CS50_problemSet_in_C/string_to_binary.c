// Computers, use base-2, or binary. Binary numbers can only have 0s and 1s.
// But the process of figuring outexactly what decimal number a binary number stands for is easy.
//This program takes a message and converts it to a set of bits (or emojis) that we could show to an unsuspecting audience.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BASE 2
#define BITS_IN_BYTE 8

int convert(int string_ascii_value[], int string_length);
print_emoji(int bit);

int main(void)
{
	char message[200];
	printf("Message: ");
	scanf("%s", &message);

	int string_length = strlen(message);

	// Array to store ascii values of string
	int *string_ascii_value = malloc(sizeof(int) * string_length);
	if (string_ascii_value == NULL) {
		printf("Memory allocation failed.\n");
		return 1;
	}

	// Converting string to there ascii values
	for (int i = 0; i < string_length; i++)
	{
		string_ascii_value[i] = message[i];
	}

	int string_to_emoji = convert(string_ascii_value, string_length);
	if (string_to_emoji == 1)
	{
		// If count is not equals to desired array, some error occured
		printf("Some error occured!\n");
		free(string_ascii_value);
		return 3;
	}

	free(string_ascii_value);

	return 0;
}

int convert(int string_ascii_value[], int string_length)
{
	// Allocating memory for 2d array to store generated bit values
	int (*converted_bits)[BITS_IN_BYTE] = malloc(string_length * sizeof(*converted_bits));

	if (converted_bits == NULL) {
		printf("Memory allocation failed.\n");
		return 2;
	}

	int count = 0;

	for (int i = 0; i < string_length; i++)
	{
		int temp = string_ascii_value[i];

		for (int j = 0; j < BITS_IN_BYTE; j++)
		{
			// LCM of ascii value, remainder of the value is a corresponding binary value
			int remainder = temp % BASE;
			converted_bits[i][j] = remainder;
			temp /= BASE;
			count++;
		}
	}

	for (int i = 0; i < string_length; i++)
	{
		// in LCM of ascii values, the remainders of ascii values should be in reverse order for a 8 bit sequence
		for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
		{
			print_emoji(converted_bits[i][j]);
		}
		printf("\n");
	}

	free(converted_bits);

	return ((string_length * BITS_IN_BYTE) == count) ? 0 : 1;
}

print_emoji(int bit)
{
	if (bit == 0)
	{
		// Currently printing 0 and 1, can change to emoji unicode 
		printf("0");
	}
	else if (bit == 1)
	{
		printf("1");
	}
}