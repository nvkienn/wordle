from base_game_code import colorize,invalid,ans_generator,colorize_outcome
from solver_code import probability,bits,worst_entropy_all,renewed_ans
import listw
import math
import json

possible_guesses = listw.guesses
ans_list = listw.answers

#user guesses
user_guess_color = []
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
        print ('bits of uncertainty: 11.173')
        print('(qajaq, 1.890)')
        print('(jujus, 2.039)')
        print('(immix, 2.055)')
        print('(xylyl, 2.190)')
        print('(yukky, 2.205)')
    elif (turn == 1 and guess == 'qajaq'):
        ans_left = len(ans_list)
        print ('possible answers:',ans_left)
        print ('bits of uncertainty:',round(math.log(ans_left,2),3))
        print(second_word[str(tuple(outcome))])
    elif (turn == 2 and user_guess == ['qajaq','xylyl']):
        ans_left = len(ans_list)
        print ('possible answers:',ans_left)
        print ('bits of uncertainty:',round(math.log(ans_left,2),3))
        print(third_word[str(tuple(outcome))])
    else:
        ans_left = len(ans_list)
        print ('possible answers:',ans_left)
        print ('bits of uncertainty:',round(math.log(ans_left,2),3))
        a = worst_entropy_all(ans_list,possible_guesses)
        for i in a:
            print(i)
        print ('possible answers:')
        b = worst_entropy_all(ans_list,ans_list)
        for i in b:
            print(i)
                
    #input guess
    guess = input ("Enter guess:")
    #check for validity
    while (invalid(guess)):
        guess = input ("Invalid, enter guess:")
    user_guess.append(guess)
    #generates outcome
    input_outcome = input("Enter outcome:")
    outcome = list(input_outcome.upper())
    while(len(renewed_ans(guess,outcome,ans_list))==0):
        input_outcome = input("Invalid,enter outcome:")
        outcome = list(input_outcome.upper())

    user_guess_color.append(colorize_outcome(guess,outcome))
    for z in user_guess_color:
        print (z)

    print ('probability of outcome is',probability(guess,outcome,ans_list))
    print ('bits of info is',bits(guess,outcome,ans_list))
    ans_list = renewed_ans(guess,outcome,ans_list)
    possible_guesses = renewed_ans(guess,outcome,possible_guesses)

    if (input_outcome.upper() == 'GGGGG'):
        print ('\nYOU GUESSED IT.')
        print ('guesses took:',turn+1)
        break
    print ('\n-----------------------------')


print ('\nEND OF GAME')

