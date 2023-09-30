// Covert strings to ascii to binary to emojis.

import java.util.Scanner;

public class StringToBinaryEmojis {

    static final int BITS_IN_BYTE = 8;
    static  final int BASE = 2;

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        System.out.print("Enter string to convert to binary(s): ");
        String text = s.nextLine();

        int textLength = text.length();
//        Array to store ascii values of string
        int[] textAsciiValue = new int[textLength];

//        Covert string to their ascii value
        for (int i = 0; i < textLength; i++) {
            textAsciiValue[i] = text.charAt(i);
        }

        int[] remainder = new int[BITS_IN_BYTE];
        int[][] bitsRemainder = new int[textLength][BITS_IN_BYTE];

        for (int i =0; i < textLength; i++) {
            int temp = textAsciiValue[i];

            for (int j =0; j < BITS_IN_BYTE; j++) {
                remainder[i] = temp % BASE;    // Storing modules(0 or 1) into remainder array
                bitsRemainder[i][j] = remainder[i];
                temp /= BASE;  // Then divide temp with 2 to get next quotient
            }
        }

        for (int i = 0; i <  textLength; i++) {
            for (int j = BITS_IN_BYTE - 1; j >= 0; j--) {
                print_bulbs(bitsRemainder[i][j]);  // Sending 0 or 1 to print emoji
            }
            System.out.println();
        }
    }

    static void print_bulbs(int bit) {
        if (bit == 0)
        {
            // Dark emoji
            System.out.print("\uD83D\uDFE1");
        }
        else if (bit == 1)
        {
            // Light emoji
            System.out.print("\uD83D\uDFE2");
        }
    }
}
