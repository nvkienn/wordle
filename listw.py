def lines(file):
    data = []
    with open(file) as f:
        data = f.read().splitlines()
    return data

answers = lines("./words/answers.txt")
guesses = lines("./words/guesses.txt")
