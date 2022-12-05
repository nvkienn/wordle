import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;

/**
 * Loads a directory containing data files into a two layer dictionary.
 * {
 *   [ans]: {
 *     [guess]: "outcome",
 *     ...
 *   },
 *   ...
 * }
 */
public class Loader {
    /**
     * Reads a file containing 10-character lines.
     * Filename is the answer.
     * First 5 characters is the guess.
     * Last 5 characters is the outcome of taking that guess.
     */
    private static HashMap<String, String> readFile(File file) {
        HashMap<String, String> data = new HashMap<String, String>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            reader.lines().forEach(line -> {
                String guess = line.substring(0, 5);
                String outcome = line.substring(5);
                data.put(guess, outcome);
            });
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.printf("File not found: %s\n", file);
        } catch (IOException e) {
            System.out.printf("Error reading file: %s\n", file);
        }
        return data;
    }

    /**
     * Gets the path to the data file directory.
     * hard-coded to take ../data/ relative to this java code file.
     */
    private static Path getDataDir() {
        Path currentDir = Paths.get("").toAbsolutePath();
        return currentDir.getParent().resolve("data");
    }

    static HashMap<String, HashMap<String, String>> loadDatabase() {
        File[] dataFiles = getDataDir().toFile().listFiles();
        HashMap<String, HashMap<String, String>> database =
            new HashMap<String, HashMap<String, String>>(dataFiles.length);
        System.out.printf("Reading %d files", dataFiles.length);
        for (int i = 0; i < dataFiles.length; i++) {
            if (i % 200 == 0)
                System.out.print('.');
            File dataFile = dataFiles[i];
            String ans = dataFile.getName();
            HashMap<String, String> ansDict = readFile(dataFiles[i]);
            database.put(ans, ansDict);
        }
        System.out.print("done!\n");
        return database;
    }
}
