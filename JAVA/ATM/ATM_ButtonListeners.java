import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Objects;
import java.util.Timer;
import java.util.TimerTask;

public class ATM_ButtonListeners implements ActionListener, KeyListener {

    ATM_UI atmUi;
    Login_UI login_ui;
    Timer timer = new Timer();
    boolean isSubmit = false;

    private final int pinNumberLength = 4;

    ATM_ButtonListeners(ATM_UI atmUi, Login_UI login_ui) {
        this.atmUi = atmUi;
        this.login_ui = login_ui;
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == atmUi.screenButtons[3]) {
            timer.schedule(new TimerTask() {
                @Override
                public void run() {
                    atmUi.frame.dispose();
                    System.exit(0);
                }
            }, 900);
        }

        if (e.getSource() == atmUi.screenButtons[1]) {
            if (isSubmit) {
                if (login_ui.currentState == Login_UI.State.EXIT && Objects.equals(atmUi.amountText.getText(), "") || Objects.equals(atmUi.amountText.getText(), "0") || atmUi.amountText.getText().length() > 7) {
                    atmUi.amountText.setText("");
                    JOptionPane.showMessageDialog(atmUi.screenPanel, "Please enter a validate amount.", "Alert", JOptionPane.INFORMATION_MESSAGE);
                } else {
                    login_ui.handleButtonA();
                    timer.schedule(new TimerTask() {
                        @Override
                        public void run() {
                            atmUi.amountText.setVisible(login_ui.currentState == Login_UI.State.EXIT);
                            login_ui.createPinTextField();
                            if (!Objects.equals(atmUi.amountText.getText(), ""))
                                login_ui.userMoneyInputTextField.setText(atmUi.amountText.getText());
                        }
                    }, 500);
                }
            }
            if (login_ui.currentState == Login_UI.State.TRANSACTION_TYPE) {
                atmUi.amountText.setText("");
            }
        }

