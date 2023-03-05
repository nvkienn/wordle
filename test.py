import json
from outcomes_all import possible_outcomes
with open('second_word.json','r') as f:
    data = json.loads(f.read())
print (data[str(tuple(['B' for i in range(5)]))])
