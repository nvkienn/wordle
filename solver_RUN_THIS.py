from base_game_code import colorize,invalid,ans_generator
from solver_wordle_code import probability,bits
from outcomes_all import possible_outcomes
import listw
import math

#generates answer
ans = ans_generator()
ans = 'abyss'
print (ans)

#initiating each turn 
for i in range (6):

    #input guess
    guess = input ("Enter guess:")
    #check for validity
    while (invalid(guess)):
        guess = input ("Invalid, enter guess:")
    #generates outcome
    outcome = colorize (guess,ans)

    print (outcome)
    probability = probability(guess,outcome)
    print ('probability of outcome is',probability)
    print ('bits of info is',info[1])

    if (guess==ans):
        print ('YOU GUESSED IT')
        break

if (guess!=ans):
    print ('You failed.')

