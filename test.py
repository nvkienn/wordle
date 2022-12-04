import json
import time

start_time = time.time()
with open ('outcomes_combinations.json','r') as f1:
    data = json.loads(f1.read())
print (data['fight']['while'])    
print (time.time()-start_time)


#two_entropy_v1('soare',listw.ans)
#print(best_entropy(listw.ans))
#print (probability('soare',['B' for i in range (5)],listw.ans))
