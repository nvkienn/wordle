import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.nio.file.Paths;
import java.util.HashMap;

public class Loader {
    static HashMap<String, String> readFile(File file) {
        HashMap<String, String> data = new HashMap<String, String>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            reader.lines().forEach(line -> {
                String guess = line.substring(0, 5);
                String outcome = line.substring(5);
                data.put(guess, outcome);
            });
            reader.close();
        } catch (Exception e) {
            System.err.printf("File not found: %s\n", file);
        }
        return data;
    }

    static File[] getDataFiles() {
        File dataFolder =
            Paths.get("").toAbsolutePath().getParent().resolve("data").toFile();
        return dataFolder.listFiles();
    }

    static HashMap<String, HashMap<String, String>> loadDatabase() {
        File[] dataFiles = getDataFiles();
        HashMap<String, HashMap<String, String>> db =
            new HashMap<String, HashMap<String, String>>(dataFiles.length);
        for (int i = 0; i < dataFiles.length; i++) {
            if (i % 200 == 0) {
                System.err.printf("read file: %d/%d\n", i, dataFiles.length);
            }
            File dataFile = dataFiles[i];
            String ans = dataFile.getName();
            HashMap<String, String> ansDict = readFile(dataFiles[i]);
            db.put(ans, ansDict);
        }
        return db;
    }
}
