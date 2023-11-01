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
	if (checksum == 1)
	{
		printf("invalid\n");
		return 1;
	}
}

// Varify card checksum using Luhn's algorotm
int verify_checksum(long card_number)
{
	int card_length, card_index_odd, card_index_even  = 0;
	while (card_number != 0)
	{
		// Divide card number by 10 untill it becomes 0, extracting card number length
		card_number / 10;
		card_length++;
	}

	int products_digit, sum_digit = 0;
	int card_number_odd, card_number_even = card_number;

	// Selecting every other odd digit from card number, multipying by 2, and then add those digits
	do
	{
		// Extracting card number's last digit
		int odd_digit = card_number_odd % 10;

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

		//Shorten the card length for next loop
		card_number_odd = card_number_odd / 10;
		card_index_odd++;
	}
	while (card_index_odd < card_length);

	// Now adding the card's those digits that were'nt multiplied by 2
	do
	{
		int even_digit = card_number_even % 10;

		if (card_index_even % 2 == 0)
		{
			sum_digit += even_digit;
		}

		card_number_even = card_number_even / 10;
		card_index_even++;

	} while (card_index_even < card_length);

	// If both product_digit and sum_digit added, and thier last digit is 0, checksum passes
	return ((products_digit + sum_digit) % 10 == 0) ? 0 : 1;
}