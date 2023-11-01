// There are a lot of people with credit cards in this world, so card numbers are pretty long.
// Credit card numbers actually have some structure to them. All American Express numbers start with 34 or 37;
// most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers
// which we won’t concern ourselves with for this problem); and all Visa numbers start with 4.
// But credit card numbers also have a “checksum” built into them, a mathematical relationship between
// at least one number and others. That checksum enables computers to detect typos (e.g., transpositions),
// if not fraudulent numbers, without having to query a database, which can be slow

// Using Luhn's Algorithm

#include <stdio.h>

int verify_checksum(long card_number);

int main(void)
{
	long card_number;

	printf("Card number: ");
	scanf_s("%li", &card_number);

	int checksum = verify_checksum(card_number);
}

// Varify card checksum using Luhn's algorotm
int verify_checksum(long card_number)
{
	int card_length, card_index = 0;

	while (card_number != 0)
	{
		// Divide card number by 10 untill it becomes 0, extracting card number length
		card_number / 10;
		card_length++;
	}

	int products_digit = 0;

	do
	{
		// Extracting card number's last digit
		int odd_digit = card_number / 10;

		// Checking if didgit is at odd place
		if (card_index % 2 == 1)
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
	}
}