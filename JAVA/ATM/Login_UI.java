import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.text.NumberFormat;
import java.util.Locale;
import java.util.Timer;
import java.util.TimerTask;

public class Login_UI {

    private double currentAccountBalance = 400000;
    private double savingAccountBalance = 1000000;
    private boolean currentAccountSelected = false;
    private boolean isDeposit = false;

    protected enum State {
        START,
        ACCOUNT_TYPE,
        TRANSACTION_TYPE,
        EXIT
    }
    protected State currentState = State.START;

    protected JLabel pinPromptLabel;
    protected JTextField pinTextField;
    protected JButton pinEnterButton;
    protected JLabel accountTypePrompt;
    protected JLabel showAccountBalance;
    protected JLabel showAccountCurrency;
    protected JTextField userMoneyInputTextField;

    private final Font pinPromptFont = new Font("Arial", Font.BOLD, 40);
    private final Font pinTextFieldFont = new Font("Arial", Font.BOLD, 35);
    private final Font pinSubmitButtonFont = new Font("Arial", Font.BOLD, 18);
    private final Font accountBalanceFont = new Font("Arial", Font.BOLD, 25);
    private final Font accountCurrenyFont = new Font("Arial", Font.ITALIC, 20);
    private final Font operatingChoisesFont = new Font("Arial", Font.BOLD, 15);

    private final Timer timer = new Timer();
    private final NumberFormat formatCurrency = NumberFormat.getCurrencyInstance((new Locale("hi", "IN")));

    Login_UI() {
    }

    protected JLabel createPinPromptLabel() {
        pinPromptLabel = new JLabel("Enter PIN");
        pinPromptLabel.setBounds(136, 120, 200, 50);
        pinPromptLabel.setForeground(Color.WHITE);
        pinPromptLabel.setFont(pinPromptFont);
        return pinPromptLabel;
    }

    protected JTextField createPinTextField() {
        pinTextField = new JTextField();
        pinTextField.setBounds(179, 190, 95, 45);
        pinTextField.setFont(pinTextFieldFont);
        pinTextField.setBackground(new Color(170, 190, 190));
        pinTextField.setHorizontalAlignment(SwingConstants.RIGHT);
        Border roundBorder = BorderFactory.createLineBorder(Color.white, 6, true);
        pinTextField.setBorder(roundBorder);
        pinTextField.setEditable(false);
        return pinTextField;
    }

    protected JButton createPinButton() {
        pinEnterButton = new JButton("Submit");
        pinEnterButton.setBackground(Color.white);
        pinEnterButton.setFocusable(false);
        pinEnterButton.setBounds(187, 250, 80, 30);
        pinEnterButton.setFont(pinSubmitButtonFont);
        Border roundBorder = BorderFactory.createLineBorder(Color.white, 6, true);
        pinEnterButton.setBorder(roundBorder);
        return pinEnterButton;
    }

    protected JLabel createAccountBalance() {
        showAccountBalance = new JLabel("Account Balance:");
        showAccountBalance.setBounds(125, 60, 250, 60);
        showAccountBalance.setFont(accountBalanceFont);
        showAccountBalance.setForeground(Color.white);
        showAccountBalance.setVisible(false);
        return showAccountBalance;
    }

    protected JLabel createAccountCurrency() {
        showAccountCurrency = new JLabel();
        showAccountCurrency.setBounds(160, 95, 250, 60);
        showAccountCurrency.setFont(accountCurrenyFont);
        showAccountCurrency.setForeground(Color.white);
        return showAccountCurrency;
    }

    protected JLabel createAccountTypePrompt() {
        accountTypePrompt =  new JLabel();
        accountTypePrompt.setFont(operatingChoisesFont);
        accountTypePrompt.setForeground(Color.white);
        accountTypePrompt.setBounds(150, 164, 300, 180);
        return accountTypePrompt;
    }

    protected JTextField createUserMoneyInputTextField() {
        userMoneyInputTextField = new JTextField();
        userMoneyInputTextField.setBounds(125, 140, 200, 40);
        userMoneyInputTextField.setFont(pinTextFieldFont);
        userMoneyInputTextField.setBackground(new Color(170, 190, 190));
        userMoneyInputTextField.setHorizontalAlignment(SwingConstants.RIGHT);
        Border roundBorder = BorderFactory.createLineBorder(Color.white, 6, true);
        userMoneyInputTextField.setBorder(roundBorder);
        userMoneyInputTextField.setEditable(false);
        userMoneyInputTextField.setVisible(false);
        return userMoneyInputTextField;

    }

