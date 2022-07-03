from base_game_code import colorize,invalid,ans_generator,colorize_outcome
from solver_code import probability,bits,entropy,all_entropy,first_guesses,renewed_ans, best_entropy
from outcomes_all import possible_outcomes
from colors import colors
import listw
import math

#generates answer
#ans = ans_generator()



#to be averaged to find the average number of guesses took to solve all answers
number_of_guess = 0


#running through all answers
for answer in listw.ans:

    print ('Word #'+str(answer+1))

    #user guesses
    user_guess = []

    #selects list of answers
    ans_list = listw.ans

    #initiating each turn 
    for turn in range (6):
    
        print ('Guess #'+str(turn+1))
        #best first guesses
        if (turn == 0):
            #print ('possible answers: 2309')
            #print ('bits of uncertainty: 11.173052457774116')
            #first_guesses()
            guess = 'soare'
        elif (len(ans_list)==1):
            #print ('possible answers: 1')
            #print ('bits of uncertainty: 0')
            #print ('answer is:',ans_list[0])
            guess = ans_list[0]
        else:
            ans_left = len(ans_list)
            #print ('possible answers:',ans_left)
            #print ('bits of uncertainty:',math.log(ans_left,2))
            a = all_entropy(ans_list)
            guess = a[0][0]
            #for i in range (10):
            #   print (a[i])
    
            possible_answers = {}
            #print ('possible answers:')
            for ans in ans_list:
                possible_answers[ans]=entropy(ans,ans_list)
            sorted_possible_answers = sorted (possible_answers.items(),key = lambda x:x[1],reverse = True)
            #for i in range(10):
            #    try:
            #        print (sorted_possible_answers[i])
            #    except:
            #        pass
            if (sorted_possible_answers[0][1]==a[0][1]):
                guess = sorted_possible_answers[0][0]
                    
    
        #generates outcome
        outcome = colorize (guess,answer)
        user_guess.append(colorize_outcome(guess,outcome))
        for z in user_guess:
            print (z)
    
        #print ('probability of outcome is',probability(guess,outcome,ans_list))
        #print ('bits of info is',bits(guess,outcome,ans_list))
        ans_list = renewed_ans(guess,outcome,ans_list)
    
        print ('\n-----------------------------')
    
        if (guess==answer):
           # print ('\nYOU GUESSED IT.')
           # print ('guesses took:',turn+1)
            break

    #if (guess!=answer):
    #    print ('You failed.')
    #
    #print ('\nEND OF GAME')
    number_of_guess += (turn+1)
    
print ('Average number of guesses:',number_of_guess/2309)
