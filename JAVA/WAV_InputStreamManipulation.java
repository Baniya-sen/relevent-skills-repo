import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class WAV_InputStreamManipulation {
    
    public static void main(String[] args) {
        
        String isDecimal = args[2];
        float factor = Float.parseFloat(isDecimal);

        if (args.length != 3) {
            System.out.println("Usage: java WAV_InputStreamManipulation input.wav output.wav factor");
            System.exit(1);
        } else if (!isDecimal.matches("\\d+")) {
            System.out.println("Usage: java WAV_InputStreamManipulation input.wav output.wav factor");
            System.exit(1);
        }

        try {
            FileInputStream input_stream = new FileInputStream(args[0]);
            FileOutputStream output_stream = new FileOutputStream(args[1]);

            byte[] header = new byte[44];
            int bytesRead = input_stream.read(header);

            if (bytesRead != -1) {
                output_stream.write(header);
            } else {
                System.out.println("End of input stream reached.");
            }

            int samplesRead;
            byte[] buffer = new byte[1];

            while ((samplesRead = input_stream.read(buffer)) != -1) {
                buffer[0] *= factor;
                output_stream.write(buffer);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        System.exit(0);
    }
}