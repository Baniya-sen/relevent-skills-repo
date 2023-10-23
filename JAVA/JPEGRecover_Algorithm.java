import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileNotFoundException;

public class JPEGRecover_Algorithm {
    
    private final int BLOCK_SIZE = 512;

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java JPEGRecover_Algorithm IMAGE");
            System.exit(1);
        }
        
        try {
            int count = 0;
            int bytesRead;
            byte[] buffer = new byte[512];
            FileInputStream infile = new FileInputStream(args[0]);
            FileOutputStream outfile = null;

            while ((bytesRead = infile.read(buffer)) != -1) {

                if (bytesRead >= 3 && buffer[0] == (byte) 0xFF && buffer[1] == (byte) 0xD8 && buffer[2] == (byte) 0xFF) {
                    if (outfile != null)
                        outfile.close();
                    String names = String.format("%03d.jpg", count);
                    outfile = new FileOutputStream(names);
                    if (outfile == null)
                        System.out.println("Could not write to .jpg file");
                    count++;
                }

                if (outfile != null)
                    outfile.write(buffer);
            }
            
            infile.close();
            outfile.close();

        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.exit(0);
    }
}