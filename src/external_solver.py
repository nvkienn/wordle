from base_game_code import invalid, ans_generator, colorize_outcome
from solver_code import (
    probability,
    bits,
    all_entropy,
    first_guesses,
    renewed_ans,
    possible_answers,
)
import listw
import math
import json

# selects list of answers
ans_list = listw.answers
guess = ""
outcome = []

# user guesses
user_guess = []

with open("second_word.json", "r") as f:
    data = json.loads(f.read())

# initiating each turn
for turn in range(6):
    print("Guess #" + str(turn + 1))
    # best first guesses
    if turn == 0:
        print("possible answers: 2309")
        print("bits of uncertainty: 11.173")
        first_guesses()
    elif len(ans_list) == 1:
        print("possible answers: 1")
        print("bits of uncertainty: 0")
        print("answer is:", ans_list[0])
    elif turn == 1 and guess == "soare":
        ans_left = len(ans_list)
        print("possible answers:", ans_left)
        print("bits of uncertainty:", round(math.log(ans_left, 2), 3))
        print(data[str(tuple(outcome))])
    else:
        ans_left = len(ans_list)
        print("possible answers:", ans_left)
        print("bits of uncertainty:", round(math.log(ans_left, 2), 3))
        a = all_entropy(ans_list)
        for i in a:
            print(i)
        print("possible answers:")
        b = possible_answers(ans_list)
        for i in b:
            print(i)

    # input guess
    guess = input("Enter guess:")
    # check for validity
    while invalid(guess):
        guess = input("Invalid, enter guess:")
    # generates outcome
    input_outcome = input("Enter outcome:")
    outcome = list(input_outcome.upper())
    while len(renewed_ans(guess, outcome, ans_list)) == 0:
        input_outcome = input("Invalid,enter outcome:")
        outcome = list(input_outcome.upper())

    user_guess.append(colorize_outcome(guess, outcome))
    for z in user_guess:
        print(z)

    print("probability of outcome is", probability(guess, outcome, ans_list))
    print("bits of info is", bits(guess, outcome, ans_list))
    ans_list = renewed_ans(guess, outcome, ans_list)

    if input_outcome.upper() == "GGGGG":
        print("\nYOU GUESSED IT.")
        print("guesses took:", turn + 1)
        break
    print("\n-----------------------------")

print("\nEND OF GAME")
