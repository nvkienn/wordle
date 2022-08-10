from solver_code import entropy, all_entropy,first_guesses,best_entropy_value,best_entropy_word,worst_entropy, renewed_ans,two_entropy,probability,two_entropy_all, practical_entropy
from base_game_code import colorize
from outcomes_all import possible_outcomes
import listw
import json

with open ('data.txt','a') as f1:
    f1.write(practical_entropy('soare',listw.guess[2500:3000]))

#two_entropy_v1('soare',listw.ans)
#print(best_entropy(listw.ans))
#print (probability('soare',['B' for i in range (5)],listw.ans))
