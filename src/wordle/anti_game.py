from base_game_code import colorize, invalid, ans_generator, colorize_outcome
from solver_code import renewed_ans
import listw

# generates answer
ans = ans_generator()
guess = ""

possible_guesses = listw.guesses

# initiating each turn
for i in range(100):
    # input guess
    guess = input("Enter guess:")
    # check for validity
    while guess not in possible_guesses:
        guess = input("Invalid, enter guess:")
    # generates outcome
    outcome = colorize(guess, ans)
    possible_guesses = renewed_ans(guess, outcome, possible_guesses)

    print(colorize_outcome(guess, outcome))
    if guess == ans:
        print("YOU GUESSED IT")
        break

if guess != ans:
    print("You failed.")
