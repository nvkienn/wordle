import json
import listw
from base_game_code import colorize
d = {}
count = 0
for ans in listw.ans:
    count+=1
    print(count)
    d[ans] = {}
    for guess in listw.guess:
        d[ans][guess] = colorize(guess,ans)

with open ('outcomes_combinations.json','w') as f1:
    f1.write(json.dumps(d,indent = 4))


