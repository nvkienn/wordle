import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.lang.Math;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

class Guess {
    String word;
    double info;

    Guess(String word, double info) {
        this.word = word;
        this.info = info;
    }

    Guess copy() {
        return new Guess(this.word, this.info);
    }
}

class Database {
    private final HashMap<String, HashMap<String, String>> data;
    final List<String> guesses, answers;

    Database(HashMap<String, HashMap<String, String>> data) {
        this.data = data;
        HashMap<String, String> ansMap = data.values().iterator().next();
        this.guesses = ansMap.keySet().stream().toList();
        this.answers = data.keySet().stream().toList();
    }

    String getOutcome(String ans, String guess) {
        return this.data.get(ans).get(guess);
    }

    double entropy(String guess, HashSet<String> ansList) {
        HashMap<String, Integer> outcomes = new HashMap<String, Integer>();
        double entropy = 0;
        for (String ans : ansList) {
            String outcome = this.getOutcome(ans, guess);
            outcomes.put(outcome, outcomes.getOrDefault(outcome, 0) + 1);
        }
        double len = ansList.size();
        for (double val : outcomes.values()) {
            if (val > 0)
                entropy += val / len * Math.log(len / val) / Math.log(2);
        }
        return entropy;
    }

    private boolean isAns(String word) {
        return this.data.containsKey(word);
    }

    /**
     * Pick a next guess based on best entropy.
     * If guess that is in answer list is within tolerance, pick it instead.
     */
    String nextGuess(HashSet<String> ansList) {
        Guess best = new Guess("not-ans", 0);
        Guess ans = new Guess("ans", 0);
        double tolerance = 0.00001;
        for (String guess : this.guesses) {
            double info = this.entropy(guess, ansList);
            if (info > best.info) {
                best = new Guess(guess, info);
                if (isAns(guess)) {
                    ans = best;
                }
            }
        }
        return (best.info - ans.info < tolerance ? ans : best).word;
    }
}

public class Wordle extends Debug {
    final Database db;
    final HashSet<String> masterAnswerSet;
    double totalGuesses = 0.0;
    double totalTimeInMilliseconds = 0.0;
    int done = 0;

    HashMap<String, String> readFile(File file) {
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
            printf("File not found: %s\n", file);
        }
        return data;
    }

    /** removes elements from set that don't have same outcome */
    void filterAnsList(String guess, HashSet<String> ansList, String outcome) {
        Iterator<String> iter = ansList.iterator();
        while (iter.hasNext()) {
            String ans = iter.next();
            if (!db.getOutcome(ans, guess).equals(outcome)) {
                iter.remove();
            }
        }
    }

    HashSet<String> freshAnsList() {
        return new HashSet<String>(this.masterAnswerSet);
    }

    int solve(String ans) {
        String guess;
        HashSet<String> ansList = freshAnsList();
        int turn = 0;
        long startTime = System.nanoTime();
        for (turn = 0; turn < 6; turn++) {
            if (turn == 0) {
                guess = "soare";
            } else if (ansList.size() == 1) {
                guess = ansList.stream().findFirst().get();
            } else {
                guess = db.nextGuess(ansList);
            }
            String outcome = db.getOutcome(ans, guess);
            filterAnsList(guess, ansList, outcome);
            if (guess.equals(ans))
                break;
        }
        long endTime = System.nanoTime();
        printf("[solved] `%s` in %d tries.\n", ans, turn);
        long mills = (endTime - startTime) / 1000000;
        this.totalTimeInMilliseconds += mills;
        println("That took " + mills + " milliseconds");
        return turn;
    }

    void display(int numAns) {
        printf("[%d/%d] avg = %.3f\n", done, numAns, totalGuesses / (done + 1));
        double avgTime = this.totalTimeInMilliseconds / done;
        printf("avg time = %.3f\n", avgTime);
        double remainingInSeconds = avgTime * (numAns - done) / 1000;
        int seconds = (int)remainingInSeconds % 60;
        int minutes = (int)remainingInSeconds / 60;
        printf("time remaining: %d min %d sec\n", minutes, seconds);
    }

    void solve() {
        List<String> allPossibleAns = this.db.answers;
        int numAns = allPossibleAns.size();
        Iterator<String> iter = allPossibleAns.iterator();
        while (iter.hasNext()) {
            String ans = iter.next();
            double tries = solve(ans);
            this.totalGuesses += tries;
            display(numAns);
        }
    }

    Wordle() {
        this.db = new Database(Loader.loadDatabase());
        this.masterAnswerSet = new HashSet<String>();
    }

    void main() {
        println("MAIN");
        solve();
    }

    public static void main(String[] args) {
        new Wordle().main();
    }
}
