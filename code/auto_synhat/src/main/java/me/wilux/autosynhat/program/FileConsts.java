package me.wilux.autosynhat.program;

import java.io.File;

public final class FileConsts {
    public static final File outputDir = new File("resourcepacks/Synhat");
    public static final File downloadDir = new File(outputDir, "temp");
    public static final File downloadZipFile = new File(downloadDir, "synhat.zip");
    public static final File permanentStorageFile = new File(outputDir,"properties.json");

}
