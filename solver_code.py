from outcomes_all import possible_outcomes
from base_game_code import colorize
import listw
import math

answers_count = 2309
ans_default = listw.ans

def renewed_ans (guess,outcome,ans_list):
    renewed_list = []
    for ans in ans_list:
        check_outcome = colorize(guess,ans)
        if (outcome == check_outcome):
            renewed_list.append(ans)
    return renewed_list

def probability (guess,outcome,ans_list):
    counter = 0
    for i in ans_list:
         check_outcome = colorize(guess,i)
         if (outcome == check_outcome):
             counter +=1
    probability = counter/len(ans_list)
    return probability

def bits (guess,outcome,ans_list):
    chance = probability(guess,outcome,ans_list)
    bits = math.log(1/chance,2)
    return bits

def entropy (guess,ans_list):
    #sum(probability * log2(1/p))
    temp = possible_outcomes.copy()
    entropy = 0
    for ans in ans_list:
        outcome = tuple(colorize(guess,ans))
        temp[outcome] += 1
    for i in temp.values():
        if (i != 0):
            entropy += i/len(ans_list) * math.log(len(ans_list)/i,2)
    return entropy

def all_entropy (ans_list):
    d_entropy = {}
    #for c,i in enumerate (listw.ans):
    #    if (c>100):
    #        break

    #look through all possible guesses
    for i in listw.guess:
        a = entropy(i,ans_list)
        d_entropy[i] = a
    sort_entropy = sorted (d_entropy.items(), key = lambda x:x [1], reverse = True) 
    return sort_entropy

def possible_answers(ans_list):
    d_entropy = {}
    for i in ans_list:
        a = entropy(i,ans_list)
        d_entropy[i] = a
    sort_entropy = sorted (d_entropy.items(), key = lambda x:x [1], reverse = True) 
    return sort_entropy

def best_entropy (ans_list):
    temp = ('ans',0)
    for i in listw.guess:
        a = entropy(i,ans_list)
        if (a > temp[1]):
            temp = (i,a)
    return temp[0]

#for anti wordle
def worst_entropy (ans_list):
    d_entropy = {}
    for i in listw.guess:
        a = entropy(i,ans_list)
        d_entropy[i] = a
    sort_entropy = sorted (d_entropy.items(), key = lambda x:x [1], reverse = False) 
    return sort_entropy
    
def two_entropy (guess,ans_list):
    #soare - different outcomes - reduce the word list - find best entropy word - multiply by probability of outcome
    #dictionary {soare:{
    d_entropy = {}
    for i in listw.guess:
        a = entropy(i,ans_list)
        d_entropy[i] = a
    sort_entropy = sorted (d_entropy.items(), key = lambda x:x [1], reverse = True) 
    return sort_entropy


def first_guesses():
    print ("('soare', 5.885202744292758)\n('roate', 5.884856313732008)\n('raise', 5.878302956493171)\n('reast', 5.867738020843565)\n('raile', 5.865153829041265)")
