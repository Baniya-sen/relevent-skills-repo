/*Supposedly, Caesar used to encrypt confidential messages by shifting each letter therein by
some number of places. For instance, he might write A as B, B as C, C as D, …, and,
wrapping around alphabetically, Z as A. And so, to say HELLO to someone, Caesar might write IFMMP instead.
Upon receiving such messages from Caesar, recipients would have to decrypt them
by shifting letters in the opposite direction by the same number of places.*/

import java.util.Scanner;
import static java.lang.Character.*;

public class CaesarEncryption {

    final static int alphabetLength = 26;
    static char[] ALPHA = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    static char[] alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    static char[] punctuations = {' ', '.', ',', '!', '?', '@'};

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        if (args.length != 1) {
            System.out.println("Usage: java \"class_name\" \"key\"");
            System.exit(1);
        } else {
            String argument1 = args[0];
            if (!argument1.matches("\\d+")) {
                System.out.println("The provided key contains non-digit characters.");
                System.exit(1);
            }
        }

        int key = Integer.parseInt(args[0]);

        System.out.print("Plaintext:  ");
        String plainText = s.nextLine();

        String cipherText = "";
        for (int i = 0; i < plainText.length(); i++) {
            char rotatedChar = rotate(plainText.charAt(i),key);
            cipherText += rotatedChar;
        }

        System.out.print("Ciphertext: ");
        for (int i = 0; i < plainText.length(); i++) {
            System.out.print(cipherText.charAt(i));
        }
    }

    static char rotate(char ciphertext, int key) {
        char cipherT = '0';
        char verifyCiphertext = toUpperCase(ciphertext);

        for (int i = 0; i < alphabetLength; i++) {
            if (verifyCiphertext == ALPHA[i]) {
                if (isUpperCase(ciphertext)) {
                    cipherT = ALPHA[(i + key) % alphabetLength];
                    break;
                } else if (isLowerCase(ciphertext)) {
                    cipherT = alpha[(i + key) % alphabetLength];
                    break;
                }
            }
            else if (ciphertext == punctuations[i % punctuations.length]) {
                cipherT = ciphertext;
            }
        }
        return cipherT;
    }
}
