import listw
import random

#asssigning answer
p = random.randint(0,2308)
#ans = listw.ans[p]
ans = 'hello'
print (ans)


#check if guess is in allowed guesses
def invalid():
    for i in listw.guess:
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

    #going through each letter
    for i in range (5):
        #if letter in guess is in the answer
        if (word[i] in ans):
            #if guess has more of the same letter than the ans:
            if (word.count(word[i])>ans.count(word[i])):
                #initiating counter for each letter
                letter_count = 0
                #running through the word again to count the number of the same letter
                for x in range (5):
                    #if it is the same letter
                    if (word[x] == word [i]):
                        #adds 1 to the counter
                        letter_count += 1
                        #if the current letter has a lower count then the number of letters in the answer
                        if (letter_count<=ans.count(word[i])):
                            #if the letter in the guess matches the letter and position of the letter in the answer
                            if (word[i]==ans[i]):
                                #then the outcome is G
                                outcome[x]='G'
                        
                    else:
                        outcome[x]='B'
            else:
                outcome[i]='Y'
        if (word[i] not in ans):
            outcome[i]='B'
        elif (word[i] == ans[i]):
            outcome[i]='G'
        else:

    print (outcome)

    #if succeeded:
    if (word == ans):
        print ('YAY')
        break

#if failed
if (word != ans):
    print ('nay')




