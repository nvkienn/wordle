from colors import colors
import random
import listw


# counting number of letters in the word
def counter(lst):
    d = {}
    for i in lst:
        d[i] = d.get(i, 0) + 1
    return d


# checks validity of guess
def invalid(guess):
    for i in listw.guesses:
        if guess == i:
            return False
    return True


# generates answer
def ans_generator():
    p = random.randint(0, 2309)
    ans = listw.answers[p]
    return ans


# generates outcome
def colorize(guess, answer):
    d_answer = counter(answer)
    d_guess = counter(guess)

    # sets default as Black
    result = ["B"] * 5

    # scan for Greens
    for index, letter in enumerate(guess):
        correct_letter = answer[index]
        if letter is correct_letter:
            result[index] = "G"
            d_answer[letter] -= 1
            d_guess[letter] -= 1

    # scan for Ys
    for index, letter in enumerate(guess):
        if d_answer.get(letter, 0) > 0:
            if result[index] != "G":
                result[index] = "Y"
                d_answer[letter] -= 1
                d_guess[letter] -= 1
    return result


def colorize_outcome(guess, result):
    outcome = ""
    for c, i in enumerate(result):
        if i == "G":
            outcome += (
                colors.BGGREEN
                + colors.BLACK
                + " "
                + guess[c].upper()
                + " "
                + colors.ENDC
            )
        elif i == "Y":
            outcome += (
                colors.BGYELLOW
                + colors.BLACK
                + " "
                + guess[c].upper()
                + " "
                + colors.ENDC
            )
        else:
            outcome += colors.BGGREY + " " + guess[c].upper() + " " + colors.ENDC
    return outcome
