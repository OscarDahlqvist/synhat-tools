package me.wilux.autosynhat.program.logger;

import java.util.Formatter;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.LogRecord;

public class WindowHandler extends Handler {
    private LogWindow window = null;

    private Formatter formatter = null;

    private Level level = null;

    private static WindowHandler handler = null;

    private WindowHandler() {
        LogManager manager = LogManager.getLogManager();
        String className = this.getClass().getName();
        String level = manager.getProperty(className + ".level");
        setLevel(level != null ? Level.parse(level) : Level.INFO);
        if (window == null)
            window = new LogWindow();
    }

    public static synchronized WindowHandler getInstance() {
        if (handler == null) {
            handler = new WindowHandler();
        }
        return handler;
    }

    public synchronized void publish(LogRecord record) {
        String message = null;
        if (!isLoggable(record))
            return;
        message = getFormatter().format(record);
        window.showInfo(message);
    }

    public synchronized void publishString(String message) {
        window.showInfo(message+"\n");
    }

    public void close() {
    }

    public void flush() {
    }
}

