from base_game_code import colorize,invalid,ans_generator
ans = ans_generator()
print (ans)
for i in range (6):
    guess = input ("Enter guess:")
    while (invalid(guess)):
        guess = input ("Invalid, enter guess:")
    outcome = colorize (guess,ans)
    print (outcome)
    if (guess==ans):
        print ('YOU GUESSED IT')
        break
if (guess!=ans):
    print ('You failed.')

