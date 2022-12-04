import json
import listw
from database import Database

print("BENCH")

db = Database(5)

all_outcomes = {}

# with open("outcomes_combinations.json", "r") as f1:
#     all_outcomes = json.loads(f1.read())


for ans in listw.ans:
    print(db.get(ans)["raise"])
