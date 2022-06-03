from random import seed
from random import randint
seed(8)

#wordholders
wordlist = ["hello","james","xenok","zerif","plant","bells","juked","fleet","plead","ratio","hemps","lucky"] #acceptable guesses
answer = ["hello","james","xenok","zerif","plant","bells","juked","fleet","plead","ratio","hemps","lucky"] #possible answers
tlist = list(wordlist+answer)
cguess = ["","","","",""]

#functions
def checkword():
    global word
    while word not in wordlist or len(word) != 5:
        word = input("Invalid, Input a guess: ")

def getanswer(): #randomly chooses an answer, you can change seed each time
    x = randint(0,len(answer)-1)
    return(answer[x])

def getguess():
    global word
    word = input("Input your next guess: ")
    checkword()
    return(word)

def checkguess(words,ans):
    global cguess
    for i in range(0,5):
        if words[i] in ans:
            if words[i] == ans[i]:
                cguess[i] = "G"#word[i].upper()
            else:
                cguess[i] = "Y"#word[i].lower()
        else:
            cguess[i] = "B"#"*"
    return(cguess)

def entropy():
    global wordlist, answer, tlist
    for answers in answer:
        for guess in wordlist:
            word = guess
            if checkguess(guess,answers) != ["G","G","G","G","G"]:
                for guess2 in wordlist:
                    if guess2 != guess:
                        if (getvalue(checkguess(guess2,answers)) == getvalue(checkguess(guess,answers))) and (checkguess(guess2,answers) != ["B","B","B","B","B"]):
                            print("Ans:",answers,"original guess: ",guess,"matching guess: ",guess2)
                print("\n")
        
            
            #print("ans: ",answers,"guess: ",guess)
            #print(checkguess(guess, answers))
            
    
def getvalue(w):
    bc = 0
    yc = 0
    gc = 0
    for i in w:
        if i == "B":
            bc += 1 
        else:
            if i == "Y":
                yc += 1
            else:
                gc += 1
    return([bc,yc,gc])
#choosing answer
ans = str(getanswer())
cans = []
for i in str(ans):
    cans.append(i.upper())
#start
print("* * * * *","\n")
print("Wordle! Capital letter means green and lower case means yellow. * means gray")
word = input("Input a guess: ")
checkword()

#checking guess
print(checkguess(word,ans))
#loop
while cguess != ["G","G","G","G","G"]:
    word = getguess()
    checkword()
    print(checkguess(word,ans))
print("congrats")

#entropy
"""
for tans in answer:
    for guess in wordlist:
        word = guess
        result = checkguess(tans)
        if result == ["B","B","B","B","B"]: #if there are no matches
            fesfs #remove all words in possible guesses with 
        else:

        """
