import listw
from solver_code import all_entropy, renewed_ans,possible_answers,worst_entropy_all
from outcomes_all import possible_outcomes
import json

with open ('anti_third_word.json','w') as f:
    all_outcomes = {}
    for outcome in possible_outcomes:
        ans_list = renewed_ans('qajaq',['B','B','B','B','B'],listw.ans)
        ans_list = renewed_ans('xylyl',list(outcome),ans_list)
        possible_guesses = renewed_ans('qajaq',['B','B','B','B','B'],listw.guess)
        possible_guesses = renewed_ans('xylyl',list(outcome),possible_guesses)
        if (len(ans_list)>0):
            a = worst_entropy_all(ans_list,possible_guesses)
            result = ''
            if (len(possible_guesses)>=5):
                count = 5
            else:
                count = len(possible_guesses)
            for i in range(count):
                result+=str(a[i])
                result+='\n'
            result+='possible answers:\n'
            b = worst_entropy_all(ans_list,ans_list)
            if (len(ans_list)>=5):
                count = 5
            else:
                count = len(ans_list)
            for i in range(count):
                result+=str(b[i])
                if (count-1 != i):
                    result+='\n'
            all_outcomes[str(outcome)]=result

    f.write(json.dumps(all_outcomes,indent=2))



