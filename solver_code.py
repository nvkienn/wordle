from outcomes_all import possible_outcomes
from base_game_code import colorize
import listw
import math
import json
answers_count = 2309
ans_default = listw.ans

with open ('outcomes_combinations.json','r') as f1:
    all_outcomes = json.loads(f1.read())

def renewed_ans (guess,outcome,ans_list):
    renewed_list = []
    for ans in ans_list:
        if (outcome == all_outcomes[ans][guess]):
            renewed_list.append(ans)
    return renewed_list

def probability (guess,outcome,ans_list):
    counter = 0
    for ans in ans_list:
         if (outcome == all_outcomes[ans][guess]):
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
        outcome = tuple(all_outcomes[ans][guess])
        temp[outcome] += 1
    for i in temp.values():
        if (i != 0):
            entropy += i/len(ans_list) * math.log(len(ans_list)/i,2)
    return entropy

def all_entropy (ans_list):
    d_entropy = {}
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
    best_guess = ('ans',0)
    #count = 0
    for guess in listw.guess:
    #    count +=1
    #    if (count%50==0):
    #        print (count)
        info = entropy(guess,ans_list)
        if (info > best_guess[1]):
            best_guess = (guess,info)
    return best_guess

def best_entropy_value (ans_list):
    best_guess = ('ans',0)
    #count = 0
    for guess in listw.guess:
    #    count +=1
    #    if (count%50==0):
    #        print (count)
        info = entropy(iguess,ans_list)
        if (info > best_guess[1]):
            best_guess = (guess,info)
    return best_guess[1]

#for anti wordle
def worst_entropy_all (ans_list):
    d_entropy = {}
    for i in listw.guess:
        a = entropy(i,ans_list)
        d_entropy[i] = a
    sort_entropy = sorted (d_entropy.items(), key = lambda x:x [1], reverse = False) 
    return sort_entropy

def worst_entropy_word (ans_list):
    worst_guess = ('ans',100)
    for guess in ans_list:
        info = entropy(guess,ans_list)
        if (info < worst_guess[1]):
            worst_guess = (guess,info)
    return worst_guess[0]
    
def two_entropy (guess,ans_list):
    total_entropy = 0
    total_entropy += entropy(guess,ans_list)
    all_outcomes = possible_outcomes.copy()
    for outcome in all_outcomes:
        chance = probability(guess,list(outcome),ans_list)
        renewed_list = renewed_ans(guess,list(outcome),ans_list)
        total_entropy += best_entropy_value(renewed_list)*chance
    return total_entropy

def two_entropy_all (ans_list):
    d_entropy = []
    for guess in listw.guess:
        value = two_entropy(guess,ans_list)
        two_entropy_all.append([guess,value])
    return sort_entropy

def practical_entropy (guess,guess_list):
    save = [guess,'2guess',0]
    all_outcomes = possible_outcomes.copy()
    count = 0
    for word in guess_list:
        count +=1
        print (count)
        total_entropy = 0
        for outcome in all_outcomes:
            chance = probability(guess,list(outcome),listw.ans)
            renewed_list = renewed_ans(guess,list(outcome),listw.ans) 
            total_entropy += entropy(word,renewed_list)*chance
        if (total_entropy>save[2]):
            save[1] = word
            save[2] = total_entropy
    save[2] += entropy(guess,listw.ans)
    return save




def first_guesses():
    print ("('soare', 5.885202744292758)\n('roate', 5.884856313732008)\n('raise', 5.878302956493171)\n('reast', 5.867738020843565)\n('raile', 5.865153829041265)")
