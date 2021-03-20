package manager;

import jdk.nashorn.internal.scripts.JO;

import javax.swing.*;

import static javax.swing.JOptionPane.showMessageDialog;
public class Window {
    public static void msgBox(String message){
        JOptionPane.showMessageDialog(
                null,
                "<html><body><p style='width: 200px;'>"+message+"</p></body></html>",
                "Message",
                JOptionPane.INFORMATION_MESSAGE);
    }

    public static void basicMsgBox(String message){
        JOptionPane.showMessageDialog(null, message);
    }

    public static boolean yesNoQuery(String message, String title){
        int dialogResult = JOptionPane.showConfirmDialog(null, message, title, JOptionPane.YES_NO_OPTION);
        return (dialogResult == JOptionPane.YES_OPTION);
    }
}
