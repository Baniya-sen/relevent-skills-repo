public class WAV_InputStreamManipulation {
    
    public static void main(String[] args) {
        
        if (args.length != 3) {
            System.out.println("Usage: java WAV_InputStreamManipulation input.wav output.wav factor");
            System.exit(1);
        }

        String isDecimal_Factor = args[2];
        if (!isDecimal_Factor.matches("\\d+")) {
            System.out.println("Usage: java WAV_InputStreamManipulation input.wav output.wav factor");
            System.exit(1);
        }
    }
}