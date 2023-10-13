import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.*;

public class ATM_UI {

    protected JFrame frame;
    protected JPanel screenPanel;
    protected JLabel screenBankImage;
    protected JPanel screenButtonPanel;
    protected JLabel enterPin;
    protected JTextField pinText;
    protected JButton pinSubmitButton;
    protected JTextField amountText;

    protected final ImageIcon titleIcon = new ImageIcon("/atm_icon.png");
    private final ImageIcon atmIcon = new ImageIcon("/atm.png");

    protected final JButton[] screenButtons = new JButton[4];
    protected final String[] screenButtonName = {"<START", "<<-  A", "<<-  B", "<<EXIT"};
    protected final JButton[] functionButtons = new JButton[4];
    protected final String[] functionButtonName = {"CLEAR", "DELETE", "CANCEL", "ENTER"};
    protected final JButton[] numberButtons = new JButton[12];
    protected final String[] numberButtonNames = {"7", "8", "9", "4", "5", "6", "1", "2", "3", "", "0", "."};

    private ATM_ButtonListeners buttonListener;
    private final Login_UI login_ui = new Login_UI();

    protected  ATM_UI () {
    }

    protected ATM_UI(String initData) {
        initializeUI();
        buttonListener = new ATM_ButtonListeners(this, login_ui);
        for (JButton button : screenButtons) {
            button.addActionListener(buttonListener);
            button.addKeyListener(buttonListener);
        }
        for (JButton button : functionButtons) {
            button.addActionListener(buttonListener);
            button.addKeyListener(buttonListener);
        }
        for (JButton button : numberButtons) {
            button.addActionListener(buttonListener);
            button.addKeyListener(buttonListener);
        }
        pinSubmitButton.addActionListener(buttonListener);
    }

