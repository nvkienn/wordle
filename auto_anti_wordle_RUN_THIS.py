from base_game_code import colorize, colorize_outcome
from solver_code import renewed_ans, worst_entropy_word
import listw

# generates answer
# ans = ans_generator()


# to be averaged to find the average number of guesses took to solve all answers
number_of_guess = 0

word_count = 0

# running through all answers
for answer in listw.ans:

    word_count += 1

    print("Word #" + str(word_count))

    # user guesses
    user_guess = []

    # selects list of possible_guesses
    ans_list = listw.guess

    # initiating each turn
    for turn in range(100):

        print("Guess #" + str(turn + 1))
        # best first guesses
        if turn == 0:
            # print ('possible answers: 2309')
            # print ('bits of uncertainty: 11.173052457774116')
            # first_guesses()
            guess = "qajaq"
        else:
            # ans_left = len(ans_list)
            # print ('possible answers:',ans_left)
            # print ('bits of uncertainty:',math.log(ans_left,2))
            print(worst_entropy_word(ans_list))
            guess = "input"

        # generates outcome
        outcome = colorize(guess, answer)
        outcome = list(input())
        user_guess.append(colorize_outcome(guess, outcome))
        for z in user_guess:
            print(z)

        # print ('probability of outcome is',probability(guess,outcome,ans_list))
        # print ('bits of info is',bits(guess,outcome,ans_list))
        ans_list = renewed_ans(guess, outcome, ans_list)

        print("\n-----------------------------")

        # if (guess==answer):
        # print ('\nYOU GUESSED IT.')
        # print ('guesses took:',turn+1)
        #    break

    # if (guess!=answer):
    #    print ('You failed.')
    #
    # print ('\nEND OF GAME')
    number_of_guess += turn + 1

with open("anti_wordle_data.txt", "a") as f1:
    f1.write("\n")
    f1.write("(" + str(number_of_guess) + ")")
