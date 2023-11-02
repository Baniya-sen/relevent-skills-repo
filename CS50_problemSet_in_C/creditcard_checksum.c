// There are a lot of people with credit cards in this world, so card numbers are pretty long.
// Credit card numbers actually have some structure to them. All American Express numbers start with 34 or 37;
// most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers
// which we won�t concern ourselves with for this problem); and all Visa numbers start with 4.
// But credit card numbers also have a �checksum� built into them, a mathematical relationship between
// at least one number and others. That checksum enables computers to detect typos (e.g., transpositions),
// if not fraudulent numbers, without having to query a database, which can be slow

// Using Luhn's Algorithm

#include <stdio.h>
#include <string.h>

int verify_checksum(unsigned long long card_number, int card_length);
char *verify_card_class(char *card_number_s, int card_length);

int main(void)
{
	unsigned long long card_number;

	printf("Card number: ");
	scanf_s("%llu", &card_number);

	char card_number_s[16];
	sprintf(card_number_s, "%llu", card_number);
	int card_length = strlen(card_number_s);

	if (card_length < 13 || card_length > 16)
	{
		printf("Please enter valid Card!\n");
		return 1;
	}

	int checksum = verify_checksum(card_number, card_length);

	if (checksum == 1)
	{
		printf("INVALID\n");
		return 1;
	}

	char *card_name = verify_card_class(card_number_s, card_length);
	printf("%s\n", card_name);

	return 0;
}

// Verify card checksum using Luhn's algorotm
int verify_checksum(unsigned long long card_number, int card_length)
{
	int card_index_odd = 0, card_index_even = 0;
	unsigned long long card_number_odd_copy = card_number, card_number_even_copy = card_number;

	int products_digit = 0, sum_digit = 0;

	// Selecting every other odd digit from card number, multipying by 2, and then add those digits
	do
	{
		// Extracting card number's last digit
		int odd_digit = card_number_odd_copy % 10;

		// Checking if digit is at odd place
		if (card_index_odd % 2 == 1)
		{
			int digit_by_2 = odd_digit * 2;

			// We have to add every odd digit multiplied by 2 to each others, not the product themselves
			if (digit_by_2 > 9)
			{
				// If a number is grater than 9, add their first and second digit
				int digits_first_place = digit_by_2 % 10;
				int digits_second_place = digit_by_2 / 10;
				digit_by_2 = digits_first_place + digits_second_place;
			}

			products_digit += digit_by_2;
		}

		//Shorten the card length
		card_number_odd_copy = card_number_odd_copy / 10;
		card_index_odd++;
	}
	while (card_index_odd < card_length);

	// Now adding the card's those digits that were'nt multiplied by 2
	do
	{
		int even_digit = card_number_even_copy % 10;

		sum_digit += (card_index_even % 2 == 0) ? even_digit : 0;

		card_number_even_copy = card_number_even_copy / 10;
		card_index_even++;

	} while (card_index_even < card_length);

	// If both product_digit and sum_digit added, and thier last digit is 0, checksum passes
	return ((products_digit + sum_digit) % 10) == 0 ? 0 : 1;
}

// Verify card is of which brand
char* verify_card_class(char *card_number_s, int card_length) {

	char card_name_first_2_digits[3];
	strncpy(card_name_first_2_digits, card_number_s, 2);
	card_name_first_2_digits[2] = '\0';

	if (card_length == 13 && card_number_s[0] == '4')
	{
		return "VISA!";
	}
	else if (card_length == 15 && strcmp(card_name_first_2_digits, "34") == 0 || strcmp(card_name_first_2_digits, "37") == 0)
	{
		return "AMEX!";
	}
	else if (card_length == 16)
	{
		if (strcmp(card_name_first_2_digits, "51") == 0 || strcmp(card_name_first_2_digits, "52") == 0 || strcmp(card_name_first_2_digits, "53") == 0 || strcmp(card_name_first_2_digits, "54") == 0 || strcmp(card_name_first_2_digits, "55") == 0)
		{
			return "MASTERCARD!";
		}
		else if (card_number_s[0] == '4')
		{
			return "VISA!";
		}
	}
	
	return "INVALID!";
}