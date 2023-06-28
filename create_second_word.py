import listw
from solver_code import all_entropy, renewed_ans,possible_answers,worst_entropy_all
from outcomes_all import possible_outcomes
import json

#with open ('second_word.json','w') as f:
#    all_outcomes = {}
#    for outcome in possible_outcomes:
#        ans_list = renewed_ans('soare',list(outcome),listw.ans)
#        if (len(ans_list)>1):
#            a = all_entropy(ans_list)
#            result = ''
#            for i in a:
#                result+=str(i)
#                result+='\n'
#            result+='possible answers:\n'
#            b = possible_answers(ans_list)
#            for i in b:
#                result+=str(i)
#                result+='\n'
#            result = result[:-1]
#            all_outcomes[str(outcome)]=result
#
#    f.write(json.dumps(all_outcomes,indent=2))

#with open ('anti_second_word.json','w') as f:
#    all_outcomes = {}
#    for outcome in possible_outcomes:
#        ans_list = renewed_ans('qajaq',list(outcome),listw.ans)
#        possible_guesses = renewed_ans('qajaq',list(outcome),listw.guess)
#        if (len(ans_list)>0):
#            a = worst_entropy_all(ans_list,possible_guesses)
#            result = ''
#            for i in a:
#                result+=str(i)
#                result+='\n'
#            result+='possible answers:\n'
#            b = worst_entropy_all(ans_list,ans_list)
#            for i in b:
#                result+=str(i)
#                result+='\n'
#            result = result[:-1]
#            all_outcomes[str(outcome)]=result
#
#    f.write(json.dumps(all_outcomes,indent=2))

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
            for i in a:
                result+=str(i)
                result+='\n'
            result+='possible answers:\n'
            b = worst_entropy_all(ans_list,ans_list)
            for i in b:
                result+=str(i)
                result+='\n'
            result = result[:-1]
            all_outcomes[str(outcome)]=result

    f.write(json.dumps(all_outcomes,indent=2))



