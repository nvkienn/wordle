import java.util.ArrayList;
import java.util.Iterator;

public class Wordle {
    private static final String FIRST_GUESS = "soare";
    final Database db;
    final AnsList ansList;
    double totalGuesses = 0.0;
    double totalNanoTime = 0.0;
    int done = 0;
    final String firstGuess;

    Wordle() {
        this.db = new Database(Loader.loadDatabase());
        this.ansList = new AnsList(db);
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
            ansList.filter(guess, outcome);
        }

        // ensure that answer is found
        if (!guess.equals(ans))
            throw new Error("Unable to solve [" + ans + "]");

        // timer stuff
        long endTime = System.nanoTime();
        this.totalNanoTime += endTime - startTime;
        System.out.printf("`%s` in %d tries.\n", ans, turn);
        return turn;
    }

    void display(int numAns) {
        double avgGuess = totalGuesses / done;
        double avgTime = totalNanoTime / done / 1000000;
        System.out.printf("[%d/%d] avg.guess = %.3f\n", done, numAns, avgGuess);
        System.out.printf("avg time = %.3fms\n", avgTime);

        double remainingInSeconds = avgTime * (numAns - done) / 1000;
        int seconds = (int)remainingInSeconds % 60;
        int minutes = (int)remainingInSeconds / 60;
        System.out.printf("time remaining: %d min %d sec\n", minutes, seconds);
    }

    /**
     * Main loop for auto-solver.
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
        timer.print("Wordle::auto()");
    }

    static void help(String[] commands) {
        System.err.println("Run with one of these subcommands:");
        for (String command : commands) {
            System.err.printf("  * %s\n", command);
        }
    }

    public static void main(String[] args) {
        String[] commands = new String[] {"auto"};
        if (args.length < 1) {
            help(commands);
            return;
        }
        switch (args[0]) {
            case "auto":
                Wordle wordle = new Wordle();
                wordle.auto();
                break;
            default:
                help(commands);
        }
    }
}