    private void initializeUI() {
        frame = new JFrame();
        frame.setTitle("ATM");
        frame.setResizable(false);
        frame.setSize(1000, 720);
        frame.setLayout(null);
        frame.setIconImage(titleIcon.getImage());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel backgroundLabel = createBackgroundImage();
        JPanel screenPanel = createScreenPanel();
        JPanel screenButtonPanel = createScreenButtonPanel();
        JPanel numberFunctionButtonPadPanel = createFunctionButtonPadPanel();
        JPanel buttonPadPanel = createNumberButtonPadPanel();
        JPanel buttonPanel = createButtonPanel();
        JPanel SmallSidePanel = createSmallSidePanel();

        frame.add(screenPanel);
        frame.add(screenButtonPanel);
        frame.add(numberFunctionButtonPadPanel);
        frame.add(buttonPadPanel);
        frame.add(SmallSidePanel);
        frame.add(buttonPanel);
        frame.add(backgroundLabel);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ATM_UI("Data"));
    }

    public JLabel createBackgroundImage() {
        JLabel backgroundLabel = new JLabel();
        backgroundLabel.setBounds(0, -50, 1000, 800);
        ImageIcon resizedImage = resizeIcon(atmIcon, 1000, 700);
        backgroundLabel.setIcon(resizedImage);
        return backgroundLabel;
    }

    public JPanel createScreenPanel() {
        screenPanel = new JPanel();
        screenPanel.setBounds(152, 82, 440, 380);
        screenPanel.setBackground(new Color(0, 70, 125));
        Border screenBorder = BorderFactory.createLineBorder(Color.DARK_GRAY, 8, true);
        screenPanel.setBorder(screenBorder);
        screenPanel.setLayout(null);

//        Imported methods from Login-UI class
        screenPanel.add(login_ui.createPinPromptLabel());
        screenPanel.add(login_ui.createPinTextField());
        screenPanel.add(login_ui.createPinButton());
        screenPanel.add(login_ui.createAccountTypePrompt());
        screenPanel.add(login_ui.createUserMoneyInputTextField());

        enterPin = login_ui.pinPromptLabel;
        pinText = login_ui.pinTextField;
        pinSubmitButton = login_ui.pinEnterButton;
        pinSubmitButton.addActionListener(buttonListener);
        amountText = login_ui.userMoneyInputTextField;
        screenPanel.setVisible(false);
        return screenPanel;
    }

    public JPanel createScreenButtonPanel() {
        screenButtonPanel = new JPanel();
        screenButtonPanel.setBounds(600, 270, 70, 189);
        screenButtonPanel.setBackground(new Color(174, 174, 174));
        screenButtonPanel.setLayout(new GridLayout(4, 1, 1, 2));
        screenButtonPanel.setBorder(BorderFactory.createLineBorder(new Color(124, 124 , 124), 4, true));
        initializeButtons(screenButtonPanel, 4, screenButtons, screenButtonName, new Color(220, 175, 90), Color.WHITE, new Color(150, 115, 42));
        return screenButtonPanel;
    }

    public JPanel createButtonPanel() {
        JPanel buttonPanel = new JPanel();
        buttonPanel.setBounds(68, 480, 635, 210);
        buttonPanel.setBackground(new Color(94, 94, 94));
        Border borderPadding = BorderFactory.createLineBorder(new Color(84, 94, 94), 5, true);
        buttonPanel.setBorder(borderPadding);
        return buttonPanel;
    }

    public JPanel createNumberButtonPadPanel() {
        JPanel buttonPadPanel = new JPanel();
        buttonPadPanel.setBounds(160, 490, 426, 188);
        buttonPadPanel.setBackground(new Color(145, 145, 145));
        buttonPadPanel.setLayout(new GridLayout(4, 1, 10, 10));
        Border borderStroke = BorderFactory.createLineBorder(new Color(84, 94, 94), 5, true);
        Border borderPadding = BorderFactory.createEmptyBorder(4, 4, 4, 150);
        Border compoundBorder = BorderFactory.createCompoundBorder(borderStroke, borderPadding);
        buttonPadPanel.setBorder(compoundBorder);
        initializeButtons(buttonPadPanel, 12, numberButtons, numberButtonNames, new Color(145, 155, 155), new Color(40, 40, 30), new Color(90, 99, 99));
        return buttonPadPanel;
    }

    public JPanel createFunctionButtonPadPanel() {
        JPanel functionButtonPadPanel = new JPanel();
        functionButtonPadPanel.setBounds(460, 496, 120, 178);
        functionButtonPadPanel.setBackground(new Color(145, 145, 145));
        functionButtonPadPanel.setLayout(new GridLayout(4, 1, 10, 10));
        Border borderPadding = BorderFactory.createEmptyBorder(4, 4, 4, 5);
        functionButtonPadPanel.setBorder(borderPadding);
        initializeButtons(functionButtonPadPanel, 4, functionButtons, functionButtonName, new Color(145, 155, 155), new Color(40, 40, 30), new Color(90, 99, 99));
        return functionButtonPadPanel;
    }

    public void initializeButtons(JPanel panel, int count, JButton[] buttons, String[] buttonNames, Color buttonColor, Color foreGround, Color mouseEntered) {
        for (int i = 0; i < count; i++) {
            buttons[i] = new JButton(buttonNames[i]);
            buttons[i].setActionCommand(null);
            buttons[i].setBackground(buttonColor);
            buttons[i].setFocusable(true);
            buttons[i].setFocusPainted(false);
            buttons[i].setForeground(foreGround);
            buttons[i].setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2, true));
            buttons[i].addActionListener(buttonListener);
            buttons[i].addKeyListener(buttonListener);
            screenButtons[0].setEnabled(false);
            screenButtons[0].setBackground(new Color(94, 94, 94));
            int finalI = i;
            buttons[i].addMouseListener(new MouseAdapter() {
                @Override
                public void mouseEntered(MouseEvent e) {
                    super.mouseEntered(e);
                    buttons[finalI].setBackground(mouseEntered);
                    screenButtons[0].setBackground(new Color(94, 94, 94));
                }

                @Override
                public void mouseExited(MouseEvent e) {
                    super.mouseExited(e);
                    buttons[finalI].setBackground(buttonColor);
                    screenButtons[0].setBackground(new Color(94, 94, 94));
                }
            });
            panel.add(buttons[i]);
        }
    }

    public JPanel createSmallSidePanel() {
        JPanel sideSmallPanel = new JPanel();
        sideSmallPanel.setBounds(815, 591, 78, 76);
        sideSmallPanel.setBackground(Color.black);
        return sideSmallPanel;
    }

    public ImageIcon resizeIcon(ImageIcon icon, int width, int height) {
        Image image = icon.getImage();
        Image scaledImage = image.getScaledInstance(width, height, Image.SCALE_SMOOTH);
        return new ImageIcon(scaledImage);
    }
}
