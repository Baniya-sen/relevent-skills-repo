// Finding Max value in an Array using Linear search

import java.util.Scanner;

public class SearchMaxIn_Array {
    
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        int n_Elements = 0;
        
        do {
            System.out.print("Number of Elements: ");
            n_Elements = s.nextInt();
        } while (n_Elements < 1);
        
        final int[] array = new int[n_Elements];
        
        for (int i = 0; i < n_Elements; i++) {
            System.out.print("Element " + i + " : ");
            array[i] = s.nextInt();
        }
        
        System.out.println("The Max value is: " + max(array, n_Elements));
    }
    
    public static int max(int[] array, int n) {
        int highestValue = array[0];

        for (int i = 1; i < n; i++) {
            if (highestValue < array[i]) {
                highestValue = array[i];
            }
        }
        return highestValue;
    }
}