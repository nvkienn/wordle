from base_game_code import colorize,invalid,ans_generator
from solver_code import probability,bits,entropy,all_entropy,first_guesses,renewed_ans
from outcomes_all import possible_outcomes
from colors import colors
import listw
import math

#generates answer
ans = ans_generator()
ans = 'abyss'
print (ans)

#initiating each turn 
for i in range (6):

    print (colors.WHITE + 'Guess #'+str(i+1))
    #best first guesses
    if (i == 0):
        first_guesses()
        ans_list = listw.guess
    else:
        ans_list = renewed_ans(guess,outcome,ans_list)
        all_entropy(ans_list)
    #input guess
    guess = input ("Enter guess:")
    #check for validity
    while (invalid(guess)):
        guess = input ("Invalid, enter guess:")
    #generates outcome
    outcome = colorize (guess,ans)
    print (outcome)

    print ('probability of outcome is',probability(guess,outcome,ans_list))
    print ('bits of info is',bits(guess,outcome,ans_list))

    if (guess==ans):
        print ('YOU GUESSED IT')
        break
    print ('\n-----------------------------\n')

if (guess!=ans):
    print ('You failed.')

print ('END OF GAME')