        if (e.getSource() == atmUi.screenButtons[2]) {
            atmUi.amountText.setText("");
            if (isSubmit) {
                login_ui.handleButtonB();
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        atmUi.amountText.setVisible(login_ui.currentState == Login_UI.State.EXIT);
                        if (login_ui.currentState == Login_UI.State.ACCOUNT_TYPE) {
                            login_ui.currentState = Login_UI.State.START;
                            login_ui.handleButtonA();
                            atmUi.screenPanel.setVisible(false);
                            timer.schedule(new TimerTask() {
                                @Override
                                public void run() {
                                    atmUi.screenPanel.setVisible(true);
                                }
                            }, 500);
                        }
                    }
                }, 500);
            }
        }

        if (e.getSource() == atmUi.pinSubmitButton) {
            int pinTextFieldLength = atmUi.pinText.getText().length();
            if (pinTextFieldLength == pinNumberLength) {
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        atmUi.pinText.setText("");
                        timer.schedule(new TimerTask() {
                            @Override
                            public void run() {
                                atmUi.enterPin.setVisible(false);
                                atmUi.pinText.setVisible(false);
                                atmUi.pinSubmitButton.setVisible(false);
                                timer.schedule(new TimerTask() {
                                    @Override
                                    public void run() {
                                        atmUi.screenPanel.add(login_ui.createAccountBalance());
                                        login_ui.showAccountBalance.setVisible(true);
                                        atmUi.screenPanel.add(login_ui.createAccountCurrency());
                                        atmUi.screenPanel.add(login_ui.createAccountTypePrompt());
                                        login_ui.handleButtonA();
                                    }
                                }, 50);
                            }
                        }, 50);
                    }
                }, 700);
                isSubmit = true;
            } else {
                atmUi.pinText.setText("");
                JOptionPane.showMessageDialog(atmUi.screenPanel, "Please enter correct pin.", "Alert", JOptionPane.INFORMATION_MESSAGE);
            }
        }

        for (int i = 0; i < 11; i++) {
            if (e.getSource() == atmUi.numberButtons[i]) {
                int pinTextFieldLength = atmUi.pinText.getText().length();
                if (pinTextFieldLength < pinNumberLength)
                    atmUi.pinText.setText(atmUi.pinText.getText().concat(atmUi.numberButtonNames[i]));
                if (isSubmit) {
                    if (login_ui.currentState == Login_UI.State.EXIT) {
                        int accountTextLength = atmUi.amountText.getText().length();
                        if (accountTextLength < pinNumberLength + 2)
                            atmUi.amountText.setText(atmUi.amountText.getText().concat(atmUi.numberButtonNames[i]));
                    }
                }
            }
        }

        if (e.getSource() == atmUi.numberButtons[11]) {
            if (isSubmit) {
                boolean isDecimal = false;
                int accountTextLength = atmUi.amountText.getText().length();
                for (int i = 0; i < accountTextLength; i++) {
                    if (atmUi.amountText.getText().charAt(i) == '.') {
                        isDecimal = true;
                    }
                }
                if (!isDecimal)
                    atmUi.amountText.setText(atmUi.amountText.getText().concat("."));
            }
        }

        if (e.getSource() == atmUi.functionButtons[0]) {
            if (!isSubmit)
                atmUi.pinText.setText("");
            else atmUi.amountText.setText("");
        }

        if (e.getSource() == atmUi.functionButtons[1]) {
            if (!isSubmit) {
                int pinTextLength = atmUi.pinText.getText().length();
                if (pinTextLength != 0)
                    atmUi.pinText.setText(atmUi.pinText.getText().substring(0, pinTextLength - 1));
            } else {
                int amountTextLength = atmUi.amountText.getText().length();
                if (amountTextLength != 0)
                    atmUi.amountText.setText(atmUi.amountText.getText().substring(0, amountTextLength - 1));
            }
        }

        if (e.getSource() == atmUi.functionButtons[2]) {
            if (isSubmit) {
                login_ui.currentState = Login_UI.State.START;
                atmUi.amountText.setText("");
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        atmUi.amountText.setVisible(false);
                    }
                }, 300);
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        atmUi.screenPanel.setVisible(false);
                        login_ui.handleButtonA();
                    }
                }, 500);
                timer.schedule(new TimerTask() {
                    @Override
                    public void run() {
                        atmUi.screenPanel.setVisible(true);
                    }
                }, 1500);
            }
            else
                atmUi.pinText.setText("");
        }

        if (e.getSource() == atmUi.functionButtons[3]) {
            if (!isSubmit)
                actionPerformed(new ActionEvent(atmUi.pinSubmitButton, ActionEvent.ACTION_PERFORMED, null));
            else {
                if (login_ui.currentState == Login_UI.State.EXIT || login_ui.currentState == Login_UI.State.START)
                    actionPerformed(new ActionEvent(atmUi.screenButtons[1], ActionEvent.ACTION_PERFORMED, null));
            }
        }
    }

    @Override
    public void keyTyped (KeyEvent e){
    }

    @Override
    public void keyPressed (KeyEvent e){
    }

    @Override
    public void keyReleased (KeyEvent e){

        final int letterAKeycode = 65;
        if (e.getKeyCode() == letterAKeycode) {
            actionPerformed(new ActionEvent(atmUi.screenButtons[1], ActionEvent.ACTION_PERFORMED, null));
        }

        final int letterBKeycode = 66;
        if (e.getKeyCode() == letterBKeycode) {
            actionPerformed(new ActionEvent(atmUi.screenButtons[2], ActionEvent.ACTION_PERFORMED, null));
        }

        if (e.getKeyCode() == KeyEvent.VK_DELETE) {
            actionPerformed(new ActionEvent(atmUi.functionButtons[0], ActionEvent.ACTION_PERFORMED, null));
        }

        if (e.getKeyCode() == KeyEvent.VK_BACK_SPACE) {
            actionPerformed(new ActionEvent(atmUi.functionButtons[1], ActionEvent.ACTION_PERFORMED, null));
        }

        if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
            actionPerformed(new ActionEvent(atmUi.functionButtons[2], ActionEvent.ACTION_PERFORMED, null));
        }

        if (e.getKeyCode() == KeyEvent.VK_ENTER) {
            actionPerformed(new ActionEvent(atmUi.functionButtons[3], ActionEvent.ACTION_PERFORMED, null));
        }

        char keyChar = e.getKeyChar();
        if (Character.isDigit(keyChar)) {
            for (int i = 0; i < 11; i++) {
                if (String.valueOf(keyChar).equals(atmUi.numberButtonNames[i])) {
                    if (!isSubmit) {
                        int pinTextFieldLength = atmUi.pinText.getText().length();
                        if (pinTextFieldLength < pinNumberLength)
                            atmUi.pinText.setText(atmUi.pinText.getText().concat(atmUi.numberButtonNames[i]));
                    }
                    else {
                        if (login_ui.currentState == Login_UI.State.EXIT) {
                            int amountTextLength = atmUi.amountText.getText().length();
                            if (amountTextLength < pinNumberLength + 2)
                                atmUi.amountText.setText(atmUi.amountText.getText().concat(atmUi.numberButtonNames[i]));
                        }
                    }
                }
            }
        }
    }
}

