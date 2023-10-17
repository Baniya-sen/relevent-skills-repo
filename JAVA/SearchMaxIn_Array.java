public class SearchMaxIn_Array {
    
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        
        do {
            System.out.println("Number of Elements: ");
            final int n_Elements = s.nextInt();
        } while (n_Elements < 1);
        
        final int[] array = new int[n_Elements];
        
        for (int i = 0; i < n_Elements; i++) {
            System.out.println("Element " + i + " : ");
            array[i] = s.nextInt();
        }
        
        System.out.println("The Max value is: " + max(array, n_Elements));
    }
    
    public static int max(int[] array, int n) {
    }
}