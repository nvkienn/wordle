import listw
import random


#asssigning answer
p = random.randint(0,2308)
ans = listw.ans[p]
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
    repeat = {}

    #the guess
    word = input()

    #computating the outcome
    while (word.isalpha == False or len(word) != 5 or invalid()):
        word = input()
    for i in range (5):
        if (word[i] not in ans):
            outcome[i]='B'
        elif (word[i] == ans[i]):
            outcome[i]='G'
        else:
            outcome[i]='Y'

    #exceptions with more than 1 of the same letter in a guess
    for i in word:
        if (i in repeat):
            d[str(i)]+=1
        else:
            d[str(i)]=1
    for i in repeat.items():
        if (i[1]>=2):
            if (


    #if succeeded:
    if (word == ans):
        print ('YAY')
        break

#if failed
if (word != ans):
    print ('nay')




