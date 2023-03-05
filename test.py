import json
from outcomes_all import possible_outcomes
with open('anti_second_word.json','r') as f:
    data = json.loads(f.read())
print (data[str(('B','G','B','B','B'))])
