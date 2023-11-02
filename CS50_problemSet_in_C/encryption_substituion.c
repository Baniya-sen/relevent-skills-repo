// In a substitution cipher, we “encrypt” a message by replacing every letter with another letter.
// To do so, we use a key: in this case, a mapping of each of the letters of the alphabet to the letter
// it should correspond to when we encrypt it.
// To “decrypt” the message, the receiver of the message would need to know the key,
// so that they can reverse the process: translating the encrypt text back into the original message.
// A key, for example, might be the string NQXPOMAFTRHLZGECYJIUWSKDVB.
// This 26 - character key means that A(the first letter of the alphabet) should be converted into N(the first character of the key),
// B(the second letter of the alphabet) should be converted into Q(the second character of the key), and so forth.
// A message like HELLO, then, would be encrypted as FOLLE, replacing each of the letters according to the mapping determined by the key.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char *rotate(char *plaintext, int plaintext_length, char *key);

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		printf("Usage: ./encryption_substitution key");
		return 1;
	}

	if (strlen(argv[1]) != 26)
	{
		printf("Key must be 26 characters\n");
		return 2;
	}

	char plaintext[10001];
	printf("Message to encrypt: ");
	fgets(plaintext, sizeof(plaintext), stdin);

	int plaintext_length = strlen(plaintext);
	char* ciphertext = malloc(sizeof(char) * plaintext_length);

	ciphertext = rotate(plaintext, plaintext_length, argv[1]);
	printf("%s\n", ciphertext);

	free(ciphertext);

	return 0;
}

char* rotate(char* plaintext, int plaintext_length, char *key)
{
	int i = 0;
	char* ciphertext = malloc(sizeof(char) * plaintext_length);

	while (*plaintext)
	{
		if (isalpha(*plaintext))
		{
			ciphertext[i] = (isupper(*plaintext)) ? toupper(key[*plaintext - 'A']) : tolower(key[*plaintext - 'a']);
		}
		else
		{
			ciphertext[i] = *plaintext;
		}

		plaintext++;
		i++;
	}
	ciphertext[i] = '\0';

	return ciphertext;
}