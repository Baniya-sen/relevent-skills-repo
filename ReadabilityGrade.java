/* A number of “readability tests” have been developed over the years that
 define formulas for computing the reading level of a text.
 One such readability test is the Coleman-Liau index.
 The Coleman-Liau index of a text is designed to output that (U.S.)
 grade level that is needed to understand some text. */

import java.util.Scanner;

import static java.lang.Character.isDigit;

public class ReadabilityGrade {

    public static void main(String[] args) {

//        Input
        Scanner s = new Scanner(System.in);

        System.out.print("Enter a text to check it's grade: ");
        String text = s.nextLine();
        int grade = gradeCalculate(text);

        if (grade == 0)
            System.out.println("Grade: 0");
        else if (grade >= 1 && grade <= 16)
            System.out.println("Grade: " + grade);
        else if (grade > 16)
            System.out.println("Grade: 16+");
    }

    static int gradeCalculate(String text) {
        double letters = 0;
        int spaces = 0;
        int digit = 0;
        int extraSymbols = 0;
        double sentences = 0;

        int textLength = text.length();

        for (int i =  0; i < textLength; i++) {
            if (text.charAt(i) == ' ')
                spaces += 1;
            else if (text.charAt(i) == ',' || text.charAt(i) == '\'' || text.charAt(i) == '"' || text.charAt(i) == '-' || text.charAt(i) == '_')
                extraSymbols += 1;
            else if (text.charAt(i) == '.' || text.charAt(i) == '!' || text.charAt(i) == '?')
                sentences += 1;
            else if (isDigit(text.charAt(i)))
                digit += 1;
        }

//        Space + 1 will be all words in a text
        double words = spaces + 1;

//        Subtracting all from total length will give us no. of letter.
        letters = textLength - (spaces + extraSymbols + digit + sentences);

//        Coleman-Liau index formula:
        double letterAverage = (letters / words) * 100;
        double sentenceAverage = (sentences / words) * 100;
        double gradeIndex = 0.0588 * letterAverage - 0.296 * sentenceAverage - 15.8;

//        Round-figure grade
        double grade = Math.round(gradeIndex);
        
        return (int) grade;
    }
}
