// Implementing Greedy Algorithm, using money change given.
// When making change, odds are you want to minimize the number of coins you�re
// dispensing for each customer, lest you run out. Fortunately, computer science
// has given cashiers everywhere ways to minimize numbers of coins due: greedy algorithms.

#include <stdio.h>

int get_cents();
int calculator_quaters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
	int cents = get_cents();
  	
	int quaters = calculator_quaters(cents);
	cents = cents - quaters * 25;

	int dimes =  calculate_dimes(cents);
	cents = cents - dimes * 10;

	int nickels =  calculate_nickels(cents);
	cents = cents - nickels * 5;

	int pennies =  calculate_pennies(cents);
	cents = cents - pennies * 1;

	int coins = quaters + dimes + nickels + pennies;

	printf("Coins owed: %i\n", coins);

	return 0;
}

int get_cents()
{
	int cents;

	do {
		printf("Enter cents owed: ");
		scanf_s("%i", &cents);
	} while (cents < 1);

	return cents;
}

int get_quaters(int cents)
{
	return cents >= 25 ? cents / 25 : 0;
}

int calculate_dimes(int cents)
{
	return cents >= 10 ? cents / 10 : 0;
}

int calculate_nickels(int cents)
{
	return cents >= 5 ? cents / 5 : 0;
}

int calculate_pennies(int cents)
{
	return cents > 0 ? cents : 0;
}