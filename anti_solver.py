from base_game_code import colorize,invalid,ans_generator,colorize_outcome
from solver_code import probability,bits,worst_entropy_all,renewed_ans
import listw
import math
import json

#generates answer
ans = ans_generator()

possible_guesses = listw.guess
ans_list = listw.ans

#user guesses
user_guess = []
guess = ''
outcome = []

with open ('anti_second_word.json','r') as f:
    second_word = json.loads(f.read())
with open ('anti_third_word.json','r') as f:
    third_word = json.loads(f.read())

#initiating each turn 
for turn in range (100):

    print ('Guess #'+str(turn+1))
    #best first guesses
    if (turn == 0):
        print ('possible answers: 2309')
        print ('bits of uncertainty: 11.173052457774116')
        print('(qajaq, 1.8901929060587057)')
        print('(jujus, 2.0394702600664427)')
        print('(immix, 2.0553250345034906)')
        print('(xylyl, 2.1896376350793587)')
        print('(yukky, 2.2053433495356694)')
    elif (turn == 1):
        ans_left = len(ans_list)
        print ('possible answers:',ans_left)
        print ('bits of uncertainty:',math.log(ans_left,2))
        print(second_word[str(tuple(outcome))])
    elif (turn == 2 and guess == 'xylyl'):
        ans_left = len(ans_list)
        print ('possible answers:',ans_left)
        print ('bits of uncertainty:',math.log(ans_left,2))
        print(third_word[str(tuple(outcome))])
    else:
        ans_left = len(ans_list)
        print ('possible answers:',ans_left)
        print ('bits of uncertainty:',math.log(ans_left,2))
        a = worst_entropy_all(ans_list,possible_guesses)
        for i in range (5):
            try:
                print (a[i])
            except:
                pass
        print ('possible answers:')
        b = worst_entropy_all(ans_list,ans_list)
        for i in range (5):
            try:
                print (b[i])
            except:
                pass
                
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
    possible_guesses = renewed_ans(guess,outcome,possible_guesses)

    if (guess==ans):
        print ('\nYOU GUESSED IT.')
        print ('guesses took:',turn+1)
        break
    print ('\n-----------------------------')


print ('\nEND OF GAME')

