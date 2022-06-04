def counter(lst):
    d = {}
    for i in lst:
        d[i] = d.get(i, 0) + 1
    return d

# target return
# ['G', 'B', 'Y', 'Y', 'G']
def colorize(guess, answer):
    if len(guess) != 5 or len(answer) != 5:
        return ["B"] * 5

    d_answer = counter(answer)
    d_guess = counter(guess)

    result = ['B'] * 5

    # scan for Gs
    for index, letter in enumerate(guess):
        correct_letter = answer[index]
        if (letter is correct_letter):
            result[index] = 'G'
            d_answer[letter] -= 1
            d_guess[letter] -= 1

    # scan for Ys
    for index, letter in enumerate(guess):
        if d_answer.get(letter, 0) > 0:
            result[index] = 'Y'

    return result
