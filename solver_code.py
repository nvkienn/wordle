from outcomes_all import possible_outcomes
from base_game_code import colorize
import listw
import math

def probability (guess,outcome):
    counter = 0
    for i in listw.guess:
         check_outcome = colorize(guess,i)
         if (outcome == check_outcome):
             counter +=1
    probability = counter/12974
    return probability

def bits (guess,outcome):
    probability = probability(guess,outcome)
    bits = math.log(1/probability,2)
    return bits

def entropy (guess):
    #sum(probability * log2(1/p))
    entropy = 0
    for i in listw.guess:
        a = tuple(colorize(guess,i))
        possible_outcomes[a] += 1
    for i in possible_outcomes.values():
        if (i != 0):
            entropy += i/12974 * math.log(12974/i,2)
    return entropy
        
        



    




