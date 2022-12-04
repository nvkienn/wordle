import java.lang.Math;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

/**
 * Represents a guess taken, and the outcomes faced before.
 */
class Guess {
    final String value;
    /** Outcome-Guess pairs. */
    final HashMap<String, Guess> nextGuesses;

    Guess(String value) {
        this.value = value;
        this.nextGuesses = new HashMap<String, Guess>();
    }

    Guess getNext(String outcome) {
        return nextGuesses.get(outcome);
    }

    void add(String outcome, String guess) {
        nextGuesses.put(outcome, new Guess(guess));
    }
}

public class Database {
    private final HashMap<String, HashMap<String, String>> data;
    final List<String> guesses, answers;
    Guess root;

    Database(HashMap<String, HashMap<String, String>> data) {
        this.data = data;
        HashMap<String, String> ansMap = data.values().iterator().next();
        this.guesses = ansMap.keySet().stream().toList();
        this.answers = data.keySet().stream().toList();
        this.root = new Guess("soare");
    }

    void setSeed(String guess) {
        if (this.root.nextGuesses.isEmpty())
            this.root = new Guess(guess);
    }

    String getOutcome(String ans, String guess) {
        return this.data.get(ans).get(guess);
    }

    double entropy(String guess, HashSet<String> ansList) {
        HashMap<String, Integer> outcomes = new HashMap<String, Integer>();
        for (String ans : ansList) {
            String outcome = this.getOutcome(ans, guess);
            outcomes.put(outcome, outcomes.getOrDefault(outcome, 0) + 1);
        }
        final double t = ansList.size();
        return outcomes.values()
            .stream()
            .mapToDouble(x -> x / t * Math.log(t / x) / Math.log(2))
            .sum();
    }

    private boolean isAns(String word) {
        return this.data.containsKey(word);
    }

    String bestCandidate(List<String> candidates) {
        for (String candidate : candidates)
            if (isAns(candidate))
                return candidate;
        return candidates.get(0);
    }

    /**
     * Pick a next guess based on best entropy.
     * If guess that is in answer list is within tolerance, pick it instead.
     */
    String nextGuess(AnsList ansList) {
        ArrayList<String> candidates = new ArrayList<String>();
        double bestInfo = 0.0;
        for (String guess : this.guesses) {
            double info = this.entropy(guess, ansList);
            // cmp < 0 means info < bestInfo
            if (info > bestInfo) {
                candidates.clear();
                candidates.add(guess);
                bestInfo = info;
            } else if (info == bestInfo) {
                candidates.add(guess);
            }
        }
        return bestCandidate(candidates);
    }

    /**
     * Pick a next guess based on best entropy.
     * Use a cached value if possible.
     */
    String nextGuess(AnsList ansList, List<String> path) {
        Guess guess = this.root;
        for (int i = 0, n = path.size(); i < n; i++) {
            String outcome = path.get(i);
            Guess next = guess.getNext(outcome);
            if (next == null) {
                String suggested = nextGuess(ansList);
                guess.add(outcome, suggested);
                return suggested;
            } else
                guess = next;
        }
        return guess.value;
    }
}
