package me.wilux.autosynhat.program;

import me.wilux.autosynhat.program.logger.WindowHandler;

import javax.swing.*;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.logging.Level;
import java.util.logging.LogRecord;
import java.util.logging.Logger;

public class Main {
    public static boolean argNoLog = false;
    public static boolean argPromptDownload = false;
    public static boolean argNoWarn = false;
    public static boolean startedByAgent = false;

    public static PermaFile propertyFile;

    public static WindowHandler windowHandler = null;
    public static Logger logger = null;

    public static void main(String[] args) {

        //Reformat javaagent arguments to normal arguments
        if(args.length>0 && args[0].startsWith("agentArgs")){
            args = (args[0].split("="))[1].split(",");
            startedByAgent = true;
        }

        for (String s: args){
            if (s.equals("noLog")) argNoLog = true;
            if (s.equals("promptDownload")) argPromptDownload = true;
            if (s.equals("noWarn")) argNoWarn = true;
        }

        windowHandler = WindowHandler.getInstance();
        windowHandler.publishString("AutoSynhat Starting with Args ="+ String.join(" ",args));
        if(!startedByAgent){
            windowHandler.publishString("AutoSynhat Started Directly");
        }


        try {
            propertyFile = new PermaFile(FileConsts.permanentStorageFile);
        } catch (IOException e) {
            windowHandler.publish(new LogRecord(Level.WARNING,"Can not read property file"+e));
            exitSevere(e);
        }

        try {
            if (GithubDownloader.isOutdated()) {
                windowHandler.publishString("A new version is available, downloading automatically");
                String versionName = GithubDownloader.downloadLatestZip();
                GithubDownloader.unzip();
                windowHandler.publishString(versionName+" Downloaded Successfully");
                exitDownloadSuccess();
            } else {
                exitNoUpdate();
            }
        } catch (IOException e) {
            windowHandler.publish(new LogRecord(Level.WARNING,"Unable to access github"+e));
            exitCantDownload();
        }
    }

    public static void exitDownloadSuccess(){

        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                Window.basicMsgBox("New synhat version "+
                        propertyFile.content.get(PermaFile.installedPackName)+
                        " successfully installed!\n If minecraft loaded before this dialog popped up you might need to reload assets using F3+T"
                );
                System.exit(0);
            }
        });
    }

    public static void exitNoUpdate() {
        windowHandler.publishString("No updated needed, this window will close in 3 seconds");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {e.printStackTrace();}
        System.exit(0);
    }
    public static void exitCantDownload(){
        if(argNoWarn == true){
            System.exit(0);
        }

        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                Window.basicMsgBox("Unable to access the synhat online files, Exiting"+
                        "\n If you don't want this popup in the future add \"noWarn\" to the synhat.jar arguments in JVM arguments (-javaagent:synhat.jar=noWarn)"+
                        "\n This window will automatically close in 10 seconds"
                );
            }
        });

        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {e.printStackTrace();}

        System.exit(0);
    }
    public static void exitSevere(Exception e){
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                StringWriter sw = new StringWriter();
                PrintWriter pw = new PrintWriter(sw);
                e.printStackTrace(pw);

                Window.basicMsgBox("Catastophic failure. Please report this to Wilux" +
                        "\nThis window must be closed manually" +
                        "\n" + e.getMessage() +
                        "\n" + sw.toString()
                );
            }
        });
    }
}

