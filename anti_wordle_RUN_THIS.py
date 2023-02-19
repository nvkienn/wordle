from base_game_code import colorize,invalid,ans_generator,colorize_outcome
from solver_code import probability,bits,entropy,worst_all_entropy,first_guesses,renewed_ans,possible_answers
from outcomes_all import possible_outcomes
from colors import colors
import listw
import math

#generates answer
ans = ans_generator()

#selects list of answers
ans_list = listw.ans

#user guesses
user_guess = []

#initiating each turn 
for turn in range (100):

    print ('Guess #'+str(turn+1))
    #best first guesses
    if (turn == 0):
        print ('possible answers: 2309')
        print ('bits of uncertainty: 11.173052457774116')
        print('qajaq', 1.8901929060587057)
        print('jujus', 2.0394702600664427)
        print('immix', 2.0553250345034906)
        print('xylyl', 2.1896376350793587)
        print('yukky', 2.2053433495356694)
    elif (len(ans_list)==1):
        print ('possible answers: 1')
        print ('bits of uncertainty: 0')
        print ('answer is:',ans_list[0])
    else:
        ans_left = len(ans_list)
        print ('possible answers:',ans_left)
        print ('bits of uncertainty:',math.log(ans_left,2))
        a = worst_all_entropy(ans_list)
        for i in range (5):
            print (a[i])
                
    #input guess
    guess = input ("Enter guess:")
    #check for validity
    while (invalid(guess)):
        guess = input ("Invalid, enter guess:")
    #generates outcome
    outcome = colorize (guess,ans)


    user_guess.append(colorize_outcome(guess,outcome))
    for z in user_guess:
        print (z)

    print ('probability of outcome is',probability(guess,outcome,ans_list))
    print ('bits of info is',bits(guess,outcome,ans_list))
    ans_list = renewed_ans(guess,outcome,ans_list)

    if (guess==ans):
        print ('\nYOU GUESSED IT.')
        print ('guesses took:',turn+1)
        break
    print ('\n-----------------------------')


print ('\nEND OF GAME')

