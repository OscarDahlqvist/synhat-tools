package me.wilux.autosynhat.program.logger;

import javax.swing.*;

class LogWindow extends JFrame {
    private JTextArea textArea = new JTextArea();

    public LogWindow() {
        super("");
        setSize(400, 200);
        add(new JScrollPane(textArea));

        java.net.URL imageURL = Thread.currentThread().getContextClassLoader().getResource("icon.png"); //access jar root
        System.out.println(imageURL.toString());
        ImageIcon icon = new ImageIcon(imageURL);
        setIconImage(icon.getImage());

        setVisible(true);
    }

    public void showInfo(String data) {
        textArea.append(data);
        this.validate();
    }
}
