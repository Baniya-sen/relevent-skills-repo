import java.text.NumberFormat;
import java.util.Scanner;

public class Mortgage {
    public static void main(String[] args) {


//         Initialization
        long principal;
        Scanner s = new Scanner(System.in);
        float aInterest;
        float mInterest;
        byte years;
        int totalMonPay;
        final byte one = 1;
        double totalPay;
        final int percent = 100;
        final int monthsInYears = 12;
        NumberFormat currency = NumberFormat.getCurrencyInstance();

//         User Input
        do {
            System.out.print("Principal: ");
            principal = s.nextLong();
        } while (principal < 1000 || principal > 100000000);

//         One method
        while (true) {
            System.out.print("Annual Interest: ");
            aInterest = s.nextFloat();
            if (aInterest >= 1 || aInterest <= 30)
                break;
            System.out.println("Enter value from 1 to 30");
        }
//         Alternate method
        while (true) {
            System.out.print("Years: ");
            years = s.nextByte();
            if (years < 1 || years > 99) {
                System.out.println("Enter value from 1 to 99");
            }
            else {
                break;
            }
        }

//         values:
        mInterest = (aInterest / percent) / monthsInYears;
        totalMonPay = years * monthsInYears;

//         Equation:
        String mInterMoney = currency.format(principal * ((Math.pow((one + mInterest), totalMonPay) * mInterest) / (Math.pow((one + mInterest), totalMonPay) - 1)));
        double mInterMoneyNonCurF = principal * ((Math.pow((one + mInterest), totalMonPay) * mInterest) / (Math.pow((one + mInterest), totalMonPay) - 1));
        System.out.println("Your Monthly interest: " + mInterMoney);
        totalPay = mInterMoneyNonCurF * totalMonPay;
        System.out.println("Total payable amount for " + years +" Years: "  + currency.format(totalPay));
    }
}
