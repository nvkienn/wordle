import os
from outcomes_all import generate_all_outcomes
import listw
import math

__dirname__ = os.path.dirname(os.path.realpath(__file__))
db_dir = os.path.join(__dirname__, "data")

from math import log

outcomes_dict = generate_all_outcomes()


def clear(d):
    for k in d.keys():
        d[k] = 0


class Database:
    data = {}
    size = 0
    word_len = 0

    def __init__(self, word_len):
        self.data = {}
        self.word_len = word_len

    def get(self, ans) -> dict[str, str]:
        if ans in self.data:
            return self.data[ans]
        else:
            return self.retrieve(ans)

    def get_outcome(self, ans: str, guess: str) -> str:
        return self.get(ans)[guess]

    def retrieve(self, ans):
        with open(os.path.join(db_dir, ans)) as f:
            mem = {}
            for line in f.read().splitlines():
                guess, outcome = line[: self.word_len], line[self.word_len :]
                mem[guess] = outcome
        self.data[ans] = mem
        self.size += 1
        if self.size % 200 == 0:
            print("fresh read", self.size)
        return self.data[ans]

    def reduce_ans_list(
        self, guess: str, outcome: str, ans_list: list[str]
    ) -> list[str]:
        renewed_list = []
        for ans in ans_list:
            if outcome == self.get_outcome(ans, guess):
                renewed_list.append(ans)
        return renewed_list

    def entropy(self, guess: str, ans_list: list[str]):
        # sum(probability * log2(1/p))
        clear(outcomes_dict)
        entropy = 0
        for ans in ans_list:
            outcome = self.get_outcome(ans, guess)
            outcomes_dict[outcome] += 1
        ans_len = len(ans_list)
        for i in outcomes_dict.values():
            if i != 0:
                entropy += i / ans_len * log(ans_len / i, 2)
        return entropy

    def all_entropy(self, ans_list: list[str]):
        d_entropy = {}
        for i in listw.guess:
            a = self.entropy(i, ans_list)
            d_entropy[i] = a
        sort_entropy = sorted(d_entropy.items(), key=lambda x: x[1], reverse=True)
        return sort_entropy

    def best_entropy(self, ans_list: list[str]):
        best_guess = ("ans", 0)
        # count = 0
        for guess in listw.guess:
            info = self.entropy(guess, ans_list)
            if info > best_guess[1]:
                best_guess = (guess, info)
        return best_guess

    def possible_answers(self, ans_list: list[str]):
        d_entropy = {}
        for i in ans_list:
            a = self.entropy(i, ans_list)
            d_entropy[i] = a
        sort_entropy = sorted(d_entropy.items(), key=lambda x: x[1], reverse=True)
        return sort_entropy

    def read_all(self):
        for ans in listw.ans:
            self.retrieve(ans)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
        # return "Point({}, {})".format(self.x, self.y)


t = (1, 4)
p = Point(1, 4)
print(p.distance_from_origin())
print(p.x)
