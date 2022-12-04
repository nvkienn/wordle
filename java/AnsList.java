import java.util.HashSet;
import java.util.Iterator;

public class AnsList extends HashSet<String> {
    private final Database db;

    AnsList(Database db) {
        this.db = db;
        this.reset();
    }

    void reset() {
        this.clear();
        this.addAll(db.answers);
    }

    void filter(String guess, String outcome) {
        Iterator<String> ans = this.iterator();
        while (ans.hasNext())
            if (!db.getOutcome(ans.next(), guess).equals(outcome))
                ans.remove();
    }
}
