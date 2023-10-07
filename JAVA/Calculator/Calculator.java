import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.*;
import java.util.Objects;


public class Calculator implements ActionListener, KeyListener {

    char operator;
    double numb1, numb2, result;
    int numb1Count = 0;
    int numb2Count = 0;
    boolean clearTextFieldForNumb2 = false;

    JFrame frame;
    JLabel imageLabel;
    JLabel label;
    JLabel highlightTextLabel;
    JPanel panel;
    JTextField textField;

    Font labelFont = new Font("Arial", Font.BOLD, 22);
    Font textFieldFont = new Font("Arial", Font.BOLD, 40);
    Font buttonFont = new Font("Arial", Font.PLAIN, 20);
    Font functionButtonFont = new Font("Arial", Font.BOLD, 14);
    Font highlightTextLabelFont = new Font("Arial", Font.ITALIC, 15);

    ImageIcon menuIcon = new ImageIcon("src /menu.png");
    ImageIcon windowIcon = new ImageIcon("src/calculator.png");
    ImageIcon standardIcon = new ImageIcon("src/standard.png");

    JButton[] numberButtons = new JButton[10];
    JButton[] functionButtons = new JButton[10];
    String[] functionButtonsLabels = {"+", "-", "x", "/", "%", ".", "=", "DEL", "CLR", "+/-"};

