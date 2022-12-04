class Timer {
    long start, end;

    static Timer start() {
        return new Timer();
    }

    private Timer() {
        this.start = System.nanoTime();
        this.end = this.start;
    }

    void end() {
        this.end = System.nanoTime();
    }

    long elapsedInMilliseconds() {
        return (this.end - this.start) / 1000000;
    }

    void print(String msg) {
        System.err.printf("%s took %d ms\n", msg, this.elapsedInMilliseconds());
    }
}
