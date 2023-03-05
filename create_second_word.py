import listw
from solver_code import all_entropy, renewed_ans,possible_answers
from outcomes_all import possible_outcomes
from base_game_code import colorize
import json

with open ('second_word.json','w') as f:
    all_outcomes = {}
    for outcome in possible_outcomes:
        ans_list = renewed_ans('soare',list(outcome),listw.ans)
        if (len(ans_list)>1):
            entropy_words = all_entropy(ans_list)
            result = ''
            for i in range(3):
                result+=str(entropy_words[i])
                result+='\n'
            answers = possible_answers(ans_list)
            result+='possible answers:\n'
            for i in range(3):
                try:
                    result+=str(answers[i])
                    if (i!=2):
                        result+='\n'
                except:
                    pass
            all_outcomes[str(outcome)]=result

    f.write(json.dumps(all_outcomes,indent=2))



