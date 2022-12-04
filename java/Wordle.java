import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Wordle {
    private static final String FIRST_GUESS = "soare";
    final Database db;
    final Stats stats = new Stats("stats.txt");
    final AnsList ansList;
    double totalGuesses = 0.0;
    double totalNanoTime = 0.0;
    int done = 0;
    final String firstGuess;
    final PrintWriter io;

    Wordle() {
        this.db = new Database(Loader.loadDatabase());
        this.ansList = new AnsList(db);
        this.io = new PrintWriter(System.out);
        if (FIRST_GUESS.isEmpty()) {
            System.out.println("generating first guess...");
            this.firstGuess = db.nextGuess(ansList);
            System.out.printf("first guess is `%s`\n", this.firstGuess);
        } else {
            this.firstGuess = FIRST_GUESS;
        }
        db.setSeed(firstGuess);
    }

    int solve(String ans) {
        String guess = "";
        int turn = 0;
        long startTime = System.nanoTime();
        ansList.reset();
        ArrayList<String> path = new ArrayList<String>();

        for (turn = 0; guess != ans; turn++) {
            if (turn == 0) {
                guess = firstGuess;
            } else if (ansList.size() == 1) {
                guess = ansList.stream().findFirst().get();
            } else {
                guess = db.nextGuess(ansList, path);
            }
            String outcome = db.getOutcome(ans, guess);
            path.add(outcome);
            stats.recordGuess(guess, turn);
            ansList.filter(guess, outcome);
        }

        // ensure that answer is found
        if (!guess.equals(ans))
            throw new Error("Unable to solve [" + ans + "]");

        // timer stuff
        long endTime = System.nanoTime();
        this.totalNanoTime += endTime - startTime;

        io.printf("`%s` in %d tries.\n", ans, turn);
        return turn;
    }

    int interval = 10;

    void display(int numAns) {
        io.printf("[%d/%d] avg.guess = %.3f\n", done, numAns,
                  totalGuesses / done);
        double avgTime = this.totalNanoTime / done / 1000000;
        io.printf("avg time = %.3fms\n", avgTime);
        double remainingInSeconds = avgTime * (numAns - done) / 1000;
        int seconds = (int)remainingInSeconds % 60;
        int minutes = (int)remainingInSeconds / 60;
        io.printf("time remaining: %d min %d sec\n", minutes, seconds);
        if (done % interval == 0)
            io.flush();
    }

    /**
     * Solves against every possible answer and tracks results.
     */
    void auto() {
        Timer timer = Timer.start();
        int numAns = this.db.answers.size();
        Iterator<String> ans = this.db.answers.iterator();
        while (ans.hasNext()) {
            this.totalGuesses += solve(ans.next());
            this.done++;
            display(numAns);
        }
        timer.end();
        io.flush();
        this.stats.saveToFile();
        timer.print("Wordle::auto()");
        this.stats.print();
        io.close();
    }

    /**
     * Solves against queried answers.
     */
    void auto(List<String> solveList) {
        List<String> allPossibleAns = this.db.answers;
        int numAns = allPossibleAns.size();
        for (String ans : solveList) {
            this.totalGuesses += solve(ans);
            if (done++ % 100 == 0)
                this.stats.saveToFile();
            display(numAns);
        }
    }

    /**
     * For running any benchmarks.
     */
    void bench() {
        Timer timer = Timer.start();
        timer.end();
        timer.print("That");
    }

    public static void main(String[] args) {
        if (args.length < 1)
            System.err.println("Run with `auto` or `bench` as argument.");
        Wordle wordle = new Wordle();
        switch (args[0]) {
            case "auto":
                wordle.auto();
                break;
            case "bench":
                wordle.bench();
                break;
            default:
                System.err.println("Run with `auto` or `bench` as argument.");
        }
    }
}