    protected void handleButtonA() {
        switch (currentState) {
            case START -> {
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        currentState = State.ACCOUNT_TYPE;
                        showAccountCurrency.setText("Select A or B");
                        accountTypePrompt.setText("<html><div align='right'>Select your preferred Account type: <br><br><br> Click A - Current Account <br><br> Click B - Saving Account </div></html>");
                    }
                }, 1200);
            }
            case ACCOUNT_TYPE -> {
                currentState = State.TRANSACTION_TYPE;
                currentAccountSelected = true;
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        showAccountCurrency.setText(formatCurrency.format(currentAccountBalance));
                        accountTypePrompt.setText("<html><div align='right'>Select preferred $ Transaction type: <br><br><br> Click A - Deposit Money <br><br> Click B - Withdraw Money </div></html>");
                    }
                }, 500);
            }
            case TRANSACTION_TYPE -> {
                currentState = State.EXIT;
                isDeposit = true;
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        accountTypePrompt.setText("<html><div align='right'>Enter the amount u likely to deposit: <br><br><br> Click A - Enter <br><br> Click B - Cancel </div></html>");
                        if (currentAccountSelected) {
                            showAccountCurrency.setText(formatCurrency.format(currentAccountBalance));
                        }
                        else {
                            showAccountCurrency.setText(formatCurrency.format(savingAccountBalance));
                        }
                    }
                }, 500);
            }
            case EXIT -> {
                currentState = State.START;
                createUserMoneyInputTextField();
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        if (currentAccountSelected)
                            if (isDeposit)
                                showAccountCurrency.setText(formatCurrency.format(currentAccountBalance += Double.parseDouble(userMoneyInputTextField.getText())));
                            else
                                showAccountCurrency.setText(formatCurrency.format(currentAccountBalance -= Double.parseDouble(userMoneyInputTextField.getText())));
                        else
                            if (isDeposit)
                                showAccountCurrency.setText(formatCurrency.format(savingAccountBalance += Double.parseDouble(userMoneyInputTextField.getText())));
                            else
                                showAccountCurrency.setText(formatCurrency.format(savingAccountBalance -= Double.parseDouble(userMoneyInputTextField.getText())));
                        accountTypePrompt.setText("<html><div align='right'> Your request has been submitted! </div></html>");
                    }
                }, 900);
            }
        }
    }

    protected void handleButtonB() {
        switch (currentState) {
            case START -> {
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        currentState = State.ACCOUNT_TYPE;
                        showAccountCurrency.setText("Select A or B");
                        accountTypePrompt.setText("<html><div align='right'>Select your preferred Account type: <br><br><br> Click A - Current Account <br><br> Click B - Saving Account </div></html>");
                    }
                }, 1200);
            }
            case ACCOUNT_TYPE -> {
                currentState = State.TRANSACTION_TYPE;
                currentAccountSelected = false;
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        showAccountCurrency.setText(formatCurrency.format(savingAccountBalance));
                        accountTypePrompt.setText("<html><div align='right'>Select preferred $ Transaction type: <br><br><br> Click A - Deposit Money <br><br> Click B - Withdraw Money </div></html>");
                    }
                }, 500);
            }
            case TRANSACTION_TYPE -> {
                currentState = State.EXIT;
                isDeposit = false;
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        accountTypePrompt.setText("<html><div align='right'>Enter the amount likely to withdraw: <br><br><br> Click A - Enter <br><br> Click B - Cancel </div></html>");
                        if (currentAccountSelected) {
                            showAccountCurrency.setText(formatCurrency.format(currentAccountBalance));
                        }
                        else {
                            showAccountCurrency.setText(formatCurrency.format(savingAccountBalance));
                        }
                    }
                }, 500);
            }
            case EXIT -> {
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        currentState = State.ACCOUNT_TYPE;
                    }
                }, 500);
            }
        }
    }
}
