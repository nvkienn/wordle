from os import path


def lines(file):
    data = []
    with open(file) as f:
        data = f.read().splitlines()
    return data


CWD = path.dirname(path.realpath(__file__))

answers = lines(path.join(CWD, "words/answers.txt"))
guesses = lines(path.join(CWD, "words/guesses.txt"))
