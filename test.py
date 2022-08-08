from solver_code import entropy, all_entropy,first_guesses,best_entropy_value,best_entropy_word,worst_entropy, renewed_ans,two_entropy,probability,two_entropy_all
from base_game_code import colorize
import listw
import json

x = two_entropy_all(listw.ans)
with open ('entropy_two.json','w') as f1:
    f1.write(json.dumps(x,indent = 2))




#two_entropy_v1('soare',listw.ans)
#print(best_entropy(listw.ans))
#print (probability('soare',['B' for i in range (5)],listw.ans))
