import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Welcome_UI extends ATM_UI {

    protected JFrame welcomeFrame;
    protected final JButton[] screenSButtons = new JButton[4];
    private final String[] screenSButtonName = {"<START", "<<-  A", "<<-  B", "<<EXIT"};
    private final ImageIcon bankImage = new ImageIcon("/bank.png");

    Welcome_ButtonListen welcomeButtonListen;

    Welcome_UI() {
        initializeLoginUI();
        welcomeButtonListen = new Welcome_ButtonListen(this);
        screenSButtons[0].addActionListener(welcomeButtonListen);
        screenSButtons[0].addKeyListener(welcomeButtonListen);
    }

    protected void initializeLoginUI() {
        welcomeFrame = new JFrame();
        welcomeFrame.setTitle("ATM");
        welcomeFrame.setResizable(false);
        welcomeFrame.setSize(1000, 720);
        welcomeFrame.setLayout(null);
        welcomeFrame.setIconImage(super.titleIcon.getImage());
        welcomeFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        JLabel backgroundLabel = createBackgroundImage();
        JPanel screenPanel = createScreenPanel();
        JLabel screenImageLabel = createScreenImageLabel();
        JPanel screenButtonPanel = createScreenButtonPanel();
        JPanel numberFunctionButtonPadPanel = createFunctionButtonPadPanel();
        JPanel buttonPadPanel = createNumberButtonPadPanel();
        JPanel buttonPanel = createButtonPanel();
        JPanel SmallSidePanel = createSmallSidePanel();

        welcomeFrame.add(screenImageLabel);
        welcomeFrame.add(screenPanel);
        welcomeFrame.add(screenButtonPanel);
        welcomeFrame.add(numberFunctionButtonPadPanel);
        welcomeFrame.add(buttonPadPanel);
        welcomeFrame.add(SmallSidePanel);
        welcomeFrame.add(buttonPanel);
        welcomeFrame.add(backgroundLabel);
        welcomeFrame.setLocationRelativeTo(null);
        welcomeFrame.setVisible(true);
    }

    public JLabel createScreenImageLabel() {
        screenBankImage = new JLabel();
        screenBankImage.setBounds(157, 88, 430, 370);
        ImageIcon resizedImage = resizeIcon(bankImage, 430, 370);
        screenBankImage.setIcon(resizedImage);
        Border screenBorder = BorderFactory.createLineBorder(Color.GRAY, 2, true);
        screenBankImage.setBorder(screenBorder);
        return screenBankImage;

    }

    @Override
    public JPanel createScreenButtonPanel() {
        JPanel screenButtonPanel = new JPanel();
        screenButtonPanel.setBounds(600, 270, 70, 189);
        screenButtonPanel.setBackground(new Color(174, 174, 174));
        screenButtonPanel.setLayout(new GridLayout(4, 1, 1, 2));
        screenButtonPanel.setBorder(BorderFactory.createLineBorder(new Color(124, 124 , 124), 4, true));
        initializeButtons(screenButtonPanel, 4, screenSButtons, screenButtonName, new Color(220, 175, 90), Color.WHITE, new Color(150, 115, 42));
        return screenButtonPanel;
    }

    @Override
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

    @Override
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

    @Override
    public void initializeButtons(JPanel panel, int count, JButton[] buttons, String[] buttonNames, Color buttonColor, Color foreGround, Color mouseEntered) {
        for (int i = 0; i < count; i++) {
            buttons[i] = new JButton(buttonNames[i]);
            buttons[i].setActionCommand(null);
            buttons[i].setBackground(new Color(84, 94, 94));
            buttons[i].setEnabled(false);
            screenSButtons[0].setEnabled(true);
            screenSButtons[0].setBackground(new Color(220, 175, 90));
            buttons[i].setFocusable(true);
            buttons[i].setFocusPainted(false);
            buttons[i].setForeground(foreGround);
            buttons[i].setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2, true));
            screenSButtons[0].addActionListener(welcomeButtonListen);
            screenSButtons[0].addKeyListener(welcomeButtonListen);
            int finalI = 0;
            screenSButtons[0].addMouseListener(new MouseAdapter() {
                @Override
                public void mouseEntered(MouseEvent e) {
                    super.mouseEntered(e);
                    screenSButtons[finalI].setBackground(new Color(150, 115, 42));
                }

                @Override
                public void mouseExited(MouseEvent e) {
                    super.mouseExited(e);
                    screenSButtons[finalI].setBackground(new Color(220, 175, 90));
                }
            });
            panel.add(buttons[i]);
        }
    }
}
