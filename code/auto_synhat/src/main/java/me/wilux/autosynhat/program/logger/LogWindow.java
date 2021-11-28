package me.wilux.autosynhat.program.logger;
import me.wilux.autosynhat.program.Main;

import java.util.logging.*;
import javax.swing.*;

/** YOINKED CODE
 * http://www.java2s.com/Code/Java/Language-Basics/JavalogLogandWindowJFrameframe.htm
 */
public class LogWindow extends JFrame {
    private int width;

    private int height;

    private JTextArea textArea = null;

    private JScrollPane pane = null;

    public LogWindow(String title, int width, int height) {
        super(title);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        setSize(width, height);
        textArea = new JTextArea();
        pane = new JScrollPane(textArea);
        getContentPane().add(pane);

        java.net.URL imageURL = Thread.currentThread().getContextClassLoader().getResource("icon.png"); //access jar root
        System.out.println(imageURL.toString());
        ImageIcon icon = new ImageIcon(imageURL);
        setIconImage(icon.getImage());

        setVisible(true);
    }

    public static LogRecord logError(Level lvl, String s, Exception e){
        e.printStackTrace();
        return new LogRecord(lvl, s+"\n"+e.getMessage());
    }

    /**
     * This method appends the data to the text area.
     *
     * @param data
     *            the Logging information data
     */
    public void showInfo(String data) {
        textArea.append(data);
        this.getContentPane().validate();
    }
}


