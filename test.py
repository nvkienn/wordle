import json
import listw
from outcomes_all import possible_outcomes
from solver_code import renewed_ans, all_entropy, all_entropy_unrounded
from all_entropy import all_entropy

# with open('anti_second_word.json','r') as f:
#    data = json.loads(f.read())
# print (data[str(('B','G','B','B','B'))])
x = input()
for index, i in enumerate(all_entropy):
    if i[0] == str(x):
        print(i)
        print(index + 1)
