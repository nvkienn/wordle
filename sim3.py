#trivia
#B stands for Black
#Y stands for Yellow
#G stands for Green
#The above follows the colour coding of the original wordle
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
                        if (letter_count<=ans.count(word[x])):
                            #if the letter in the guess matches the letter and position of the letter in the answer
                            if (word[x]==ans[i]):
                                #then the outcome is G
                                outcome[i]='G'
                            #if letter is in the guess but not the right position 
                            else:
                                #then the outcome is Y
                                outcome[x]='Y'
                        #if the letter count is greater than the number of that letter in the asnwer
                        else:
                            #then outcome is B
                            outcome[x]='B'

            #if guess has less of the same letter than answer
            else:
                #if letter in the guess matches the postion of the letter in the answer
                if (word[i]==ans[i]):
                    #then outcome is G
                    outcome[x]='G'
                #if letter does not match position
                else:
                    #then outcome is Y
                    outcome[x]='Y'

        #if letter in guess not in answer
        else:
            #then outcome is B
            outcome[i] = 'B'

    print (outcome)

    #if succeeded:
    if (word == ans):
        print ('YAY')
        break

#if failed
if (word != ans):
    print ('nay')




