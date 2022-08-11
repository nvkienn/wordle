from solver_code import entropy, all_entropy,first_guesses,best_entropy_value,best_entropy_word,worst_entropy, renewed_ans,two_entropy,probability,two_entropy_all, practical_entropy
from base_game_code import colorize
from outcomes_all import possible_outcomes
import listw
import json

with open ('data.txt','r') as f1:
    data = f1.readlines()
result = ['a','a',0]
for i in data:
    #if (i[2]>result[2]):
    #    result = i
    a = list[i]
    print (type(a))
    


#two_entropy_v1('soare',listw.ans)
#print(best_entropy(listw.ans))
#print (probability('soare',['B' for i in range (5)],listw.ans))