    Calculator() {
        frame = new JFrame("Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(340, 540);
        frame.setLayout(null);
        frame.setIconImage(windowIcon.getImage());
        frame.getContentPane().setBackground(new Color(35, 32, 26));
        frame.setResizable(false);

        imageLabel = new JLabel();
        imageLabel.setBounds(3, 11, 330, 40);
//        Resize the image to fit the label's dimensions
        Image image = menuIcon.getImage();
        int width = 30;
        int height = 30;
        Image scaledMenuImage = image.getScaledInstance(width, height, Image.SCALE_SMOOTH);
//        Create a new ImageIcon with the resized image
        ImageIcon resizedMenuIcon = new ImageIcon(scaledMenuImage);
        imageLabel.setIcon(resizedMenuIcon);
        imageLabel.setForeground(new Color(255, 255, 255));

        label = new JLabel("Standard Calculator");
        label.setBounds(40, 11, 340, 40);
        label.setFont(labelFont);
        label.setForeground(new Color(255, 255, 255));
//        Resize the image to fit the label's dimensions
        Image imageStandard = standardIcon.getImage();
        int widthS = 18;
        int heightS = 18;
        Image scaledImage = imageStandard.getScaledInstance(widthS, heightS, Image.SCALE_SMOOTH);
        ImageIcon resizedIcon = new ImageIcon(scaledImage);
        label.setIcon(resizedIcon);
        label.setHorizontalTextPosition(JLabel.LEFT);
        label.setIconTextGap(42);

        textField = new JTextField();
        textField.setBounds(1, 95, 324, 65);
        textField.setFont(textFieldFont);
        textField.setHorizontalAlignment(SwingConstants.RIGHT);
        textField.setBackground(new Color(36, 32, 26));
        textField.setForeground(Color.WHITE);
        textField.addKeyListener(this);
//        Create the line border
        Border lineBorder = BorderFactory.createLineBorder(new Color(190, 190, 190), 3, true);
//        Create an empty border with padding
        Border paddingBorder = BorderFactory.createEmptyBorder(1, 1, 1, 5);
//        Combine the line border and padding border
        Border compoundBorder = BorderFactory.createCompoundBorder(lineBorder, paddingBorder);
//        Set the compound border on the JTextField
        textField.setBorder(compoundBorder);
        textField.setEditable(false);

        highlightTextLabel = new JLabel("", SwingConstants.RIGHT);
        highlightTextLabel.setBounds(-34, 56, 350, 25);
        highlightTextLabel.setFont(highlightTextLabelFont);
        highlightTextLabel.setForeground(new Color(255, 255, 255));

        panel = new JPanel();
        panel.setBounds(4, 180, 318, 322);
        panel.setLayout(new GridLayout(5, 4, 2, 2));
        panel.setBackground(new Color(35, 32, 26));
        panel.setBorder(BorderFactory.createLineBorder(new Color(35, 32, 26), 2, true));

//        Adding all buttons to panel
        for (int i = 0; i < 10; i++) {
            int tempI= i;
            functionButtons[i] = new JButton(functionButtonsLabels[i]);
            functionButtons[i].addActionListener(this);
            functionButtons[i].setFont(functionButtonFont);
            functionButtons[i].setFocusable(false);
            functionButtons[i].setBackground(new Color(55, 51, 45));
            functionButtons[i].setForeground(Color.WHITE);
            functionButtons[i].setBorder(BorderFactory.createLineBorder(new Color(35, 32, 26), 2, true));
            functionButtons[i].addMouseListener(new MouseAdapter() {

                @Override
                public void mouseEntered(MouseEvent e) {
                    super.mouseEntered(e);
                    functionButtons[tempI].setBackground(new Color(66, 63, 58));
                    functionButtons[6].setBackground(new Color(247, 152, 47));
                }

                @Override
                public void mouseExited(MouseEvent e) {
                    super.mouseExited(e);
                    functionButtons[tempI].setBackground(new Color(55, 51, 45));
                    functionButtons[6].setBackground(new Color(247, 152, 47));
                }
            });
        }

//        Adding all function buttons to label
        for (int i = 0; i < 10; i++) {
            int tempI = i;
            numberButtons[i] = new JButton(String.valueOf(i));
            numberButtons[i].addActionListener(this);
            numberButtons[i].setFont(buttonFont);
            numberButtons[i].setFocusable(false);
            numberButtons[i].setBackground(new Color(66, 63, 58));
            numberButtons[i].setForeground(Color.WHITE);
            numberButtons[i].setBorder(BorderFactory.createLineBorder(new Color(35, 32, 26), 2, true));
            numberButtons[i].addMouseListener(new MouseAdapter() {

                @Override
                public void mouseEntered(MouseEvent e) {
                    super.mouseEntered(e);
                    numberButtons[tempI].setBackground(new Color(58, 54, 48));
                }

                @Override
                public void mouseExited(MouseEvent e) {
                    super.mouseExited(e);
                    numberButtons[tempI].setBackground(new Color(66, 63, 58));
                }
            });
        }

//        Top button layer column
        panel.add(functionButtons[8]);    // CLR button
        panel.add(functionButtons[7]);    // DEL button
        panel.add(functionButtons[4]);    // % button
        functionButtons[3].setFont(new Font("Arial", Font.BOLD, 20));
        panel.add(functionButtons[3]);    // / button

//        Second button layer column
        panel.add(numberButtons[7]);    // 7 button
        panel.add(numberButtons[8]);    // 8 button
        panel.add(numberButtons[9]);    // 9 button
        functionButtons[2].setFont(new Font("Arial", Font.PLAIN, 20));
        panel.add(functionButtons[2]);    // * button

//        Third button layer column
        panel.add(numberButtons[4]);    // 4 button
        panel.add(numberButtons[5]);    // 5 button
        panel.add(numberButtons[6]);    // 6 button
        functionButtons[1].setFont(new Font("Arial", Font.PLAIN, 26));
        panel.add(functionButtons[1]);    // - button

//        Fourth button layer column
        panel.add(numberButtons[1]);    // 1 button
        panel.add(numberButtons[2]);    // 2 button
        panel.add(numberButtons[3]);    // 3 button
        functionButtons[0].setFont(new Font("Arial", Font.PLAIN, 21));
        panel.add(functionButtons[0]);    // + button

//        Fifth button layer column
        panel.add(functionButtons[9]);    // +/- button
        panel.add(numberButtons[0]);    // 0 button
        panel.add(functionButtons[5]);    // . button
        functionButtons[6].setBackground(new Color(247, 152, 47));
        functionButtons[6].setFont(new Font("Arial", Font.PLAIN, 24));
        panel.add(functionButtons[6]);    // = button

        frame.add(imageLabel);
        frame.add(label);
        frame.add(textField);
        frame.add(highlightTextLabel);
        frame.add(panel);
        frame.setVisible(true);
    }


    public static void main(String[] args) {

        Calculator calculator = new Calculator();
    }


    @Override
    public void actionPerformed(ActionEvent e) {

//        Clearing the text-field
        if (e.getSource() == functionButtons[8]) {
            textField.setText("");
            highlightTextLabel.setText("");
        }

//        Deleting last character in text-field
        if (e.getSource() == functionButtons[7]) {
            if (Double.parseDouble(textField.getText()) != result) {  // Checks to not delete the result in text-field
                int textFieldLength = textField.getText().length();
                if (textFieldLength != 0) {
                    textField.setText(textField.getText().substring(0, textFieldLength - 1));
                }
            }
        }
//        Decimal printing in text-field
        if (e.getSource() == functionButtons[5]) {
            String newTextFieldText = textField.getText();
            boolean hasDecimalPart = numb1 % 1.0 != 0.0;  // If numb1 has decimal part greater than .0 than true
            if (!hasDecimalPart) {
                newTextFieldText = newTextFieldText.concat(".0");
            }
            if (Objects.equals(newTextFieldText, String.valueOf(numb1))) { // Checks if decimal '.' is new or behind text, i.e. 3 + .2 =(should be) 3.2, not 3 + .2 = 5
                textField.setText("");
                textField.setText(textField.getText().concat("."));
            } else {
                boolean isDecimal = false;
                String textFieldData = textField.getText();
                for (int i = 0; i < textFieldData.length(); i++) {  // Only 1 Decimal to be present in text-field
                    if (textFieldData.charAt(i) == '.') {
                        isDecimal = true;  // If decimal is present in text-field
                        break;
                    }
                }
                if (!isDecimal)
                    textField.setText(textField.getText().concat("."));
            }
        }
//        Non-Negative and Negative values
        if (e.getSource() == functionButtons[9]) {
            String currentTextField = textField.getText();
            int textFieldLength = textField.getText().length();

            switch (textField.getText().charAt(0)) {
                case '-' -> textField.setText(currentTextField.substring(1, textFieldLength));  // If number is negative, make it positive
                case '0' -> textField.setText(currentTextField);  // If number is zero, do nothing
                default -> textField.setText("-" + currentTextField);  // If number is positive, make it negative
            }
        }
//        Numbers(0-9) printing in text-field
        for (int i = 0; i < 10; i++) {
            if (e.getSource() == numberButtons[i]) {
                String textFieldData = textField.getText();
                if (!textFieldData.isEmpty()) {  // Checks if numbers not already present in text-field
                    if (textField.getText().charAt(0) == '.')  // Checks if number has a decimal before parsing to double
                        textField.setText(textField.getText().concat(String.valueOf(i)));  // Add number after decimal '.'
                    else {
                        if (clearTextFieldForNumb2) {  // Checks if operator has been assigned to perform arithmetic before clearing text-field for numb2
                            textField.setText("");  // Clear Text-field before entering numb2
                            textField.setText(textField.getText().concat(String.valueOf(i)));
                            clearTextFieldForNumb2 = false;
                        } else {
                            textField.setText(textField.getText().concat(String.valueOf(i)));
                        }
                    }
                } else {
                    textField.setText(textField.getText().concat(String.valueOf(i)));  // If no number present, this is first i.e. numb1
                }
            }
        }
//        Arithmetic operation
        if (e.getSource() == functionButtons[0]) {  // Add
            if (textField.getText().isEmpty())     // If text-field empty, don't do anything
                textField.setText("");
            else {
                numb1 = Double.parseDouble(textField.getText());  //  If not, add text to numb1
                operator = '+';
                numb1Count++;  // Count++ to track how many times numb1 has been updated
                clearTextFieldForNumb2 = true;  // To clear text-filed for numb2
                double numb1_DoubleDigit = numb1 - (int) numb1;
                if (numb1_DoubleDigit == 0.0)  // Is decimal part is .0? Then print int
                    highlightTextLabel.setText((int) numb1 + " " + operator);
                else
                    highlightTextLabel.setText(numb1 + " " + operator);
            }
        }
        if (e.getSource() == functionButtons[1]) {  // Sub
            if (textField.getText().isEmpty())
                textField.setText("");
            else {
                numb1 = Double.parseDouble(textField.getText());
                operator = '-';
                numb1Count++;
                clearTextFieldForNumb2 = true;
                double numb1_DoubleDigit = numb1 - (int) numb1;
                if (numb1_DoubleDigit == 0.0)
                    highlightTextLabel.setText((int) numb1 + " " + operator);
                else
                    highlightTextLabel.setText(numb1 + " " + operator);
            }
        }
        if (e.getSource() == functionButtons[2]) {  // Mul
            if (textField.getText().isEmpty())
                textField.setText("");
            else {
                numb1 = Double.parseDouble(textField.getText());
                operator = '*';
                numb1Count++;
                clearTextFieldForNumb2 = true;
                double numb1_DoubleDigit = numb1 - (int) numb1;
                if (numb1_DoubleDigit == 0.0)
                    highlightTextLabel.setText((int) numb1 + " " + operator);
                else
                    highlightTextLabel.setText(numb1 + " " + operator);
            }
        }
        if (e.getSource() == functionButtons[3]) {  // Div
            if (textField.getText().isEmpty())
                textField.setText("");
            else {
                numb1 = Double.parseDouble(textField.getText());
                operator = '/';
                numb1Count++;
                clearTextFieldForNumb2 = true;
                double numb1_DoubleDigit = numb1 - (int) numb1;
                if (numb1_DoubleDigit == 0.0)
                    highlightTextLabel.setText((int) numb1 + " " + operator);
                else
                    highlightTextLabel.setText(numb1 + " " + operator);
            }
        }
        if (e.getSource() == functionButtons[4]) {  // Mod
            if (textField.getText().isEmpty())
                textField.setText("");
            else {
                numb1 = Double.parseDouble(textField.getText());
                operator = '%';
                numb1Count++;
                clearTextFieldForNumb2 = true;
                double numb1_DoubleDigit = numb1 - (int) numb1;
                if (numb1_DoubleDigit == 0.0)
                    highlightTextLabel.setText((int) numb1 + " " + operator);
                else
                    highlightTextLabel.setText(numb1 + " " + operator);
            }
        }
//        Equals function
        if (e.getSource() == functionButtons[6]) {
            if (numb1Count != numb2Count) { // Checks if we have actually entered numb2 again, or numb2 is just repeating itself
                numb2 = Double.parseDouble(textField.getText());
                numb2Count++;  // Counts++ every time value is added to numb2
            }

            switch (operator) {
                case '+' -> result = numb1 + numb2;
                case '-' -> result = numb1 - numb2;
                case '*' -> result = numb1 * numb2;
                case '/' -> result = numb1 / numb2;
                case '%' -> result = numb1 % numb2;
            }
            double numb1_DoubleDigit = numb1 - (int) numb1;
            double numb2_DoubleDigit = numb2 - (int) numb2;
            double result_DoubleDigit = result - (int) result;

//            Check if numb1, numb2, and result have decimal value 0, i.e. ".0" then print int, if not, print double
            if (numb1_DoubleDigit == 0.0 && numb2_DoubleDigit == 0.0 && result_DoubleDigit == 0.0) {
                textField.setText(String.valueOf((int)result));
                highlightTextLabel.setText((int)numb1 + " " + operator + " " + (int)numb2 + " " + "=");
            } else if (numb1_DoubleDigit == 0.0 && numb2_DoubleDigit == 0.0 && result_DoubleDigit != 0.0) {
                textField.setText(String.valueOf(result));
                highlightTextLabel.setText((int)numb1 + " " + operator + " " + (int)numb2 + " " + "=");
            } else if (numb1_DoubleDigit != 0.0 && numb2_DoubleDigit != 0.0 && result_DoubleDigit != 0.0) {
                textField.setText(String.valueOf(result));
                highlightTextLabel.setText(numb1 + " " + operator + " " + numb2 + " " + "=");
            } else if (numb1_DoubleDigit != 0.0 && numb2_DoubleDigit != 0.0 && result_DoubleDigit == 0.0) {
                textField.setText(String.valueOf((int)result));
                highlightTextLabel.setText(numb1 + " " + operator + " " + numb2 + " " + "=");
            } else if (numb1_DoubleDigit == 0.0 && numb2_DoubleDigit != 0.0) {
                textField.setText(String.valueOf(result));
                highlightTextLabel.setText((int)numb1 + " " + operator + " " + numb2 + " " + "=");
            } else if (numb1_DoubleDigit != 0.0 && numb2_DoubleDigit == 0.0) {
                textField.setText(String.valueOf(result));
                highlightTextLabel.setText(numb1 + " " + operator + " " + (int)numb2 + " " + "=");
            }
            numb1 = result;
        }
    }


    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyPressed(KeyEvent e) {
    }

    @Override
    public void keyReleased(KeyEvent e) {

        /* KeyListener function will invoke the ActionPerformed method for same key. Simulate the CLR button action when the escape key is pressed */
        if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
//            functionButtons[HERE] will define which button correspond to which key
            actionPerformed(new ActionEvent(functionButtons[8], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the DEL button action when the Backspace key is pressed
        if (e.getKeyCode() == KeyEvent.VK_BACK_SPACE) {
            actionPerformed(new ActionEvent(functionButtons[7], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the Decimal button action when the decimal key is pressed
        if (e.getKeyCode() == KeyEvent.VK_DECIMAL) {
            actionPerformed(new ActionEvent(functionButtons[7], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the Add button action when the + key is pressed
        if (e.getKeyCode() == KeyEvent.VK_PLUS || e.isShiftDown() && e.getKeyChar() == '+') {
            actionPerformed(new ActionEvent(functionButtons[0], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the Sub button action when the - key is pressed
        if (e.getKeyCode() == KeyEvent.VK_MINUS || e.getKeyCode() == KeyEvent.VK_SUBTRACT) {
            actionPerformed(new ActionEvent(functionButtons[1], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the Mul button action when the * key is pressed
        if (e.getKeyCode() == KeyEvent.VK_ASTERISK) {
            actionPerformed(new ActionEvent(functionButtons[2], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the Div button action when the / key is pressed
        if (e.getKeyCode() == KeyEvent.VK_SLASH) {
            actionPerformed(new ActionEvent(functionButtons[3], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the Modules button action when the % key is pressed
        if (e.isShiftDown() && e.getKeyChar() == '%') {
            actionPerformed(new ActionEvent(functionButtons[4], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the Equal button action when the = key is pressed
        if (e.getKeyCode() == KeyEvent.VK_ENTER) {
            actionPerformed(new ActionEvent(functionButtons[6], ActionEvent.ACTION_PERFORMED, null));
        }

//        Simulate the corresponding number button action when a digit key is pressed
        char keyChar = e.getKeyChar();
        if (Character.isDigit(keyChar)) {
            for (int i = 0; i < 10; i++) {
                if (keyChar == Character.forDigit(i, 10)) {
                    actionPerformed(new ActionEvent(numberButtons[i], ActionEvent.ACTION_PERFORMED, null));
                    break;
                }
            }
        }
    }
}
