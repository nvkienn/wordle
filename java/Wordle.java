import java.lang.Math;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

class GuessFreq extends HashMap<String, Integer> {}

class Stats {
    GuessFreq[] guesses;

    Stats() {
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
        if (turn < 0 || turn >= this.guesses.length)
            return;
        GuessFreq data = this.guesses[turn];
        data.put(guess, data.getOrDefault(guess, 0) + 1);
    }

    void print() {
        System.out.printf("[1]: %s\n", this.guesses[1].size());
        System.out.printf("[2]: %s\n", this.guesses[2].size());
        System.out.printf("[3]: %s\n", this.guesses[3].size());
        System.out.printf("[4]: %s\n", this.guesses[4].size());
        System.out.printf("[5]: %s\n", this.guesses[5].size());
        System.out.printf("[6]: %s\n", this.guesses[6].size());
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
        ArrayList<String> candidates = new ArrayList<String>();
        double bestInfo = 0.0;
        for (String guess : this.guesses) {
            double info = this.entropy(guess, ansList);
            // cmp < 0 means info < bestInfo
            int cmp = Double.compare(info, bestInfo);
            if (cmp > 0) {
                candidates.clear();
                candidates.add(guess);
                bestInfo = info;
            } else if (cmp == 0) {
                candidates.add(guess);
            }
        }
        for (String candidate : candidates)
            if (isAns(candidate)) {
                return candidate;
            }

        return candidates.get(0);
    }
}

public class Wordle extends Debug {
    final Database db;
    final HashSet<String> masterAnswerSet;
    final Stats stats = new Stats();
    double totalGuesses = 0.0;
    double totalTimeInMilliseconds = 0.0;
    int done = 0;

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
        int turn = 1;
        long startTime = System.nanoTime();
        for (turn = 1; turn <= 6; turn++) {
            if (turn == 1) {
                guess = "soare";
            } else if (ansList.size() == 1) {
                guess = ansList.stream().findFirst().get();
            } else {
                guess = db.nextGuess(ansList);
            }
            if (turn > 1) {
                stats.recordGuess(guess, turn);
            }
            String outcome = db.getOutcome(ans, guess);
            filterAnsList(guess, ansList, outcome);
            if (guess.equals(ans))
                break;
            if (turn == 6)
                throw new Error("Unable to solve [" + ans + "]");
        }
        long endTime = System.nanoTime();
        printf("[solved] `%s` in %d tries.\n", ans, turn);
        long mills = (endTime - startTime) / 1000000;
        this.totalTimeInMilliseconds += mills;
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
        this.stats.print();
    }

    void solve() {
        List<String> allPossibleAns = this.db.answers;
        int numAns = allPossibleAns.size();
        Iterator<String> ans = allPossibleAns.iterator();
        while (ans.hasNext()) {
            double tries = solve(ans.next());
            this.totalGuesses += tries;
            this.done++;
            display(numAns);
        }
    }

    Wordle() {
        this.db = new Database(Loader.loadDatabase());
        this.masterAnswerSet = new HashSet<String>(this.db.answers);
    }

    void main() {
        println("MAIN");
        solve();
    }

    public static void main(String[] args) {
        new Wordle().main();
    }
}
