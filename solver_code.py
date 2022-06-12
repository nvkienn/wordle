from outcomes_all import possible_outcomes
from base_game_code import colorize
import listw
import math

def renewed_ans (guess,outcome,ans_list):
    for i in ans_list:
        check_outcome = colorize(guess,i)
        if (outcome != check_outcome):
            ans_list.remove(i)
    return ans_list

def probability (guess,outcome,ans_list):
    counter = 0
    for i in ans_list:
         check_outcome = colorize(guess,i)
         if (outcome == check_outcome):
             counter +=1
    probability = counter/12974
    return probability

def bits (guess,outcome,ans_list):
    chance = probability(guess,outcome,ans_list)
    bits = math.log(1/chance,2)
    return bits

def entropy (guess,ans_list):
    #sum(probability * log2(1/p))
    temp = possible_outcomes.copy()
    entropy = 0
    for i in ans_list:
        a = tuple(colorize(guess,i))
        temp[a] += 1
    for i in temp.values():
        if (i != 0):
            entropy += i/2309 * math.log(2309/i,2)
    return entropy

def all_entropy (ans_list):
    d_entropy = {}
    #for c,i in enumerate (listw.ans):
    #    if (c>100):
    #        break
    for i in listw.guess:
        a = entropy(i,ans_list)
        d_entropy[i] = a
    sort_entropy = sorted (d_entropy.items(), key = lambda x:x [1], reverse = True) 
    for i in range (10):
        print (sort_entropy[i])

def first_guesses():
    print ("('soare', 5.885202744292758)\n('roate', 5.884856313732008)\n('raise', 5.878302956493171)\n('reast', 5.867738020843565)\n('raile', 5.865153829041265)\n('slate', 5.855819244109515)\n('salet', 5.83602278209248)\n('crate', 5.835215982633282)\n('irate', 5.832798880940905)\n('trace', 5.830429108079757)")
