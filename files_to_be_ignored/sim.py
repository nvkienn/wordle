import listw
import random

#asssigning answer
p = random.randint(0,2308)
#ans = listw.answers[p]
ans = 'hello'
print (ans)


#check if guess is in allowed guesses
def invalid():
    for i in listw.guesses:
        if (word == i):
            return False
    return True


#The simulator:
for i in range (5):
    outcome = ['' for i in range (5)]

    #the guess
    word = input()

    #checking that guess is valid:
    '''
    while (word.isalpha == False or len(word) != 5 or invalid()):
    '''
    while (word.isalpha == False or len(word) != 5):
        word = input('Invalid, try again:')

    #the simulator:
    for i in range (5):
        if (word[i] not in ans):
            outcome[i]='B'
        elif (word[i] == ans[i]):
            outcome[i]='G'
        else:
            #if guess has more of the same letter than the ans:
            if (word.count(word[i])>ans.count(word[i])):
                letter_count = 0
                for x in range (5):
                    if (word[x] == word [i]):
                        letter_count += 1
                        if (letter_count<=ans.count(word[i])):
                            if (outcome[x]!='G'):
                                outcome[x]='Y'
                        else:
                            outcome[x]='B'
            else:
                outcome[i]='Y'

    print (outcome)

    #if succeeded:
    if (word == ans):
        print ('YAY')
        break

#if failed
if (word != ans):
    print ('nay')




