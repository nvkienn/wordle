import java.io.BufferedWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;

class GuessFreq extends HashMap<String, Integer> {}

public class Stats {
    GuessFreq[] guesses;
    private final String outputFile;

    Stats(String outputFile) {
        this.outputFile = outputFile;
        this.guesses = new GuessFreq[] {
            null,
            new GuessFreq(),
            new GuessFreq(),
            new GuessFreq(),
            new GuessFreq(),
            new GuessFreq(),
            new GuessFreq(),
        };
    }

    void recordGuess(String guess, int turn) {
        if (!(2 <= turn && turn <= 6))
            return;
        GuessFreq data = this.guesses[turn];
        data.put(guess, data.getOrDefault(guess, 0) + 1);
    }

    void print() {
        System.out.printf("[2]: %s\n", this.guesses[2].size());
        System.out.printf("[3]: %s\n", this.guesses[3].size());
        System.out.printf("[4]: %s\n", this.guesses[4].size());
        System.out.printf("[5]: %s\n", this.guesses[5].size());
        System.out.printf("[6]: %s\n", this.guesses[6].size());
    }

    void saveToFile() {
        System.err.println("[stats] saving to file...");
        Path output = Paths.get("").toAbsolutePath().resolve(this.outputFile);
        try {
            BufferedWriter bw = Files.newBufferedWriter(output);
            for (int i = 1; i <= 6; i++) {
                bw.write(guesses[i].toString());
                bw.write('\n');
            }
            bw.flush();
            bw.close();
            System.err.println("[stats] done.");
        } catch (Exception e) {
            System.err.println("[stats] something went wrong.");
        }
    }
}
