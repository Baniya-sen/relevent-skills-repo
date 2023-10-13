import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Timer;
import java.util.TimerTask;

public class Welcome_ButtonListen implements ActionListener, KeyListener {

    Welcome_UI welcome_ui;

    Welcome_ButtonListen(Welcome_UI welcome_ui) {
        this.welcome_ui = welcome_ui;
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == welcome_ui.screenSButtons[0]) {
            Timer timer = new Timer();
            timer.schedule(new TimerTask() {
                @Override
                public void run() {
                    ATM_UI atmUi = new ATM_UI("Initializer");
                    timer.schedule(new TimerTask() {
                        @Override
                        public void run() {
                            atmUi.screenPanel.setVisible(true);
                        }
                    }, 1000);
                }
            }, 1000);
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
        if (e.getKeyCode() == 65) {
            actionPerformed(new ActionEvent(welcome_ui.screenSButtons[0], ActionEvent.ACTION_PERFORMED, null));
        }
    }
}
