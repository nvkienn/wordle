from base_game_code import colorize,invalid,ans_generator

#generates answer
ans = ans_generator()
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
    if (guess==ans):
        print ('YOU GUESSED IT')
        break

if (guess!=ans):
    print ('You failed.')

