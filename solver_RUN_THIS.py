from base_game_code import invalid, ans_generator, colorize_outcome
from solver_code import (
    first_guesses,
    possible_answers,
)
import listw
import math
from database import Database

db = Database(5)

# generates answer
ans = ans_generator()
guess = ""

# selects list of answers
ans_list = listw.ans

# user guesses
user_guess = []

# initiating each turn
for i in range(6):
    print("Guess #" + str(i + 1))
    # best first guesses
    if i == 0:
        print("possible answers: 2309")
        print("bits of uncertainty: 11.173052457774116")
        first_guesses()
    elif len(ans_list) == 1:
        print("possible answers: 1")
        print("bits of uncertainty: 0")
        print("answer is:", ans_list[0])
    else:
        ans_left = len(ans_list)
        print("possible answers:", ans_left)
        print("bits of uncertainty:", math.log(ans_left, 2))
        a = db.all_entropy(ans_list)
        for i in range(5):
            print(a[i])
        # print("possible answers:")
        # b = possible_answers(ans_list)
        # for i in range(5):
        #     try:
        #         print(b[i])
        #     except:
        #         pass

    # input guess
    guess = input("Enter guess:")
    # check for validity
    while invalid(guess):
        guess = input("Invalid, enter guess:")
    # generates outcome
    outcome = db.get_outcome(ans, guess)

    user_guess.append(colorize_outcome(guess, outcome))
    for z in user_guess:
        print(z)

    # print("probability of outcome is", probability(guess, outcome, ans_list))
    # print("bits of info is", bits(guess, outcome, ans_list))
    ans_list = db.reduce_ans_list(guess, outcome, ans_list)

    if guess == ans:
        print("\nYOU GUESSED IT.")
        print("guesses took:", i + 1)
        break
    print("\n-----------------------------")

if guess != ans:
    print("You failed.")

print("\nEND OF GAME")
